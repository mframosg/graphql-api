from django.shortcuts import render
from faker import Faker
from .models import User

fake = Faker()

def create_random_users(num_entries):
    User.objects.all().delete()  # Truncate the table

    users = [User(name=fake.name(), age=fake.random_int(min=18, max=70)) for _ in range(int(num_entries))]

    User.objects.bulk_create(users)