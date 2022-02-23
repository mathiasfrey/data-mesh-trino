# data-mesh-trino

Is it possible to query relational and streaming data combined with SQL?

Yes, with a distributed query engine like Trino!

![](docs/trino-sql.png)

## start the services

```
docker-compose up -d
```

Open up http://localhost:8080/ (any username)

```
docker container exec -it $(docker ps | grep trino-coordinator | cut -d' ' -f1) trino
show catalogs;
show schemas in kafka;
show tables in kafka.market;
select * from kafka.market.prices;
```


## add data to the RDBMS

```
docker exec -i -t -u root $(docker ps | grep mysql | cut -d' ' -f1) /bin/bash  
mysql --user admin --password --database tiny
=> admin
CREATE TABLE stock (id INTEGER PRIMARY KEY, symbol VARCHAR(8), marketplace VARCHAR(100));
INSERT INTO stock VALUES (1, 'AAA', 'New York Stock Exchange');
INSERT INTO stock VALUES (2, 'ZZZ', 'Milano, Italia');
```

## add data top the stream

```
docker-compose up producer
```
_Run this multiple times. Also play with the payload in `producer/app.py`_

## run a distributed query across different data sources!

```
SELECT stock.symbol, stock.marketplace, prices._timestamp, prices.price
  FROM mysql.tiny.stock AS stock,
       kafka.market.prices AS prices
 WHERE stock.symbol = prices.symbol
   AND prices._timestamp IN (
       SELECT MAX(_timestamp) 
         FROM kafka.market.prices
        WHERE symbol = prices.symbol GROUP BY symbol)
```
_this is not an ideal query, In know..._



# Reference
https://github.com/bitsondatadev/trino-getting-started