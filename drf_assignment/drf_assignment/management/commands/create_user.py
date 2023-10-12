# myapp/management/commands/create_user.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a user'

    def handle(self, *args, **options):
        # Create a user
        user = User.objects.create_user(username='mitali_ramteke', password='mitali@password')

        # Optionally, set other user attributes such as email
        user.email = 'mitali@gmail.com'
        user.save()
        self.stdout.write(self.style.SUCCESS('User created successfully.'))
