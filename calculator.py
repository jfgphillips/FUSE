import pandas as pd

def machine_output_calc(soda_ash_tpy, mining_package):
    """
    :param soda_ash_tpy:
    :param mining_package: how many mining packages involved
           e.g
           bolter continuous miner shuttle
           longwall shearer + 2 borer miners + 1 bleeder + shuttle cars
    :return: an estimate of rock and ore tonnes per hour per mining package
    """
    SODA_ASH_CONVERSION_EFFICIENCY = 0.588
    DEPOSIT_MINERAL_GRADE = 0.9
    PRODUCTION_HRS_wk = 110

    ore_tpy = soda_ash_tpy/SODA_ASH_CONVERSION_EFFICIENCY
    ore_and_rock_tpy = ore_tpy/DEPOSIT_MINERAL_GRADE
    ore_and_rock_tpy_per_miner = ore_and_rock_tpy / mining_package
    ore_and_rock_tpm_per_miner = ore_and_rock_tpy_per_miner/52
    ore_and_rock_tph_per_miner = ore_and_rock_tpm_per_miner/PRODUCTION_HRS_wk
    print("The output of each mining package per hour is: ", ore_and_rock_tph_per_miner,'tph \n',"The output of each mining package per week is: ", ore_and_rock_tph_per_miner*PRODUCTION_HRS_wk, 'tpwk')
    return ore_and_rock_tph_per_miner

def taylors_law(expected_reserves, days_per_year):
    """
    :param expected_reserves: proven + probable reserves of a mine (tonnes)
    :param days_per_year: mine operation days in a year (d/yr)
    :return: a value in tonnes per day for most economical mining rates
    """
    numerator = expected_reserves ** (3 / 4)
    mining_rate = 5 * (numerator / days_per_year)
    return mining_rate


def power_consumption(motor_kW, running_load, nameplate_rating, per_unit_run_time, per_unit_time, op_hrs):
    """
    :param motor_kW: engine horse power
    :param running_load: how much the unit is carrying
    :param nameplate_rating: max operating rating
    :param per_unit_run_time: how much the unit is being run
    :param per_unit_time: per specified time (standardised hrs)
    :param op_hrs: intervals of a day, week or month

    :return: unit_energy_consumption: Energy/month (kW hours)
    """
    # motor_kW = motor_HP * 0.746  # conversion factor HP -> kW
    load_factor = running_load/nameplate_rating  # what capacity is equipment being used
    utilisation_factor = per_unit_run_time/per_unit_time
    unit_energy_consumption = motor_kW * load_factor * utilisation_factor * op_hrs  # standardised value

    return unit_energy_consumption

def belt_conveyor_power(belt_speed, belt_length, gradient, conveyor_output, drive_train_efficiency):
    """
    credit for this calculation: hard rock mininers handbook
    might be an idea to standardise units across the process

    :param belt_speed: speed of belt feet per minute
    :param belt_length: length of belt in feet
    :param gradient: slope of the conveyor
    :param conveyor_output: conveyor output tonnes per hour
    :param drive_train_efficiency: efficiency of the drive train

    :return: drive power requirements for belt conveyor
    """
    belt_df = pd.read_csv('data/equivalent_lift_matrix.csv')
    belt_df.set_index('belt speed feet per minute', inplace=True)

    column = str(belt_length)

    H_f = belt_df[column].loc[belt_speed]

    Q = conveyor_output * 36.7434  # tonne per hour conv to pounds per min
    H_g = gradient * 10  # gradient given as a percentage * 10 for some reason
    H = H_g + H_f  # total lift, H = gradient + length/speed table (.csv file)
    belt_HP = (Q * H) / 33000  # conversion to horse power
    drive_HP = belt_HP / drive_train_efficiency
    drive_kW = drive_HP * 0.746

    return drive_kW

def drum_hoist(hoisting_dist_m, production_avaliability, production_capacity_tpd):
    """
    :param hoisting_dist_m: shaft distance in meters
    :param production_avaliability: how much of the week the shaft is availiable for haulage ops
    :param production_capacity_tpd: mines total production capacity in a day
    :return: skip capacity required for haulage
    """
    optimum_line_spd = 0.405 * hoisting_dist_m**(1/2)
    cycle_time = hoisting_dist_m/optimum_line_spd + 40  # see formula page 119-120 miners handbook
    trips_hr = 3600/cycle_time
    trips_day = trips_hr*24*production_avaliability
    skip_capacity = production_capacity_tpd/trips_day

    return skip_capacity

