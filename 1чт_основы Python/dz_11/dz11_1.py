class The_date:
    def __init__(self, string_date):
        self.string_date = string_date

    def __str__(self):
        return self.string_date

    @classmethod
    def date_numbers(cls, string_date):
        number = []
        for el in string_date.split('-'):
            number.append(int(el))
        return number

    @staticmethod
    def real_data(string_date):
        number = []
        for el in string_date.split('-'):
            number.append(int(el))
        if 0 < number[0] <= 31 and 0 < number[1] <= 12 and number[2] > 0:
            return f'{string_date}'
        else:
            return f'не верно задана дата'


the_date1 = The_date('29-05-2022')
print(the_date1)
print(the_date1.date_numbers('15-05-2022'))
print(the_date1.real_data('11-05-2022'))
print(the_date1.real_data('32-05-2022'))
