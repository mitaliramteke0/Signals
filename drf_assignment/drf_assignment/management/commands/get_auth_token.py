from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Obtain an authentication token'

    def handle(self, *args, **options):
        api_base_url = 'http://http://127.0.0.1:8000/api/token/'

        data = {
            'username': 'mitali_ramteke',
            'password': 'admin',
        }

        response = requests.post(api_base_url, data=data)

        if response.status_code == 200:
            token = response.json()['token']
            self.stdout.write(self.style.SUCCESS(f"Token for user 'mitali_ramteke': {token}"))
        else:
            self.stdout.write(self.style.ERROR("Token request failed."))
