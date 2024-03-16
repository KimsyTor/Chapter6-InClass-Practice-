import requests

api_key = '7cc82b34'
endpoint = 'http://www.omdbapi.com/'

r = requests.get('http://www.omdbapi.com/?apikey=7cc82b34&t=ABC')
print(r)
# print(r.json())
# print(r.text)

### using params parameter ####
# params = {
#     "apikey": api_key,
#     "t": "abc"
# }

# r = requests.get(endpoint, params=params).json()
