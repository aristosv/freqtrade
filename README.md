# freqtrade

Install freqtrade cryptotrading bot on a Debian 10 machine.


The script provides the configuration, strategy and service file.


Before continuing make sure you already have the following information:
- Exchange key
- Exchange secret
- Telegram bot token
- Telegram chat id.

If you want to set up multiple bots, run the script again and set a different bot name.

The command below will run the script and install freqtrade (needs wget).
```
bash <(wget --no-check-certificate -qO- https://raw.githubusercontent.com/aristosv/freqtrade/main/freqtrade)
```

This is the new freqtrade configuration installer, using VolumePairList to automatically detect pairs.
```
bash <(wget --no-check-certificate -qO- https://raw.githubusercontent.com/aristosv/freqtrade/main/freqtrade_new)
```

- Bot Name: This will be the bot's name. When setting up multiple bots each one can have it's name.
- Web UI user/pass: The credentials to login on the web interface of the bot. http://your_ip_address:8080
- Stake Currency: Which coin do you want to use to trade on? It's recommended to use a stablecoin like USDT.
- Stake Amount: The amount you want to invest per trade. Binance requires above 16 USDT.
- Max Open Trades: The maximum allowed number of trades. -1 uses all the available amount on the Exchange.
- Exchange Name: The name of your Exchange. For example: binance.
- Exchange Key: Generate an API key on your exchange and use it here.
- Exchange Secret: Along with the key you will also get a secret.
- Telegram Token: Install Telegram, talk to @botfather, create a new bot and get it's token.
- Telegram ChatID: Talk to @myidbot and get your ID.
