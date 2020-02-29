list = []

list.append({3: 1})
list.append({3: 0})
list.append({3: 2})

print(list)

list_test = {'key': 123}

if list_test.get('way'):
    print(list_test.get('key'))
else:
    raise Exception('mistake')

