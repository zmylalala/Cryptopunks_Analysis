# This code will analysis the data of crypto-punks
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import datetime
import plotly.express as px


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
    # print(data.index)
    # print(data.amount_usd)

    plt.figure(figsize=(8, 4))
    plt.xlabel('date', fontsize=10)
    plt.ylabel('total trade amount (usd)', fontsize=10)
    plt.plot(data.index, data.amount_usd)
    plt.axvline('2021-01-31', color='b', linestyle='--', label='2021-01-31')
    plt.axvline('2022-03-01', color='r', linestyle='--', label='2022-03-01')
    plt.legend()
    plt.grid(color="k", linestyle=":", axis='y')
    x_major_locator = MultipleLocator(120)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    plt.tick_params(axis='both', which='both', labelsize=10)
    plt.gcf().autofmt_xdate()
    # plt.show()
    plt.savefig('./pics/date_usd.png', dpi=600)


def buyers(df):
    df['date'] = pd.to_datetime(df.evt_block_time)
    df['date'] = df['date'].apply(lambda x: x.strftime("%Y-%m-%d"))
    df = df.sort_values(by='date')
    data = df.groupby('date').nunique()['toAddress']
    data2 = df.groupby('date').nunique()['punkIndex']
    plt.figure(figsize=(8, 4))
    # plt.title("none")
    plt.xlabel('date', fontsize=10)
    plt.ylabel('transactions', fontsize=10)
    x = np.arange(len(data.index))
    width = 0.5
    plt.bar(x - width / 2, data, width, label='unique buyers')
    plt.bar(x + width / 2, data2, width, label='unique punks traded')
    plt.legend(frameon=False)
    x_t = np.arange(11)
    uniq_date = np.unique(df.date.values)
    xtl = [uniq_date[i] for i in range(0, len(data.index), int(len(data.index)/10))]
    plt.xticks(x_t+x_t*len(data.index)/10, xtl)
    plt.tick_params(axis='both', which='both', labelsize=10)
    plt.gcf().autofmt_xdate()
    # plt.show()
    plt.savefig('./pics/buyers.png', dpi=600)


def freq_trans(df1, df2):
    # First calculate the most frequently transferred punks id and its volume
    data = df1.groupby('punkIndex').agg({'eth_value': 'sum'})
    data['transfer_count'] = df1.groupby('punkIndex').agg({'eth_value': 'count'})
    data = data.sort_values(by="eth_value", ascending=False)
    # print(data.head(10))
    top_punk = data.head(100)
    top_punk_with_att = top_punk.join(df2)
    output = top_punk_with_att[['eth_value', 'transfer_count', 'attribute_list']]
    output.to_csv('./outputData/top_punk_freq.csv')


def owners_analysis(df):
    data = df['current_owner'].value_counts()
    data = data.head(100)
    data.to_csv('./outputData/top_owner_counts.csv')


def punk_analysis(df):
    # df = df.explode("type")
    data = df.groupby('type').nunique()
    # fig = plt.bar(df.drop_duplicates("punk_id")['type'].value_counts().rename_axis('type').reset_index(name='counts'),
    #             x="type", y="counts", color="type", title="Cryptopunk Type Counts")
    # fig.show()
    plt.figure(figsize=(8, 4))
    # width = 0.5
    print(df.type)
    print(data)
    # plt.bar(df['type'], data, width, label='1')
    # plt.show()


def main():
    # Read the data
    trades_data_df = pd.read_csv('./data/trades_data.csv')
    trade_trend(trades_data_df.copy())
    cp_market_df = pd.read_csv('./data/CryptoPunksMarket_evt_PunkBought.csv')
    buyers(cp_market_df.copy())
    punks_data_df = pd.read_csv('./data/punks_data.csv')
    freq_trans(cp_market_df.copy(), punks_data_df.copy())
    current_owners_per_token_df = pd.read_csv('./data/current_owners_per_token.csv')
    owners_analysis(current_owners_per_token_df.copy())
    # txn_history_df = pd.read_json("./data/txn_history.jsonl", lines=True)
    # punk_analysis(txn_history_df.copy())


if __name__ == '__main__':
    main()


