import requests

#https://statsapi.web.nhl.com/api/v1/teams
#Application Programming Interface = API

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
print(response.json())

nhl_data = response.json()

print(nhl_data['name'])