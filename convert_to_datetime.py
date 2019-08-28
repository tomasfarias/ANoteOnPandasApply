import datetime as dt
import pandas as pd


def str_to_datetime(date_str, fmt):
    return dt.datetime.strptime(date_str, fmt)


if __name__ == '__main__':
    df = pd.read_json('sample.json')
    df = df.assign(
        PurchaseDate=df['PurchaseDate'].apply(str_to_datetime, fmt="%Y-%m-%d")
    )
    print(df['PurchaseDate'])
