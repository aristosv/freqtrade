# freqtrade

Install freqtrade cryptotrading bot on a Debian 10 machine.


The script provides the configuration, strategy and service file.


Before continuing make sure you already have the following information:
- Exchange key
- Exchange secret
- Telegram bot token
- Telegram chat id.

If you want to set up multiple bots, run the script again and set a different bot name.

The command below will run the script and install freqtrade
```
bash <(wget --no-check-certificate -qO- https://raw.githubusercontent.com/aristosv/freqtrade/main/freqtrade)
```
