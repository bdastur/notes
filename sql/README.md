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

[sqlite index](https://www.sqlitetutorial.net/sqlite-index/)


## Running mysql on MAC:

Simplest way is to run it as a docker container

```
docker pull mysql
```

```
docker run --name sqlserver -e MYSQL_ROOT_PASSWORD=<password> -d mysql:latest
```

You can exec into the container to access the server.
```
/# mysql -u root -p
Enter password:
:
mysql> exit
Bye
root@d31f7768e6a5:/#

```



