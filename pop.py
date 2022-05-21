import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')

import django
django.setup()

import random
from myapp.models import *
from faker import Faker

fake_gen = Faker()

def add_user():
    user = User.objects.get_or_create(name=random.choice())[0]
    user.save()
    return user

def populate(N=5):
    for entry in range(N):
        fake_username = fake_gen.name()
        fake_password = fake_gen.password()

        user = User.objects.get_or_create(username=fake_username, password=fake_password)[0]

if __name__ == '__main__':
    print('pop')
    populate(5)
