
# Raw Package
import numpy as np
import pandas as pd

# Data Source
import yfinance as yf

# Get Bitcoin data
# 이전 24시간동안의 데이터를 15분간격으로 가져옴
#data = yf.download(tickers='BTC-USD', period='24h', interval='5m')


def get_data(tickers, period, interval):
    """
    ==========================
    About tickers
    ==========================
    Bitcoin -> BTC
    Ethereum -> ETH
    Binanace Coin -> BNB
    Dogecoin -> DOGE
    Cardano -> ADA
    Tether ->  USDT
    XRP -> XRP
    Polkadot -> DOT
    Internet Computer -> ICP
    Bitcoin Cash -> BCH
    ==========================
    About period & interval
    ==========================
    https://medium.com/analytics-vidhya/python-how-to-get-bitcoin-data-in-real-time-less-than-1-second-lag-38772da43740
    """
    try:
        data = yf.download(tickers=tickers, period=period, interval=interval)
        return data
    except:
        print("error in get data")


def create_csv(data):
    """"This function generates a csv file with cryptocurrency data's"""
    data.to_csv("CryptoData.csv")


def get_datatime(data):
    """This fuction returs a DatetimeIndex"""
    return data.index


def get_open(data):
    return data['Open']

# 모든 Datatime 데이터를 가져오는법
# print(data.index)

# 모든 Open 데이터를 가져오는법
# High,Low등을 가져오려면 괄호안의 Open대신 해당하는 인덱스 이름을 입력하면됨
# data['Open']

# 자세한 사항은 https://pandas.pydata.org/docs/reference/frame.html 참조
