# freqtrade

Install [freqtrade](https://github.com/freqtrade/freqtrade) cryptotrading bot. This script was tested on Debian 10.

---

**Disclaimer:** This software can, and probably will, lose your money. Investigate, find a strategy you're comfortable with, and use it with this bot. You are responsible for your decisions and your money. There are no warranties.

---

**Purpose:** The purpose of this script is to provide an automated installation process, a working configuration and strategy, and to simply make it easier to install, configure and update [freqtrade](https://github.com/freqtrade/freqtrade).

---

**Considerations:** The provided configuration and strategy are [Binance](https://www.binance.com/) specific and probably won't work with other exchanges without a few modifications.

---

Before continuing make sure you already have the following information:

- Exchange key
- Exchange secret
- Telegram bot token
- Telegram chat id.

If you want to set up multiple bots, run the command again and choose a different bot name.

---

## Install Freqtrade
```bash
bash <(wget -qO- https://raw.githubusercontent.com/aristosv/freqtrade/main/install)
```
---
## Required setup information
- **Bot Name:** This defines the bot's directory, service and strategy names.
- **Stake Currency:** The coin you want to use to trade on. Examples: USDT, BTC.
- **Display Currency:** The currency in which amounts will be displayed. Examples: USD, EUR, GBP.
- **Stake Amount:** The amount you want to invest per trade.
- **Max Open Trades:** The maximum allowed number of trades. -1 opens as many as possible.
- **Exchange Name:** The name of your Exchange. Example: binance.
- **Exchange Key:** Generate an API key on your exchange and use it here.
- **Exchange Secret:** Along with the API key you will also get a secret.
- **Telegram Token:** In Telegram, talk to [@botfather](https://t.me/BotFather), create a new bot and get it's API token.
- **Telegram ChatID:** In Telegram, talk to [@myidbot](https://t.me/myidbot) and get your ID.
- **Web UI user:** The username to login on the web interface of the bot.
- **Web UI pass:** The password to login on the web interface of the bot.
- **Web UI Port:** The port to use for the web interface.

## Common Usage
- **Start the bot:** systemctl start $botname.service
- **Stop the bot:** systemctl stop $botname.service
- **Restart the bot:** systemctl restart $botname.service
- **Update Freqtrade and FreqUI:** /usr/local/$botname/updateFreqtrade
- **Update the configuration from this repo:** /usr/local/$botname/updateConfig
- **Update the strategy from this repo:** /usr/local/$botname/updateStrategy
- **Tail log file:** tail -f /var/log/$botname.log
