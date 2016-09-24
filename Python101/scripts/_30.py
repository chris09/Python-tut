import csv


with open('star98.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    count = 0
    for row in readCSV:
        print(row)
        count += 1
        if count == 2:
            break
