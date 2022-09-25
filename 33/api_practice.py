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

sunrise_params = {
  "lat": iss_latitude,
  "lng": iss_longitude,
  "formatted": 0
}

sun_data = requests.get("https://api.sunrise-sunset.org/json", params=sunrise_params)

sun_data.raise_for_status()
sun_data_json = sun_data.json()

# converted for 24-hour time
sunrise_time = sun_data_json["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_time = sun_data_json["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise_time, sunset_time)