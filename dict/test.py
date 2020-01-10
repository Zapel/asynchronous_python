from decimal import Decimal
import datetime
import csv

list = [{'fee': Decimal('0.00'), 'order_id': u'tsetvTMCzSIAtJ', 'ret_ref_num': None, 'terminal_id': 3, 'timeend': datetime.datetime(2020, 1, 8, 19, 40, 30, 783155),
        'amount': Decimal('6359.20'), 'approval_code': u'478450', 'actual_amount': Decimal('5087.36'), 'merchant_id': 903004, 'id': 1006553875},
        {'fee': Decimal('0.00'), 'order_id': u'tsetvTMCzSIAtJ', 'ret_ref_num': None, 'terminal_id': 3, 'timeend': datetime.datetime(2020, 1, 8, 19, 40, 30, 127854),
         'amount': Decimal('6359.20'), 'approval_code': u'478450', 'actual_amount': Decimal('6359.20'), 'merchant_id': 903004, 'id': 1006553874},
        {'fee': Decimal('0.00'), 'order_id': u'tsetYBKSnBslyL', 'ret_ref_num': u'111111111111', 'terminal_id': 900291, 'timeend': datetime.datetime(2020, 1, 8, 19, 40, 31, 328386),
         'amount': Decimal('39.24'), 'approval_code': u'123456', 'actual_amount': Decimal('31.39'), 'merchant_id': 903006, 'id': 1006553876},
        {'fee': Decimal('0.00'), 'order_id': u'tsetYBKSnBslyL', 'ret_ref_num': u'111111111111', 'terminal_id': 900291, 'timeend': datetime.datetime(2020, 1, 8, 19, 40, 28, 888713),
         'amount': Decimal('39.24'), 'approval_code': u'123456', 'actual_amount': Decimal('39.24'), 'merchant_id': 903006, 'id': 1006553873}]

def create_cvs_list(path, filename, list):
    FILENAME = path + filename

    list_uot = []
    for i in range(len(list)):
        disct_out = {list[i].pop('merchant_id'): list[i]}
        print(disct_out)
        list_uot.append(disct_out)
    print(list_uot)

    with open(FILENAME, "w") as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=list[0].values().keys())
        writer.writerows(list)



if __name__ == '__main__':
    path = '/home/oleg/git/asynchronous_python/cvs/files/'
    filename = 'users_dic_new_list.csv'

    create_cvs_list(path, filename, list)
