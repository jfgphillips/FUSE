# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from solvayFactoryLinear import solvay_process
import functionTester as ft

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    brine = {"NaCl": 116.88, "H2O": 100, "volume": 100} # volume in cm3
    limestone = {"CaCO3": 100.086} # mass in grams
    coke = {"C": 100} # mass in grams
    init_ammonia = {"NH3": 50} # volume?
    total_energy, total_CO2, total_light_soda_ash, total_calcium_chloride = solvay_process(brine, limestone, coke, init_ammonia) # 105.988 g Na2CO3 (1Mol)
    print(total_energy, total_CO2, total_light_soda_ash, total_calcium_chloride)
    ##extraction_rate_tonnes_per_day = ft.taylors_law(4000000, 250)
    #print(extraction_rate_tonnes_per_day)
    room_and_pillar = ft.machine_output_calc(2948350.405, 7)  # mine output in tonnes, number of miners
    longwall = ft.machine_output_calc(3200000, 1)  # mine output in tonnes, number of miners
    #print(output_per_miner)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
