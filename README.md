# freqtrade

Install [freqtrade](https://github.com/freqtrade/freqtrade) cryptotrading bot on a Debian 10 machine.

---

**Disclaimer:** This software can, and probably will, lose your money. Investigate, find a strategy you're comfortable with, and use it with this bot. You are responsible for your decisions and your money. The script provides a configuration, strategy and service file. Look at them, understand them, modify them. Good luck.

---

Before continuing make sure you already have the following information:
- Exchange key
- Exchange secret
- Telegram bot token
- Telegram chat id.

If you want to set up multiple bots, run the command again and set a different bot name.

---

This command will install freqtrade.
```
bash <(wget --no-check-certificate -qO- https://raw.githubusercontent.com/aristosv/freqtrade/main/freqtrade)
```

---

This is the information you will be required to provide when installing Freqtrade.


- **Bot Name:** This will be the bot's name. When setting up multiple bots each one can have it's own name.
- **Web UI user:** The username to login on the web interface of the bot.
- **Web UI pass:** The password to login on the web interface of the bot.
- **Web UI Port:** The port to use for the web interface.
- **Stake Currency:** The coin you want to use to trade on. It's recommended to use a stablecoin like USDT.
- **Stake Amount:** The amount you want to invest per trade. Binance requires above 16 USDT.
- **Max Open Trades:** The maximum allowed number of trades.
- **Exchange Name:** The name of your Exchange. For example: binance.
- **Exchange Key:** Generate an API key on your exchange and use it here.
- **Exchange Secret:** Along with the API key you will also get a secret.
- **Telegram Token:** In Telegram, talk to [@botfather](https://t.me/BotFather), create a new bot and get it's API token.
- **Telegram ChatID:** In Telegram, talk to [@myidbot](https://t.me/myidbot) and get your ID.
