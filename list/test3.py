def create_prom_xls(orders_data):
    sort = sorted(orders_data, key=lambda x: x['number'])
    print(sort)
    info = ['sum', 'sum1', 'sum3']
    inner = []

    for data in info:
        d = {}
        for i in orders_data:
            if i['number'] not in d:
                d[i['number']] = [i[data]]
            else:
                d[i['number']].append(i[data])

        for i in range(len(d)):
            b = d.popitem()
            # dicts = {'number': list(b)[0], 'len': len(list(b)[1]), data: sum(list(b)[1])}
            dicts = {'number': list(b)[0], 'len': len(list(b)[1])}
            inner.append(dicts)
    # print(inner)

    data = [{'number': 1, 'sum': 10, 'sum1': 1, 'sum3': 1},
            {'number': 2, 'sum': 5, 'sum1': 12, 'sum3': 1},
            {'number': 1, 'sum': 10, 'sum1': 3, 'sum3': 1},
            {'number': 2, 'sum': 5, 'sum1': 8, 'sum3': 1},
            {'number': 2, 'sum': 10, 'sum1': 14, 'sum3': 1},
            {'number': 2, 'sum': 4, 'sum1': 10, 'sum3': 1}]


    super_dict = {}

    for d in inner:
        for k, v in d.items():
            if super_dict.get(k) is None:
                super_dict[k] = []
                if v not in super_dict.get(k):
                    super_dict[k].append(v)

    print(super_dict)










if __name__ == '__main__':
    data = [{'number': 1, 'sum': 10, 'sum1': 1, 'sum3': 1},
            {'number': 2, 'sum': 5, 'sum1': 12, 'sum3': 1},
            {'number': 1, 'sum': 10, 'sum1': 3, 'sum3': 1},
            {'number': 2, 'sum': 5, 'sum1': 8, 'sum3': 1},
            {'number': 2, 'sum': 10, 'sum1': 14, 'sum3': 1},
            {'number': 2, 'sum': 4, 'sum1': 10, 'sum3': 1}]

    create_prom_xls(data)