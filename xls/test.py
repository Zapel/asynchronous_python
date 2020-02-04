import xlwt
import datetime

class Create_xls():

    def generate_name_alfa(self, pattern):
        date = datetime.datetime.now().strftime('%y%m%d')
        filename = '{}{}.xls'.format(pattern, date)
        print(filename)
        return filename

    def create_xls(self, path, pattern, data):
        filename = self.generate_name_alfa(pattern)
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet('Sheet0')
        string = 'Сплата по прийнятим платежам {} - {} Без ПДВ.Згд.дог. 3171819615 вiд 2015/05/19 Сум {} Ком {} :: Реф=1'
        string1 = 'Сплата по прийнятим платежам {} - {} Без ПДВ.Згд.дог. 3171819615 вiд 2015/05/19 Сум {} Ком {} :: Реф=2'

        date = '2019-12-21'
        sum = 8324.41
        com = 430.43

        col = 0
        row = 0
        headers = ('Наш счет', 'Наш IBAN', 'Операция', 'Счет', 'IBAN', 'МФО банка', 'Наименование контрагента', 'Код контрагента',
                   'Назначение платежа', 'Дата проводки', 'Номер документа', 'Сумма', 'Валюта', 'Время проводки', 'Дата документа',
                   'Дата архивирования', 'Ид.код', 'Наименование', 'МФО')

        for header in headers:
            worksheet.write(row, col, header)
            print(col, header)
            col += 1

        for row in range(1, len(data) + 1):
            worksheet.write(row, 0, int(26504015021901))
            worksheet.write(row, 1, str('UA463003460000026504015021901'))
            worksheet.write(row, 2, str('Дебет'))
            worksheet.write(row, 3, int(13000000100))
            worksheet.write(row, 5, int(131313))
            worksheet.write(row, 6, str('Zapel'))
            worksheet.write(row, 7, int(3171819615))

            if row in [1, 3]:
                worksheet.write(row, 8, string)
            else:
                worksheet.write(row, 8, string1)
            # worksheet.write(row, 9, data[row - 1]['date'])
            # worksheet.write(row, 10, data[row-1]['trans_id'])
            worksheet.write(row, 10, int(2158267))
            # worksheet.write(row, 11, data[row - 1]['amount'] - data[row - 1]['fee'])
            worksheet.write(row, 11, float(sum - com))
            worksheet.write(row, 12, str('UAH'))
            # worksheet.write(row, 13, data[row - 1]['time'])
            # worksheet.write(row, 14, data[row - 1]['date'])
            # worksheet.write(row, 15, data[row - 1]['date'])
            worksheet.write(row, 16, int(38905834))
            worksheet.write(row, 17, str('ТОВ "ФК "ЕЛАЄНС"'))
            worksheet.write(row, 18, int(300346))

        try:
            workbook.save(path + filename)
        except:
            pass

if __name__ == '__main__':
    create = Create_xls()
    pattern = 'Doc_'
    path = 'xls/'

    data = [[{'Наш счет': '26504015021901'},
               {'Наш IBAN': 'UA463003460000026504015021901'},
               {'Операция': 'Дебет'},
               {'Счет IBAN': ''},
               {'МФО банка': ''},
               {'Наименование контрагента': ''},
               {'Код контрагента': ''},
               {'Назначение платежа': ''},
               {'Дата проводки': ''},
               {'Номер документа': ''},
               {'Сумма': ''},
               {'Валюта': 'UAH'},
               {'Время проводки': ''},
               {'Дата документа': ''},
               {'Дата архивирования': ''},
               {'Ид.код': '300346'},
               {'Наименование': 'ТОВ "ФК "ЕЛАЄНС"'},
               {'МФО': '300346'}],
               [{'Наш счет': '26504015021901'},
               {'Наш IBAN': 'UA463003460000026504015021901'},
               {'Операция': 'Дебет'},
               {'Счет IBAN': ''},
               {'МФО банка': ''},
               {'Наименование контрагента': ''},
               {'Код контрагента': ''},
               {'Назначение платежа': ''},
               {'Дата проводки': ''},
               {'Номер документа': ''},
               {'Сумма': ''},
               {'Валюта': 'UAH'},
               {'Время проводки': ''},
               {'Дата документа': ''},
               {'Дата архивирования': ''},
               {'Ид.код': '300346'},
               {'Наименование': 'ТОВ "ФК "ЕЛАЄНС"'},
               {'МФО': '300346'}]]

    create.generate_name_alfa(pattern)
    create.create_xls(path, pattern, data)
