import os
from psycopg2 import connect, Error, extras

environment = os.getenv('APP_SETTINGS')
if environment == 'testing':
    connect = connect(os.getenv('DATABASE_TEST_URL'))
    cur = connect.cursor()
    # print('connect to test database')

if environment == 'development':
    connect = connect(os.getenv('DATABASE_URL'))
    connect.autocommit = False
    cur = connect.cursor(cursor_factory=extras.RealDictCursor)
    #print('connected to development database')

if environment == 'production':
    connect = connect(os.getenv('DATABASE_URL'))
    connect.autocommit = False
    cur = connect.cursor(cursor_factory=extras.RealDictCursor)
    # print('connected to production database')


def create_tables():
    try:
        # delete tables if they exist
        cur.execute("DROP TABLE IF EXISTS products,sales,users;")
        cur.execute("DROP TABLE IF EXISTS tokens;")

        # create table users
        users = "CREATE TABLE users (id serial PRIMARY KEY NOT NULL ,username VARCHAR(64) UNIQUE NOT NULL," \
                " email VARCHAR(64) UNIQUE NOT NULL,password VARCHAR(256) NOT NULL, role int default 0);"

        # admin data
        create_admin = """INSERT INTO users (username, email, password, role)
                 VALUES ('admin','owezzygold@gmail.com',
                 '$pbkdf2-sha256$29000$qBUihNAaozTmXIvRGuN8bw$oMzLAzVT7gATROl7KkzvemH6cAx6Jx/0TLOjQdDXlz8',1)"""

        # create table tokens
        tokens = "CREATE TABLE tokens(id VARCHAR(256) PRIMARY KEY, expired_tokens VARCHAR(256));"

        categories = """create table if not exists categories(id serial PRIMARY KEY, name varchar,
        owner int, date_of_creation timestamp default now());"""

        products = """create table if not exists products(id serial PRIMARY KEY, product_name varchar,
         price int, stock int, minimum_stock int,owner int, date_of_creation timestamp default now());
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
        connect.commit()
    except (Exception, Error) as er:
        print('Error creating table', er)


def delete_table():
    cur.execute("DELETE from users ;")
    cur.execute("DELETE from products;")
    cur.execute("DELETE from sales;")
    cur.execute("DELETE from categories;")
    cur.execute("DELETE from tokens;")
