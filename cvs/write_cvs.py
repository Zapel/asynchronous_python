import csv

FILENAME = "/home/oleg/git/asynchronous_python/cvs/files/users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])
