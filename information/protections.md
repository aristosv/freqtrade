## StoplossGuard
- in the last 24 hours
- if 5 trades hit stoploss
- stop trading for 60 minutes (global lock)
```
{
    "method": "StoplossGuard",
    "lookback_period": 1440,
    "trade_limit": 5,
    "stop_duration": 60,
    "only_per_pair": false
},
```
---
## CooldownPeriod
- after a trade closes
- wait 5 minutes before buying the same pair again (pair lock)
```
{
    "method": "CooldownPeriod",
    "stop_duration": 5
},
```
---
## MaxDrawdown
- in the last 48 hours
- considering only pairs that made at least 20 trades
- if drawdown is more than 20%
- stop trading for 4 hours (global lock)
```
{
    "method": "MaxDrawdown",
    "lookback_period": 2880,
    "trade_limit": 20,
    "max_allowed_drawdown": 0.2
    "stop_duration": 240,
},
```
---
## LowProfitPairs
- in the last 4 hours
- considering only pairs that made at least 2 trades
- with less than 2% profit
- stop trading on those pairs for 60 minutes (remove from whitelist)
```
{
    "method": "LowProfitPairs",
    "lookback_period": 360,
    "trade_limit": 2,
    "required_profit": 0.02
    "stop_duration": 60,
},
```
