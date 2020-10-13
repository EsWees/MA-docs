#!/usr/bin/env python3

import sqlite3 as sql


def sqlite(query, file=":memory:") -> object:
    """
    This is AllInOne sqlite db function. Simplest stuff
    :param query: sql query for the db
    :param file: file path
    :return: connection object
    """
    conn = None
    try:
        conn = sql.connect(file)
        conn.execute(query)
        conn.commit()
    except sql.Error as error:
        print(f"connection error: {error.__class__.__name__}")

    return conn


def main():
    # Open the connection
    connection = sqlite('select sqlite_version()')
    print(f"{connection=}")
    with connection:
        c = connection.cursor()

        # If a file present as a db.
        c.execute('drop table IF EXISTS cars')

        c.execute('create table IF NOT EXISTS cars (id INTEGER PRIMARY KEY UNIQUE, name TEXT NOT NULL, price DOUBLE)')
        c.execute('insert into cars(name, price) values("Audi", 555)')
        c.execute('insert into cars(name, price) values("BMW", 555)')

        for i in range(1,10000):
            sql = f"insert into cars(name, price) values('BMW{i}', {i*10.2})"
            c.execute(sql)

        c.execute('select * from cars')

        # Testing fetchone() iterator
        res = c.fetchone()
        print(f"{res=}")

        res = c.fetchone()
        print(f"{res=}")

        # try to get all items but with limited select query
        c.execute('select * from cars where price >= 9999 limit 1')
        res = c.fetchall() # Here is fetchall() function. Type: list
        print(f"{res=}") # res=[(983, 'BMW981', 10006.199999999999)] <- list

        c.close()
    connection.close()


if __name__ == "__main__":
    main()