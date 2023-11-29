import requests
response = requests.get("https://swapi.dev/api/people/1/")
data = response.json()
print(data["mass"])

# it calls Name value of the list from above url. response: 77
