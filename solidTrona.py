import numpy as np
import pandas as pd


def solid_trona_mine():
    def power_consumption(motor_HP, running_load, nameplate_rating, per_unit_run_time, per_unit_time, op_hrs):
        """
        :param motor_HP: engine horse power
        :param running_load: how much the unit is carrying
        :param nameplate_rating: max operating rating
        :param per_unit_run_time: how much the unit is being run
        :param per_unit_time: per specified time (standardised hrs)
        :param op_hrs: intervals of a day, week or month

        :return: unit_energy_consumption: Energy/month (kW hours)
        """
        motor_kW = motor_HP * 0.746  # conversion factor HP -> kW
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

        return drive_HP



    def shaft_access():
        def drum_hoist():
            return np.nan

        def elevator_commute():
            return np.nan



    def stope_ops():
        def horizontal_conveyor(cost_of_conveyer, belt_cost):
            op_maintenance = (cost_of_conveyer * 0.02) + (belt_cost * 0.05)

            return np.nan

        def people_transport():
            return np.nan

        def load_hall_dump_vehicle():
            return np.nan

        def shuttle_car():
            return np.nan

        def rail():
            return np.nan

        def ventilation():
            return np.nan

    def room_and_pillar_method():
        def continuous_borer_miner():
            return np.nan

        def roof_bolter():
            return np.nan

        return np.nan

    def longwall_method():
        def longwall_miner():
            return np.nan

        def hydraulic_supports():
            return np.nan

    def ramp_access():
        def inclined_conveyor():
            return np.nan

        def road_commute():
            return np.nan

    return np.nan
