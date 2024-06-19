from datetime import datetime

class SuperDate(datetime):

    dict_season = {(12, 1, 2): "Зима", range(3, 6): 'Весна', range(6, 10): 'Лето', range(10, 12): 'Осень'}
    dict_time = {range(6, 12): 'Утро', range(12, 18): 'День', range(18, 24): 'Вечер', range(0, 6): 'Ночь'}

    def __init__(self, year, month, day, hour):
        self.date = datetime(year,month,day,hour)

    def get_season(self):
        for i in self.dict_season:
            if self.date.month in i:
                return self.dict_season[i]

    def get_time_of_day(self):
        for i in self.dict_time:
            if self.date.hour in i:
                return self.dict_time[i]


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())