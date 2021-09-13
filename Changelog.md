**13/09/2021**
- Modified "trailing_stop_positive_offset" to 0.015 to ensure at least 1% profit per trade
- Removed sell signal since we depend on "trailing_stop" for sales

**26/08/2021**
- Due to a [problem](https://github.com/freqtrade/freqtrade/issues/5479) with older panda versions the Bollinger Bands strategy was not working properly. It has now been fixed.
- Set profit to 1.2% with a 0.5% deviation

**19/08/2021**
- improved "pair_blacklist"
- added StaticPairList combined with VolumePairList

**15/08/2021**
- removed "amend_last_stake_amount". Now defaults to "false"
- added "unit": "minutes" in "unfilledtimeout"
- updated "bid_strategy" with new options
- moved protections to strategy file (protections in config are deprecated)

**07/05/2021**
- added "amend_last_stake_amount": true,
- updated ip detection method to use wan ip

**02/05/2021**
- stoploss is now at -40% as per the backtesting results
![backtest_results](https://user-images.githubusercontent.com/528302/116808569-29a80300-ab42-11eb-9ffb-fb6c710ccf82.jpeg)


**01/05/2021**
- Changed keyboard configuration to the most frequently used commands

**30/04/2021**
- Added explanations to the configuration
- Added VolatilityFilter

**28/04/2021**
- Modified Protections settings to accommodate new strategy
- Protections now use minutes not candles
- Added Considerations section in README.md

**27/04/2021**
- Changed default "initial_state" to "running"
- Modified "setup complete" message
- Added BNB to blacklist to avoid "insufficient balance for requested action" on sell order
- Additional Telegram buttons

**26/04/2021**
- Modified "stop_duration_candles" to 1 to accommodate new strategy

**25/04/2021**
- Moved to MACD & SMA strategy

**16/04/2021**
- Separated configuration, strategy and service files
- Created updateFreqtrade, updateConfig and updateStrategy scripts
- Added SUSD to blacklist

**14/04/2021**
- Improved IP detection

**09/04/2021**
- Now configured to use stoploss_on_exchange
- Created freqtrade and freqUI update script

**04/04/2021**
- Removed "minimal_roi" from strategy
- Added "trailing_stop" to strategy

**29/03/2021**
- Added "PAXG" to blacklist
- Added RSI indicator
- Modified ROI
- Modified "AgeFilter" to 5

**26/03/2021**

- Added "AgeFilter"
- Removed "aiohttp_trust_env" option from config.json
- Decreased "rateLimit" to 200
- Increased "number_assets" to 350
- Updated README.md

**23/03/2021**

- Changed "enableRateLimit" to "true"

**18/03/2021**

- Tidy up installer script
- Updated README.md

**17/03/2021**

- Added binance stablecoins and Fiat currencies to blacklist

**02/03/2021**

- Added Leveraged tokens to blacklist
- Prompt for FreqUI port
- Added Protections options in config.json

**01/03/2021**

- Now using VolumePairList method
- Also using multiple filters
- Updated README.md

**01/03/2021**

- Updated coin pairs list
- Updated README.md

**28/02/2021**

- Additional prompts for installation wizard
- Minor changes in config.json
- Added FreqUI installer
- Now automatically gets host IP Address
- Can now set FreqUI user/pass
- Set dry_run to false
- Now setting "jwt_secret_key" automatically
- Echoes FreqUI URL after installation

**27/02/2021**

- Removed deprecated ticker_interval from config.json
- Set minimal_roi to "0":  0.01 only
- Added custom keyboard commands for Telegram

**24/02/2021**

- Created prompts for installation wizard
- Updated README.md

**20/02/2021**

- Merged all scripts into one
- Updated README.md
- Updated coins pair list

**19/02/2021**

- Updated README.md

**19/01/2021**

- Removed comments from strategy
- Updated coins pair list

**18/01/2021**

- Created Freqtrade install script
- Created strategy install script
- Created configuration install script
- Created service install script
- Created README.md
