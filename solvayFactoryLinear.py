import numpy as np
from molmass import Formula


def solvay_process(brine, limestone, coke, init_ammonia):  # maybe a brine with percentage impurities as a dictionary

    def ammonia_saturator(brine, ammonia, temperature, time):  # step 1
        saturated_soln = [brine, ammonia]  # list with concentrations of each
        print(saturated_soln)
        energy_units = np.nan

        return energy_units, saturated_soln

    def lime_kiln(limestone, coke, temperature, time):  # step 2
        CO_2 = np.nan
        quick_lime = np.nan
        energy_units = np.nan

        return energy_units, CO_2, quick_lime

    def slacker(CaO, water, temperature, time):  # step 2.1
        slack_lime = np.nan
        energy_units = np.nan

        return energy_units, slack_lime

    def solvay_tower(saturated_soln, sum_CO_2, temperature, time):  # step 3

        # for key, value in saturated_soln:

        react_soln = np.nan
        energy_units = np.nan
        impurities = np.nan  # not sure if this is required

        return energy_units, react_soln

    def filtr(reacted_soln, temperature, time):  # add impurities here #step 4 + 5

        solid_sodium_bicarbonate = np.nan  # and solid impurities
        aqueous_ammonium_chloride = np.nan  # and aqueous impurities

        energy_units = np.nan

        return energy_units, aqueous_ammonium_chloride, solid_sodium_bicarbonate

    def ammonia_recovery_tower(slacked_lime, ammonium_chloride, temperature, time):  # step 6
        cal_chloride = np.nan
        rec_ammonia = {"NH3": 150}
        energy_units = np.nan
        return energy_units, cal_chloride, rec_ammonia

    def calciner(sodium_bicarbonate, temperature, time):  # step 7
        calciner_CO_2 = np.nan
        light_soda_ash = np.nan
        energy_units = np.nan

        return energy_units, calciner_CO_2, light_soda_ash

    total_CO2 = 0
    total_energy = 0
    ammonia = {"NH3": 0}
    total_light_soda_ash = 0
    total_calcium_chloride = 0
    water = 100

    for i in range(0, 10, 1):  # how many repeats?

        #print(i)

        if ammonia["NH3"] == 0:
            ammonia = init_ammonia
            #print("this is init ammonia", ammonia)

        else:
            ammonia = ammonia
            #print("this is the recycled ammonia", ammonia)

        E_ammonia_sat, solvay_precursor = ammonia_saturator(brine, ammonia, 100, 30)

        E_kiln, Lime_CO_2, quicklime = lime_kiln(limestone, coke, 100, 30)
        total_CO2 += Lime_CO_2

        E_slacker, slacked_lime = slacker(quicklime, water, 100, 30)

        E_solvay_tower, reacted_soln = solvay_tower(solvay_precursor, total_CO2, 100, 30)

        E_filter, ammonium_chloride, sodium_bicarbonate = filtr(reacted_soln, 100, 30)

        E_ammonia_rec, calcium_chloride, recovered_ammonia = ammonia_recovery_tower(slacked_lime, ammonium_chloride,
                                                                                    100, 30)
        ammonia["NH3"] = recovered_ammonia["NH3"]
        total_calcium_chloride += calcium_chloride

        E_calciner, calciner_CO2, light_soda_ash = calciner(sodium_bicarbonate, 100, 30)
        total_light_soda_ash += light_soda_ash
        total_CO2 += calciner_CO2
        total_energy += (E_ammonia_sat + E_kiln + E_slacker + E_solvay_tower + E_filter + E_ammonia_rec + E_calciner)

    return total_energy, total_CO2, total_light_soda_ash, total_calcium_chloride
