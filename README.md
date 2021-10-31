# Bundesbank to sqlite

[![Tests](https://github.com/mfa/bundesbank-to-sqlite/actions/workflows/tests.yml/badge.svg)](https://github.com/mfa/bundesbank-to-sqlite/actions/workflows/tests.yml)

## About

The German Bundesbank releases every quarter of a year a list of all banks in Germany.  
This script converts the xslx file to a sqlite database.


## Download source data

https://www.bundesbank.de/en/tasks/payment-systems/services/bank-sort-codes/download-bank-sort-codes-626218

choose the XLS version of ``Bank sort code files, unpacked``


## install

```
python setup.py install
```


## Convert downloaded file

```
bundesbank-to-sqlite convert blz.db blz-aktuell-xlsx-data.xlsx
```


## Use with [Datasette](https://github.com/simonw/datasette)

install Datasette:

```
pip install datasette
```

run with Datasette:

```
datasette blz.db
```

## Example queries

Run some queries in [Datasette](https://datasette.io).

```
http://localhost:8001/blz/bundesbank_blz?blz=10000000
http://localhost:8001/blz/bundesbank_blz?bic=MARKDEF1100
http://localhost:8001/blz/bundesbank_blz?city=Berlin
http://localhost:8001/blz/bundesbank_blz?zipcode=10117
```

(this are the same examples as in deprecated [banking_api](https://github.com/opendata-stuttgart/banking-api#example-api-usage))


## Thanks

[Simon Willison](https://simonwillison.net/) for Datasette and sqlite-utils.
