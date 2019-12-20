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
        col = 0
        row = 0
        head_con = ({'Наш счет': '26504015021901'},
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
                    {'Ид.код': '38905834'},
                    {'Наименование': 'ТОВ "ФК "ЕЛАЄНС"'},
                    {'МФО': '300346'})

        for header in head_con:
            worksheet.write(row, col, list(header)[0])
            print(col, list(header)[0])
            col += 1

        for row in range(1, len(data) + 1):
            worksheet.write(row, 0, '26504015021901')
            worksheet.write(row, 1, 'UA463003460000026504015021901')
            worksheet.write(row, 2, 'Дебет')
            worksheet.write(row, 11, 'UAH')
            worksheet.write(row, 15, '38905834')
            worksheet.write(row, 16, 'ТОВ "ФК "ЕЛАЄНС"')
            worksheet.write(row, 17, '300346')

        try:
            workbook.save(path + filename)
        except:
            pass

if __name__ == '__main__':
    create = Create_xls()
    pattern = 'Doc_'
    path = 'xls/'

    headers = [[{'Наш счет': '26504015021901'},
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
    create.create_xls(path, pattern, headers)
