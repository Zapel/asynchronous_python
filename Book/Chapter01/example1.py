from math import sqrt
from timeit import default_timer as timer
import concurrent.futures

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    limit = int(sqrt(x)) + 1
    # print(limit)
    for i in range(3, limit, 2):
        # print(i)
        if x % i == 0:
            return False
    return True

input = [i for i in range(10 ** 13, 10 ** 13 + 500)]

# sequential
start = timer()
result = []

for i in input:
    if is_prime(i):
        result.append(i)
print('Result 1:', result)
print('Took: %.2f seconds.' % (timer() - start))

# concurrent
start = timer()
result = []

with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(is_prime, i) for i in input]

    for i, future in enumerate(concurrent.futures.as_completed(futures)):
        if future.result():
            result.append(input[i])

print('Result 2:', result)
print('Took: %.2f seconds.' % (timer() - start))

if __name__ == '__main__':
    info = is_prime(73)
    print(info)