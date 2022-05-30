from dotenv import load_dotenv

load_dotenv()

import os

import psycopg2


POSTGRESQL_DB_NAME=os.getenv("POSTGRESQL_DB_NAME")
POSTGRESQL_USERNAME=os.getenv("POSTGRESQL_USERNAME")
POSTGRESQL_PASSWORD=os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_HOST=os.getenv("POSTGRESQL_HOST")

def populate_table():
    try:
        conn = psycopg2.connect(user=POSTGRESQL_USERNAME,
                                      password=POSTGRESQL_PASSWORD,
                                      host=POSTGRESQL_HOST,
                                      database=POSTGRESQL_DB_NAME)

        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE items (item_id VARCHAR(255),
                                                duration INT);""")


        cursor.execute("""INSERT INTO items(item_id, duration)
                                VALUES ('a', 10);""")
        cursor.execute("""INSERT INTO items(item_id, duration)
                                VALUES ('b', 20);""")
        cursor.execute("""INSERT INTO items(item_id, duration)
                                VALUES ('c', 30);""")

        cursor.execute("""SELECT * FROM items;""")
        conn.commit()
        rows = cursor.fetchall()
        print("Inserted rows fetched: ", rows)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def get_item(item_id):
    rows = []
    try:
        conn = psycopg2.connect(user=POSTGRESQL_USERNAME,
                                password=POSTGRESQL_PASSWORD,
                                host=POSTGRESQL_HOST,
                                database=POSTGRESQL_DB_NAME)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM items WHERE item_id = '""" + item_id +
                       "';")

        conn.commit()  # <--- makes sure the change is shown in the database
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    return rows[0]


def clear_table():
    try:
        conn = psycopg2.connect(user=POSTGRESQL_USERNAME,
                                password=POSTGRESQL_PASSWORD,
                                host=POSTGRESQL_HOST,
                                database=POSTGRESQL_DB_NAME)

        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()

        cursor.execute("""DROP TABLE items;""")

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

clear_table()
populate_table()
print(get_item("a"))
