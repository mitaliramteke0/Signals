import requests

# Replace 'your_api_base_url' with the actual base URL of your API
api_base_url = 'http://your_api_base_url/api/token/'

# Replace 'your_username' and 'your_password' with the user's credentials
data = {
    'username': 'your_username',
    'password': 'your_password',
}

response = requests.post(api_base_url, data=data)

if response.status_code == 200:
    token = response.json()['token']
    print(f"Token for user 'your_username': {token}")
else:
    print("Token request failed.")
