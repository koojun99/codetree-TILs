class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
forecasts = []

for _ in range(n):
    date, day, weather = tuple(input().split())
    forecasts.append(Forecast(date, day, weather))

forecasts.sort(key = lambda x: x.date)
for forecast in forecasts:
    if forecast.weather == "Rain":
        print(forecast.date + " " + forecast.day + " " + forecast.weather)
        break