import psycopg2

conn = None


def connect():
    try:
        db_conn = psycopg2.connect(
            host="localhost",
            database="puns",
            user="postgres",
            password="postgres"
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
