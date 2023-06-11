import requests
import json

# Set up login credentials
username = 'admin'
password = 'admin'

# Set up API URL
url = 'http://65.109.190.127:54321/xui/API/inbounds/add'

# Log in to the GUI panel
payload = {
    "email": username,
    "password": password
}

response = requests.post(url + '/login', json=payload)
token = json.loads(response.text)['data']['token']

# Get the current configuration
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

response = requests.get(url + '/config', headers=headers)
config = json.loads(response.text)

# Find the client to edit
client_index = 0 # Replace with the index of the client you want to edit
client = config['inbounds'][0]['settings']['clients'][client_index]

# Update the total flow
client['flow'] = "255"

# Update the configuration
payload = {
    "v": config,
    "format": "protobuf"
}

response = requests.post(url + '/config', headers=headers, json=payload)

print(response.text)
