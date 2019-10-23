import csv

def create_cvs(path, filename, fieldnames, *args):
    FILENAME = path + filename

    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for i in args:
            writer.writerow(i)

def create_cvs_list(path, filename, fieldnames, list):
    FILENAME = path + filename

    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)




if __name__ == '__main__':
    path = '/home/oleg/git/asynchronous_python/cvs/files/'
    # filename = 'users_dic_new.csv'
    filename_list = 'users_dic_new_list.csv'
    # user1 = {"name": "Sam", "age": 41, "country": "UA", "city": "Kiev"}
    # user2 = {"name": "Tom", "age": 25, "country": "UA", "city": "Kiev"}
    list =[{'name': 'Tom', 'age': 28, 'country': 'UA', 'city': 'Kiev'}, {'name': 'Alice', 'age': 23, 'country': 'UA', 'city': 'Kiev'}]
    fieldnames = ["name", "age", "country", "city"]

    create_cvs_list(path, filename_list, fieldnames, list)
