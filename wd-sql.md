<!-- Top Navigation -->
* [Psychology](/psycholgy.md)
* [Game Theory](/game_theory.md)
* [Web Development](/web-dev.md)
    * [Python](/wd-python.md)
    * [CSS](/wd-css-notes.md)
    * *SQL*
* [Web Dev](/web-dev.md)

# SQL

wildcards

% series of characters
_ single character

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
