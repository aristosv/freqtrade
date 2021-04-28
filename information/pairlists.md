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
Filters out low value coins which don't allow setting stoplosses.
```
{"method": "PrecisionFilter"},
```
