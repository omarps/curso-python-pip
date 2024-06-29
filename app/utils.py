def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

def get_population_2(country_dict):
  population_dict = {
    # '2022': int(country_dict['2022 Population']),
    # '2020': int(country_dict['2020 Population']),
    # '2015': int(country_dict['2015 Population']),
    # '2010': int(country_dict['2010 Population']),
    # '2000': int(country_dict['2000 Population']),
    # '1990': int(country_dict['1990 Population']),
    # '1980': int(country_dict['1980 Population']),
    # '1970': int(country_dict['1970 Population'])
    '2022': country_dict['2022 Population'],
    '2020': country_dict['2020 Population'],
    '2015': country_dict['2015 Population'],
    '2010': country_dict['2010 Population'],
    '2000': country_dict['2000 Population'],
    '1990': country_dict['1990 Population'],
    '1980': country_dict['1980 Population'],
    '1970': country_dict['1970 Population']
  }
  return population_dict.keys(), population_dict.values()

A = 'Hola'

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result