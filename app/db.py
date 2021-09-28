import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = None

db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_password = os.environ.get('DB_PASSWORD')
db_user = os.environ.get('DB_USER')


def create_database():
    db_conn = None
    try:
        db_conn = psycopg2.connect(
            host=db_host,
            port="5432",
            user=db_user,
            password=db_password
        )
        db_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = db_conn.cursor()

        print('Creating database:')
        cur.execute("DROP DATABASE IF EXISTS puns;")
        cur.execute("CREATE DATABASE puns;")

        # cur.execute('CREATE TABLE IF NOT EXISTS puns (pun text);')
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise

    finally:
        if db_conn is not None:
            print('closing db connection')
            db_conn.close()


def create_table():
    db_conn = None
    try:
        db_conn = psycopg2.connect(
            host=db_host,
            port="5432",
            database=db_name,
            user=db_user,
            password=db_password
        )

        cur = db_conn.cursor()

        print('Creating database table:')

        cur.execute('CREATE TABLE IF NOT EXISTS puns (pun text);')
        db_conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise

    finally:
        if db_conn is not None:
            print('closing db connection')
            db_conn.close()


def connect():
    try:
        db_conn = psycopg2.connect(
            host=db_host,
            port="5432",
            database=db_name,
            user=db_user,
            password=db_password
        )

        global conn
        conn = db_conn

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise


def add_pun(pun):
    try:
        cur = conn.cursor()

        print('adding pun', pun)
        cur.execute("INSERT INTO puns (pun) VALUES (%s);", (pun,))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print('error adding pun:')
        print(error)
        raise


def get_random_pun():
    try:
        cur = conn.cursor()

        print('getting a random pun')
        cur.execute("SELECT pun FROM puns ORDER BY random() LIMIT 1;")

        row = cur.fetchone()

        return row

    except (Exception, psycopg2.DatabaseError) as error:
        print('error getting a random pun:')
        print(error)
        raise
