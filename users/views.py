from django.shortcuts import render
from faker import Faker
from .models import User
from django.core.exceptions import ValidationError


fake = Faker()

def create_random_users(num_entries):
    if not isinstance(num_entries, int) or num_entries <= 0:
        raise ValueError("num_entries debe ser un número entero positivo")

    User.objects.all().delete()

    users = []
    for _ in range(num_entries):
        gender = fake.random_element(elements=['M', 'F'])
        name = fake.name_male() if gender == 'M' else fake.name_female()
        age = fake.random_int(min=18, max=70)
        user = User(name=name, age=age, gender=gender)
        
        try:
            user.full_clean()
            users.append(user)
        except ValidationError as e:
            print(f"Error validating user: {e.message_dict}")

    User.objects.bulk_create(users)