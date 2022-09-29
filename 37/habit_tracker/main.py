import os
from dotenv import load_dotenv
import requests
import datetime as dt
load_dotenv()
USERNAME = "jibbycodes34"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_parameters = {
    "token": os.getenv("MY_SECRET"),
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_parameters)

# print(response.text)

graph_parameters = {
    "id": "test-graph",
    "name": "graph-name",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

graph_headers = {
    "X-USER-TOKEN": os.getenv("MY_SECRET")
}

# response = requests.post(graph_endpoint, json=graph_parameters, headers=graph_headers)

# print(response.text)

today = dt.datetime.now()


# ==== POSTING A GRAPH =======
# value_parameters = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "100"
# }

# response = requests.post(
#     f"{graph_endpoint}/test-graph", json=value_parameters, headers=graph_headers)

# print(response)
# print(response.text)

# ===== UPDATING A GRAPH ========

update_endpoint = f"{graph_endpoint}/test-graph/{today.strftime('%Y%m%d')}"
update_parameters = {
    "color": "momiji",
    "quantity": "12121",
}

# Updating
# response = requests.put(update_endpoint,
#                         headers=graph_headers, json=update_parameters)

# Deleting
response = requests.delete(update_endpoint, headers=graph_headers)

print(response)
print(response.text)
