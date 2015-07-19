# MagicRanker API

Work in progress; nothing to see here.

## Setup

* Create Postgres database and user

```
> createuser magicranker
> createdb magicranker
```

* Clone repo

```
git clone git@github.com:lextoumbourou/magicranker-api.git
```

* Create [virtualenv](http://virtualenv.readthedocs.org/en/latest/) and activate it.

```
cd magicranker-api && virtualenv ENV && source ENV/bin/activate
```

* Install Python requirements.

```
pip install -r requirements.txt
```

## Endpoints

## /rank

```
> curl api.magicranker.com/rank -d '
[
    {"field": "roe", "averaged_years": 2, "min": 25, "rank": True},
    {"field": "pe", "averaged_years": 2, "min": 25, "rank": True},
    {"field": "market_cap", "averaged_years": 2, "max": 100000000},
    {"field": "debt_percent", "max": 30},
]'
```
