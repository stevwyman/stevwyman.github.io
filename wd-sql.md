<!-- Top Navigation -->
* [Psychology](/psycholgy.md)
* [Game Theory](/game_theory.md)
* [Web Development](/web-dev.md)
    * [Python](/wd-python.md)
    * [CSS](/wd-css-notes.md)
    * *SQL*

# SQL

[sqlite3](https://sqlite.org/lang_keywords.html)

wildcards

% series of characters
_ single character

## format output

```sql
.mode column
.mode table
.headers on
.separator ROW "\n"
.nullvalue NULL
```

### usefully

ctrl l  cleat terminal

= is case sensitive, LIKE is not
.schema to describe the database
pragma table_info('longlist');

asc from smallest to greatest (default)
desc from greatest to smallest

length(data) vs MAX/MIN

[scaler functions](/https://www.sqlite.org/lang_corefunc.html)

## joins

inner join is default, showing only entries where ids match

outer joins:
    left is the first and the one after join is the right

    left outer join
    -> keeps the left where is not NULL

    right outer join
    -> keeps the right where is not NULL

    full join
    -> keep all NULL values

    natural join
    -> no duplicate id columns and no NULL




## Create flights table
```sql
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
```

## Inserts

```sql
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);
INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokyo", 700);
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "Paris", 435);
INSERT INTO flights (origin, destination, duration) VALUES ("Moscow", "Paris", 245);
INSERT INTO flights (origin, destination, duration) VALUES ("Lima", "New York", 455);
```

## Selects

```sql
SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = "New York";
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";
SELECT * FROM flights WHERE duration > 500 OR destination = "Paris";
SELECT * FROM flights WHERE origin IN ("New York", "Lima");
SELECT * FROM flights WHERE origin LIKE "%a%";
```

## Update

```sql
UPDATE flights SET duration = 430 WHERE origin = "New York" AND destination = "London";
```

## Delete

```sql
DELETE FROM flights WHERE destination = "Tokyo";
```

## Join

```sql
SELECT first, origin, destination FROM flights JOIN passengers ON passengers.flight_id = flights.id;
```

## Index

```sql
CREATE INDEX name_index ON passengers (last);
```