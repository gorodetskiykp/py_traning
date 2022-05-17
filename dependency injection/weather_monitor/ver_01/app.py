import csv
import datetime
from pathlib import Path

import matplotlib.dates
import matplotlib.pyplot


BASE_DIR = Path(__file__).resolve(strict=True).parent


class App:

    def read(self, file_name):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(file_name), 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row.
            for row in reader:
                hour = datetime.datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour

    def draw(self, temperatures_by_hour):
        dates = []
        temperatures = []

        for date, temperature in temperatures_by_hour.items():
            dates.append(datetime.datetime.fromisoformat(date))
            temperatures.append(temperature)

        dates = matplotlib.dates.date2num(dates)
        matplotlib.pyplot.plot_date(dates, temperatures, linestyle='-')
        matplotlib.pyplot.show()


if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]
    app = App()
    temperatures_by_hour = app.read(file_name)
    app.draw(temperatures_by_hour)