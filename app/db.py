import os
from psycopg2 import connect, Error, extras

environment = os.getenv('APP_SETTINGS')
if environment == 'testing':
    connection = connect(os.getenv('DATABASE_TEST_URL'))
    cur = connection.cursor()
    # print('connect to test database')

elif environment == 'production':
    connection = connect(os.getenv('DATABASE_URL'))
    connect.autocommit = False
    cur = connection.cursor(cursor_factory=extras.RealDictCursor)

elif environment == 'development':
    connection = connect(os.getenv('DATABASE_URL'))
    connect.autocommit = False
    cur = connection.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("Connected to -", record, "\n")


    def create_tables():
        try:
            cur.execute("DROP TABLE IF EXISTS products,sales,users;")
            cur.execute("DROP TABLE IF EXISTS tokens;")

            # create table user
            users = "CREATE TABLE users (id serial PRIMARY KEY NOT NULL ,username VARCHAR(64) UNIQUE NOT NULL," \
                    " email VARCHAR(64) UNIQUE NOT NULL,password VARCHAR(256) NOT NULL, role int default 0);"
            # admin data
            create_admin = """INSERT INTO users (username, email, password, role)
            VALUES ('admin','owezzygold@gmail.com',
            '$pbkdf2-sha256$29000$qBUihNAaozTmXIvRGuN8bw$oMzLAzVT7gATROl7KkzvemH6cAx6Jx/0TLOjQdDXlz8',1)"""

            # create table tokens
            tokens = "CREATE TABLE tokens(id VARCHAR(256) PRIMARY KEY, expired_tokens VARCHAR(256));"

            # create tables for store
            categories = """create table if not exists categories(id serial PRIMARY KEY, name varchar,
            added_by int, date_of_creation timestamp default now());"""

            products = """create table if not exists products(id serial PRIMARY KEY, product_name varchar,
             product_category varchar, price int, stock int, minimum_stock int,owner int,
              date_of_creation timestamp default now());
                   """

            sales = """create table if not exists sales(id serial PRIMARY KEY, product_id varchar,
                  price int, stock int, minimum_stock int,owner int, date_of_creation timestamp default now());
                           """

            cur.execute(users)
            cur.execute(tokens)
            cur.execute(create_admin)
            cur.execute(categories)
            cur.execute(products)
            cur.execute(sales)
            connection.commit()
            print("Table created successfully in PostgreSQL ")
        except (Exception, Error) as er:
            print('Error creating table', er)


def delete_table():
    cur.execute("DELETE from users ;")
    cur.execute("DELETE from products;")
    cur.execute("DELETE from sales;")
    cur.execute("DELETE from categories;")
    cur.execute("DELETE from tokens;")
