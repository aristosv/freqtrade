from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
class Freqtrade_backtest_validation_freqtrade1(IStrategy):

    stoploss = -0.4
    timeframe = '1h'
    trailing_stop = True
    trailing_stop_positive = 0.01
    trailing_stop_positive_offset = 0.02
    trailing_only_offset_is_reached = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # SMA - Simple Moving Average
        dataframe['fastMA'] = ta.SMA(dataframe, timeperiod=14)
        dataframe['slowMA'] = ta.SMA(dataframe, timeperiod=28)
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['fastMA'] > dataframe['slowMA'])
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['fastMA'] < dataframe['slowMA'])
            ),
            'sell'] = 1
        return dataframe
