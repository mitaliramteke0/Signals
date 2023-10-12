from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Description of your custom command'

    def handle(self, *args, **options):
        headers = {
            'Authorization': 'Token 69da30ef2c0c91cee2116ab3f02ffa9c1f6b3cc1'
        }

        api_base_url = 'http://http://127.0.0.1:8000/api/posts/by_author/1/'

        response = requests.get(api_base_url, headers=headers)

        if response.status_code == 200:
            # Process the response data here
            # For example, print the response content
            print(response.json())
        else:
            print("Request to /api/posts/by_author/1/ failed.")
