import csv
with open('emp.csv',newline='') as csvfile:
    data=csv.reader(csvfile,delimiter=' ',quotechar='l')
    for row in data:
        print(','.join(row))
