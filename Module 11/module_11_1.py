import requests
import pandas as pd


def get_data(url):
    response = requests.get(url)
    print(response.json())


print("\n библиотека requests \n")
get_data('https://api.github.com')

data = pd.read_csv('data.csv')
print("\n библиотека pandas \n")

print(data.head())

average = data['column_name'].mean()
print(f'Среднее значение столбца "column_name": {average}')
