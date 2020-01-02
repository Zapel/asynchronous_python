import csv

def create_cvs_list(path, filename, fieldnames, list):
    FILENAME = path + filename

    with open(FILENAME, "w") as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
        writer.writerows(list)




if __name__ == '__main__':
    path = '/home/oleg/git/asynchronous_python/cvs/files/'
    filename_list = 'users_dic_new_list.csv'

    list = ({1: "Олег", 2: ''},
            {1: "Женя", 2: ''})

    fieldnames = list[0].keys()

    create_cvs_list(path, filename_list, fieldnames, list)
