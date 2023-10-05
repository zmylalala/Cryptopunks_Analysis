# This code will analysis the data of crypto-punks
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import datetime


def trade_trend(df):
    # First draw the number of trades and volumes over time
    # Examine data first
    # print(trades_data_df.dtypes)
    # Construct a dataframe with date, number of trades and volumes
    # Split the date and time
    df['date'] = pd.to_datetime(df.block_time)
    df['date'] = df['date'].apply(lambda x: x.strftime("%Y-%m-%d"))
    # df['trade_volumes'] = df.groupby('date')['amount_usd'].transform('sum')
    # trades_data_df['trade_times'] = trades_data_df.groupby('date', as_index=False)['amount_usd'].count()
    # print(trades_data_df['trade_times'].head())
    data = df.groupby('date').agg({'amount_usd': 'sum'})

    # Check the length and the type for preparing drawing
    print(data.index)
    print(data.amount_usd)

    plt.title("none")
    plt.xlabel('date', fontsize=10)
    plt.ylabel('total_amount_usd', fontsize=10)
    plt.plot(data.index, data.amount_usd)

    x_major_locator = MultipleLocator(180)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    plt.tick_params(axis='both', which='both', labelsize=10)
    plt.gcf().autofmt_xdate()
    plt.show()


def main():
    # Read the data
    trades_data_df = pd.read_csv('./data/trades_data.csv')
    trade_trend(trades_data_df.copy())


if __name__ == '__main__':
    main()


