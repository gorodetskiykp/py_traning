import csv
import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent


class DataSource:

    def read(self, **kwargs):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(kwargs['file_name']), 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row.
            for row in reader:
                hour = datetime.datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour


# from open_weather_csv import DataSource
# from open_weather_json import DataSource
# from open_weather_api import DataSource
# csv_reader = DataSource()
# reader.read(file_name='foo.csv')
# json_reader = DataSource()
# reader.read(file_name='foo.json')
# api_reader = DataSource()
# reader.read(url='https://foo.bar')