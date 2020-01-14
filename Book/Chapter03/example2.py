from math import sqrt
import _thread as thread

my_input = [2, 193, 311, 1327, 433785907]

def is_prime(x):
    if x < 2:
        print('%i is not a prime number.' % x)

    elif x == 2:
        print('%i is a prime number.' % x)

    elif x % 2 == 0:
        print('%i is not a prime number.' % x)

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print('%i is not a prime number.' % x)
        print('%i is a prime number.' % x)

for x in my_input:
    thread.start_new_thread(is_prime, (x, ))

a = input('Type something to quit: \n')

