import string

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from celery import shared_task

User = get_user_model()

@shared_task
def create_random_user(total):
    for i in range(total):
        username = f'user_{get_random_string(10, string.ascii_letters)}'
        email = f'{username}@test.com'
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return f'{total} random users created with success!'

