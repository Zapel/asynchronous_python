import csv

FILENAME = "/home/oleg/git/asynchronous_python/cvs/files/users_dic.csv"

users = []
columns = ["name", "age", "country", "city"]
user = {"name": "Sam", "age": 41, "country": "UA", "city": "Kiev"}
print('users_before: ', users)

dic1 = {"key1": "Tom", "key2": 28}
dic2 = {"key1": "Alice", "key2": 23}

inner_list = []
# print('inner_list_before: ', inner_list)
inner_list.append(dic1)
inner_list.append(dic2)
# print('inner_list_after: ', inner_list)

for i in inner_list:
    x = {}
    user["name"] = i["key1"]
    user["age"] = i["key2"]
    x.update(user)
    users.append(x)
print('users_after: ', users)

with open(FILENAME, "w", newline="") as file:

    writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
    writer.writeheader()
    # writer.writerow(user)
    writer.writerows(users)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row.values())

