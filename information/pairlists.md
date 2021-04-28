## VolumePairList
- search for 250 pairs
- refresh every 30 minutes
```
{
    "method": "VolumePairList",
    "number_assets": 250,
    "sort_key": "quoteVolume",
    "refresh_period": 1800
},
```
---
## AgeFilter
- pair must be listed for at least 5 days
```
{"method": "AgeFilter", "min_days_listed": 5},
```
---
## PrecisionFilter
- Filter out low value coins which don't allow setting stoploss.
```
{"method": "PrecisionFilter"},
```
## PriceFilter
- remove pair if the price unit (pip) raises above 1
- and if the pair minimum price is below 0.00001%
```
{"method": "PriceFilter", "low_price_ratio": 0.01, "min_price": 0.00000010},
```
