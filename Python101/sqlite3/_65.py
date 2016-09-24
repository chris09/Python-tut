import sqlite3
import datetime
import time
import random


conn = sqlite3.connect('stock.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL )')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1, '2616-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)", (unix, date, keyword, value))
    conn.commit()


def read_from_db():
    # c.execute("SELECT unix, datestamp, keyword, value FROM stuffToPlot")
    c.execute("SELECT * FROM stuffToPlot")
    for row in c.fetchall():
        print(row)


# create_table()
# data_entry()
for i in range(10):
    dynamic_data_entry()
read_from_db()

c.close()
conn.close()
