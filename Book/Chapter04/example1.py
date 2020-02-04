n_files = 10
files = []

for i in range(n_files):
    files.append(open('output/sample%i.txt' % i, 'w'))

for i in range(n_files):
    f = open('output/sample%i.txt' % i, 'w')
    files.append(f)
    f.close()

for i in range(n_files):
    with open('output/sample%i.txt' % i, 'w') as f:
        files.append(f)


