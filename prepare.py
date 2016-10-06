import os
import settings
import pandas as pd


def read():
    prices = pd.read_csv(os.path.join(settings.DATA_DIR, settings.DATA_FILENAME),header=0)
    prices = clean(prices)
    return prices


def clean(prices):
    (m, n) = prices.shape
    prices['Date'] = pd.to_datetime(prices['﻿Date'], format='%d-%b-%y')
    prices = prices.loc[:, ['Date', 'Open', 'Close']]

    # Add new column "Close Price at the Previous Day" and "Open Price at the Previous Day"
    prevColumn = prices.loc[:, ['Open', 'Close']].assign(index = lambda x: x.index-1)
    prevColumn = prevColumn.set_index('index')
    prices = prices.join(prevColumn, rsuffix='Prev')

    # Add new column "Close Price at the Day Before" and "Open Price at the Day Before"
    prevColumn = prices.loc[:, ['Open', 'Close']].assign(index = lambda x: x.index-2)
    prevColumn = prevColumn.set_index('index')
    prices = prices.join(prevColumn, rsuffix='Prev2')

    prevColumn = prices.loc[:, ['Open', 'Close']].assign(index = lambda x: x.index-3)
    prevColumn = prevColumn.set_index('index')
    prices = prices.join(prevColumn, rsuffix='Prev3')

    prevColumn = prices.loc[:, ['Open', 'Close']].assign(index = lambda x: x.index-4)
    prevColumn = prevColumn.set_index('index')
    prices = prices.join(prevColumn, rsuffix='Prev4')

    prevColumn = prices.loc[:, ['Open', 'Close']].assign(index = lambda x: x.index-5)
    prevColumn = prevColumn.set_index('index')
    prices = prices.join(prevColumn, rsuffix='Prev5')

    # No need now to save the fifth days data
    prices = prices[:m-5]

    return prices


def write(data):
    data.loc[:, ['Date','Open','OpenPrev','ClosePrev','OpenPrev2','ClosePrev2','OpenPrev3','ClosePrev3',
                 'OpenPrev4','ClosePrev4','OpenPrev5','ClosePrev5']].\
        to_csv(os.path.join(settings.PROCESSED_DIR, "trainX.csv"), index=False)
    data.loc[:, ['Close']].to_csv(os.path.join(settings.PROCESSED_DIR, "trainY.csv"), index=False)


if __name__ == "__main__":
    prices = read()
    write(prices)