# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from solvayFactoryLinear import solvay_process
from functionTester import belt_conveyor_power

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
    drive_HP = belt_conveyor_power(300, 1000, 0, 300, 0.885)
    print (drive_HP)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
