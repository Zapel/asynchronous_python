import datetime
import calendar
import time
import base64
import requests

class Ibox():

    def request_well(self, dict):
        list_well = []
        date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        ts = calendar.timegm(time.gmtime())
        authorization = 'Basic {}'.format(base64.b64encode('client#33:zapel_test'.encode("UTF-8")))

        # company_data = data_companies(kwargs.get('company_name'))
        # authorization = 'Basic {}'.format(base64.b64encode('client#{}:{}'.format(company_data.get('id'), company_data.get('private_key')).encode("UTF-8")))

        dict.update({'datetime': date,
                     'transaction_id': ts,
                     'Authorization': authorization,
                     'way': 'well'})

        list_well.append(dict)
        print('list_well', list_well)
        print('*************************************************************************************************************')
        return list_well

    def request_already(self, dict):
        list_already = []

        # data_company = get_merchant_company(kwargs.get('company_name'))
        # merch_id = data_company.get('id')
        # if merch_id:
        #     ts = get_merchant_already(merch_id)
        #     dict.update({'transaction_id': ts,
        #                  'way': 'bad'})
        # else:
        #     raise Exception('NOT DATA FOR TEST!')

        list_already.append(dict)
        return list_already


    def request_empty(self, dict):
        list_empty = []
        list_well = self.request_well(dict)
        dict.update({'way': 'bad'})

        for key, value in list_well[0].items():
            dict_out = {}
            dict_out.update(list_well[0])
            if key != 'Cache-Control' and key != 'Accept' and key != 'way':
                dict_out.update({key: ''})
                list_empty .append(dict_out)

        # for data in list_empty:
        #     print('list_empty', data)
        # print('*************************************************************************************************************')
        return list_empty

    def request_pass(self, dict):
        list_empty = []
        list_well = self.request_well(dict)
        dict.update({'way': 'bad'})

        for key, value in list_well[0].items():
            dict_out = {}
            dict_out.update(list_well[0])
            if key != 'Cache-Control' and key != 'Accept' and key != 'way':
                dict_out.pop(key)
                list_empty.append(dict_out)

        # for data in list_empty:
        #     print('pass', data)
        # print('*************************************************************************************************************')
        return list_empty

    def generate_payment_ibox(self, url, list):
        for i in list:
            payload = {
                       'datetime': i.get('datetime'),
                       'transaction_id': i.get('transaction_id'),
                       'client_id': i.get('client_id'),
                       'amount': i.get('amount')
                      }

            headers = {
                       'Content-Type': i.get('Content-Type'),
                       'Authorization': i.get('Authorization'),
                       'Accept': i.get('Accept'),
                       'Cache-Control': i.get('Cache-Control')
                       }

            # response = requests.post(url, json=payload, headers=headers).json()

            print('payload', payload)
            print('headers', headers)
            print('***********************************************************')

            if i.get('way') == 'well':
                print('well')
                print(url)
                # data_merchant = data_merchantregisters_ibox(response)
                # data_company = get_merchant_company(kwargs.get('company_name'))
                #
                # assert data_company.get('id') == data_merchant.get('merchant_id'), 'MERCHANT_ID!'
                # assert Decimal(data_merchant.get('amount')) == Decimal(kwargs.get('amount')), 'AMOUNT!'
                # assert data_merchant.get('payout_amount') == data_merchant.get('amount') - data_merchant.get('fee_ps'), 'PAYOUT_AMOUNT!'
            else:
                print('bad')
                print(url)
                # assert response.get('error_message'), '{}'.format(i)
                # if response.get('error_message'):
                #     print(response.get('error_message'))
                # else:
                #     raise Exception('{}'.format(i))






if __name__ == '__main__':
    ibox = Ibox()

    url = '123'

    dict_in = {u'Cache-Control': u'no-cache',
               u'client_id': u'380639452935',
               u'Accept': u'*/*',
               u'amount': '100',
               # u'company_name': u'FDY GLOVO ZAPEL',
               u'Content-Type': u'application/json'}


    list_well = ibox.request_well(dict_in)
    list_empty = ibox.request_empty(dict_in)
    list_pass = ibox.request_pass(dict_in)

    # ibox.generate_payment_ibox(url, list_well)
    ibox.generate_payment_ibox(url, list_empty)
    # ibox.generate_payment_ibox(url, list_pass)


