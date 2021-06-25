import pandas as pd

class mine_att:
    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="macro details", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.depth = self.df['value'].loc['depth']
        self.expected_reserves = self.df['value'].loc["proven + probable deposits"]
        self.mine_production = self.df['value'].loc["mine operating production"]
        self.ore_grade = self.df['value'].loc["ore grade"]
        self.ore_density = self.df['value'].loc["location"]
        self.ore_mkt_price = self.df['value'].loc["ore market price"]
        return


class continuousMiner_att:

    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="continuous miner", skiprows=1)
        self.df.set_index('key', inplace=True)
        print(self.df.index)
        self.production_output = self.df['value'].loc["production output"]
        self.usage = self.df['value'].loc["usage"]
        self.maintenance = self.df['value'].loc["maintenance"]
        self.power = self.df['value'].loc["power"]
        self.workers = self.df['value'].loc['workers']
        return


class roofBolter_att:
    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="roof bolter", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.model = self.df['value'].loc['model']
        self.usage = self.df['value'].loc['usage']
        self.maintenance = self.df['value'].loc['maintenance']
        self.power = self.df['value'].loc['power']
        self.workers = self.df['value'].loc['workers']
        return


class shuttleCar_att:
    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="shuttle car", skiprows=1)
        self.df.set_index('key', inplace = True)
        self.model = self.df['value'].loc['model']
        self.nameplate_rating = self.df['value'].loc['nameplate rating']
        self.usage = self.df['value'].loc['usage']
        self.maintenance = self.df['value'].loc['maintenance']
        self.power = self.df['value'].loc['power']
        self.workers = self.df['value'].loc['workers']
        return


class worker_att:
    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="worker", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.wage = self.df['value'].loc['wage']
        self.shift_length = self.df['value'].loc['shift length']
        return

class LHD_att:
    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="LHD", skiprows=1)
        self.df.set_index('key', inplace=True)
