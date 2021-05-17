import freqtrade.vendor.qtpylib.indicators as qtpylib
from pandas import DataFrame, DatetimeIndex, merge
from freqtrade.strategy.interface import IStrategy
from typing import Dict, List
from functools import reduce
import talib.abstract as ta
class $class(IStrategy):

    stoploss = -0.4
    timeframe = '1h'
    trailing_stop = True
    trailing_stop_positive = 0.01
    trailing_stop_positive_offset = 0.02
    trailing_only_offset_is_reached = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        bollinger = qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=3)
        dataframe['bb_lowerband'] = bollinger['lower']
        dataframe['bb_middleband'] = bollinger['mid']
        dataframe['bb_upperband'] = bollinger['upper']
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['close'] <= 0.98 * dataframe['bb_lowerband'])
            )
            ,
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (),
            'sell'] = 1
        return dataframe
