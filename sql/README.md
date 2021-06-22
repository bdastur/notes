# SQL Notes.

* [Good sql notes](https://github.com/vasudeveloper001/completesql/blob/main/sql_notes.md)

## SQLITE3.

### Show tables.

```
SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';
```

or

```
.tables
```

### Drop table.

```
DROP table products
```


### Indexing

[sqlite indeex](https://www.sqlitetutorial.net/sqlite-index/)
