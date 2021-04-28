## StoplossGuard
- in the last 24 hours
- if 5 trades hit stoploss
- stop trading for 60 minutes
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
## MaxDrawdown
- in the last 24 hours
- considering only pairs that made at least 10 trades
- if drawdown is more than 30%
- stop trading for 60 minutes
```
{
    "method": "MaxDrawdown",
    "lookback_period": 1440,
    "trade_limit": 10,
    "max_allowed_drawdown": 0.3
    "stop_duration": 60,
},
```
---
## LowProfitPairs
- in the last 24 hours
- considering only pairs that made at least 2 trades
- with less than 2% profit
- stop trading on those pairs for 60 minutes
```
{
    "method": "LowProfitPairs",
    "lookback_period": 1440,
    "trade_limit": 2,
    "required_profit": 0.02
    "stop_duration": 60,
},
```
---
## CooldownPeriod
- after a trade closes, wait 5 minutes before buying the same pair again
```
{
    "method": "CooldownPeriod",
    "stop_duration": 5
},
```
