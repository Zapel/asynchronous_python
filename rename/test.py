import os

def rename_file(path, old_name, new_nme):
    old_file = os.path.join(path, old_name)
    new_file = os.path.join(path, new_nme)
    os.rename(old_file, new_file)


if __name__ == '__main__':
    path = '/home/oleg/git/asynchronous_python/cvs/files/'
    old_name = 'FDY test 20190927 .csv'
    new_name = 'FDY test 20190927 .csv'

    rename_file(path, old_name, new_name)