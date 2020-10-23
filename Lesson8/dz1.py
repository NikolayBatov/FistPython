class Date:

    def __init__(self, str_date: str) -> None:
        self.__str_date = str_date

    def __str__(self) -> str:
        return self.__str_date

    @classmethod
    def get_date_as_num(cls, obj):
        return list(map(int, obj.str_date.split('-')))

    @staticmethod
    def validate_date(obj):
        try:
            day, month, year = Date.get_date_as_num(obj)
            if 0 < day < 32 and 0 < month < 13 and float('-inf') < year < float('inf'):
                return True
            return False
        except Exception as ex:
            print(ex)
            return False

    @property
    def str_date(self):
        return self.__str_date


date = Date('21-12-2002')
print(date)
print(Date.get_date_as_num(date))
print(Date.validate_date(date))

date = Date('61-12-2002')
print(date)
print(Date.get_date_as_num(date))
print(Date.validate_date(date))