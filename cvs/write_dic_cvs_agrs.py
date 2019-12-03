import csv

def create_cvs(path, filename, *args):
    FILENAME = path + filename
    user = {"name": "Sam", "age": 41, "country": "UA", "city": "Kiev"}
    columns = ["name", "age", "country", "city"]
    inner_list = []

    for i in args:
        inner_dict = {}
        user["name"] = i["key1"]
        user["age"] = i["key2"]
        inner_dict.update(user)
        inner_list.append(inner_dict)
    print('inner_list: ', inner_list)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
        writer.writeheader()
        # writer.writerow(user)
        writer.writerows(inner_list)

    # with open(FILENAME, "r", newline="") as file:
    #     reader = csv.DictReader(file)
    #     headers = reader.fieldnames
    #     for row in reader:
    #         print(row)
    #     for header in headers:
    #         print(header)

def read_csv_file(path, * args):
    for arg in args:
            dir_file = path + arg
            print(dir_file)
            with open(dir_file, "r") as file:
                reader = csv.DictReader(file, delimiter=';')
                headers = reader.fieldnames
                print(headers)
                dict_out = {}
                i = 0
                # for str in reader:
                #     print(type(str)
                # #     dict_out.update({i: str})
                # #     i += 1
                for i in dict_out.keys():
                    print(i)
                    print(dict_out)
                return dict_out






if __name__ == '__main__':
    path = '/home/oleg/git/asynchronous_python/cvs/files/'
    filename = 'FDY test 20190927 .csv'
    # dic1 = {"key1": "Tom", "key2": 28}
    # dic2 = {"key1": "Alice", "key2": 23}
    #
    # create_cvs(path, filename, dic1, dic2)
    read_csv_file(path, filename)


