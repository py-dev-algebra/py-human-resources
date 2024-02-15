# Sve funkcije vezane uz manipulaciju podacima djelatnika 
# na REST api serveru
import requests


# TODO implement try except
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
if response.status_code == 200:
    print(response.json())
