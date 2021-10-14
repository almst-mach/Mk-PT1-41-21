import csv

with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(['cat', 'dog', 'bat'])
    # writer.writerow(['camel', 'girafe', 'tiger'])
    writer.writerows([['cat', 'dog', 'bat'], ['camel', 'girafe', 'tiger']])

with open("test.csv", "r", newline='') as f:
    reader = csv.reader(f)
    column = []
    for row in reader:
        column.append(row[0])
    print(column)

