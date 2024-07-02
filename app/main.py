# data = [
#   {
#     'Country': 'Colombia',
#     'Population': 500
#   },
#   {
#     'Country': 'Bolivia',
#     'Population': 300
#   }
# ]

# def run():
#   key, values = utils.get_population()
#   print(key, values)

#   print(utils.A)

#   country = input('Type Country => ')

#   result = utils.population_by_country(data, country)
#   print(result)

import utils
import read_csv
import charts
import pandas as pd


def run():
  '''
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  df = pd.read_csv('./data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')
  print(country)

  data = read_csv.read_csv('./data.csv')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    keys, values = utils.get_population_2(country)
    charts.generate_bar_chart(country['Country'], keys, values)
  
  # print(result)
  # print(data[0]['Country'], data[0]['World Population Percentage'])
  
  # map array to dict
  # country_dict = {item['Country']: item['World Population Percentage'] for item in data}
  # # print(country_dict)
  # keys = country_dict.keys()
  # values = country_dict.values()
  # charts.generate_pie_chart(keys, values)

if __name__ == '__main__':
  run()
