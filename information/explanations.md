

{
    "method": "StoplossGuard",
    "lookback_period_candles": 24,
    "trade_limit": 4,
    "stop_duration_candles": 4,
    "only_per_pair": false
}
---
```
- if in the last 24 hours
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
---
- if in the last 24 hours
- considering only pairs that made at least 2 trades
- with at least a 2% profit
- stop trading on that pair for 60 minutes
```
{
    "method": "LowProfitPairs",
    "lookback_period": 1440,
    "trade_limit": 2,
    "required_profit": 0.02
    "stop_duration": 60,
}
```
---
