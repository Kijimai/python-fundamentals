import requests
# res = requests.get(url="https://pokeapi.co/api/v2/pokemon/ditto")
# res_json = res.json()
# res.raise_for_status()
# print(res_json)
res = requests.get("http://api.open-notify.org/iss-now.json")
res.raise_for_status()
iss_position = res.json()["iss_position"]
iss_longitude = iss_position["longitude"]
iss_latitude = iss_position["latitude"]
print(iss_longitude, iss_latitude)