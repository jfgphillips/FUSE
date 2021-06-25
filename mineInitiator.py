import pandas as pd

def init_continuous_miner():
    df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="continuous miner", skiprows=1)
    df.set_index('key', inplace=True)
    print(df)
    return


def init_mine_attributes():
    df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="macro details", skiprows=1)
    df.set_index('key', inplace=True)
    print(df)
    return

