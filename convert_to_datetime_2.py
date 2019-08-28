import datetime as dt
import pandas as pd


if __name__ == '__main__':
    df = pd.read_json('sample.json')
    df = df.assign(
        PurchaseDate=pd.to_datetime(df['PurchaseDate'], format='%Y-%m-%d')
    )
    print(df['PurchaseDate'])
