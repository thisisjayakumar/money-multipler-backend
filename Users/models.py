import random
from django.db import models
from .enums import LevelType, WithdrawalType

def generate_user_id():
    return str(random.randint(100000, 999999))

class User(models.Model):
    user_id = models.CharField(max_length=6, unique=True, default=generate_user_id)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50, choices=LevelType.choices, default=LevelType.BRONZE)
    occupation = models.CharField(max_length=255)
    age = models.IntegerField()
    withdraw_method = models.CharField(max_length=50, choices=WithdrawalType.choices, default=WithdrawalType.UPI)
    withdraw_account_id = models.CharField(max_length=50, null=True, blank=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bank_no = models.CharField(max_length=20, blank=True, null=True)
    ufsc = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.name
