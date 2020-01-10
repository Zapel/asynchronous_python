
def get_info_data(data, num):
    keys = list(data[0].keys())
    y = (len(data[0].keys()))
    reverse = data[0]


    for i in range(y):

        if keys[i] != 'merchant_id':
            # print(keys[i])
            data[0].pop(keys[i])
            # print(reverse)
            y -= 1
            # print(y)
            if y == 2 + num:
                return reverse
            else:
                continue




if __name__ == '__main__':
    num = 1
    data = [{'merchant_id': u'903015', u'tsetBUBYKtAKMm': 464.47, u'tsetBUBYKtAKMt': 464.47, u'tsetwfqxZmgshW': 3711.4, u'tsetBUBYKtAKMz': 464.47},
            {'merchant_id': u'903016', u'tsetwfqxZmgshW': 3711.4, u'tsetBUBYKtAKMz': 464.47},
            {'merchant_id': u'903017', u'tsetBUBYKtAKMk': 464.47, u'tsetBUBYKtAKMy': 464.47}]


    reverse = get_info_data(data, num)
    print(reverse)
