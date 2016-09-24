import csv
import sqlite3
import time
import datetime
import random


with open('../scripts/goog.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    count = 0
    for row in readCSV:
        print(row)


conn = sqlite3.connect('stock.db')
c = conn.cursor()

def create_table():
    pass


def data_entry():
    pass


def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]
    # c.execute('DELETE FROM stuffToPlot WHERE unix = 1')
    # conn.commit()
    time.sleep(3)
    c.execute("UPDATE stuffToPlot SET keyword = 'JAVA' WHERE value = 3")
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]


def read_from_db():
    pass



del_and_update()
c.close()
conn.close()
