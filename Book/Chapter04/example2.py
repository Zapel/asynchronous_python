from threading import Lock

my_lock = Lock()

def get_data_from_file_v1(filename):
    my_lock.acquire()
    with open(filename, 'r') as f:
        data.append(f.read())
    my_lock.release()

data = []

try:
    get_data_from_file_v1('output2/sample0.txt')
except FileNotFoundError:
    print('Encountered an exception...')

my_lock.acquire()
print('Lock can still be acquired.')
