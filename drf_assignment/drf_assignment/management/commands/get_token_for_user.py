import requests


api_base_url = 'http://127.0.0.1:8000/api/token/'


data = {
    'username': 'mitali_ramteke',
    'password': 'actual_password',
}

response = requests.post(api_base_url, data=data)

if response.status_code == 200:
    token = response.json()['token']
    print(f"Token for user 'mitali_ramteke': {token}")
else:
    print(f"Token request for 'mitali_ramteke' failed.")
