import sqlite3
import csv

COLUMN_CATALOG_CATEGORY = 5
COLUMN_CATALOG_ID = 0

COLUMN_SALE_ID = 0
COLUMN_SALE_COUNTRY = 1
COLUMN_SALE_CITY = 2
COLUMN_SALE_DATE = 3
COLUMN_SALE_PRICE = 4  # last one

def create_tables(connection: sqlite3.Connection):
    cursor_ct = connection.cursor()

    cursor_ct.execute("""CREATE TABLE IF NOT EXISTS sale
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_key varchar(200) NOT NULL,
    country varchar(3),
    city_name varchar(60),
    sale_timestamp TEXT,
    price NUMERIC
    );
    """)

    cursor_ct.execute("""
    CREATE TABLE IF NOT EXISTS catalog (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_key varchar(200),
        category varchar(200)
    );
""")


def import_catalog_into_db(connection: sqlite3.Connection):
    cursor = connection.cursor()
    with open("./catalog.csv") as _:
        catalog_reader = csv.reader(_)
        for line in catalog_reader:
            id = line[COLUMN_CATALOG_ID]
            category = line[COLUMN_CATALOG_CATEGORY]

            cursor.execute("INSERT INTO catalog (item_key, category) VALUES (?,?);",
                           [id, category])


def import_sales_into_db(connection: sqlite3.Connection):
    cursor = connection.cursor()

    with open("./sales-10K.csv") as _:
        sales_reader = csv.reader(_)

        for line in sales_reader:
            item_key = line[COLUMN_SALE_ID]
            country = line[COLUMN_SALE_COUNTRY]
            city = line[COLUMN_SALE_CITY]
            timestamp = line[COLUMN_SALE_DATE]
            price = float(line[COLUMN_SALE_PRICE])

            cursor.execute("INSERT INTO sale (item_key, country, city_name, sale_timestamp, price) VALUES (?, ?, ?, ?, ?);",
                           [item_key, country, city, timestamp, price])


with sqlite3.connect('./database', isolation_level=None) as db:
    cursor = db.cursor()
    create_tables(db)
    import_catalog_into_db(db)
    print("importing sales")
    import_sales_into_db(db)