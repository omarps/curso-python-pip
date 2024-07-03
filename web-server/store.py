import requests

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(response.status_code)
    print(response.json())
    # return response.json()
    categories = response.json()
    for category in categories:
        print(category['name'])