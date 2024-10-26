import random
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=6, unique=True, default=lambda: str(random.randint(100000, 999999)))
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    occupation = models.CharField(max_length=255)
    age = models.IntegerField()
    withdraw_method = models.CharField(max_length=50, choices=[('BANK', 'Bank'), ('UPI', 'UPI')])
    withdraw_account_id = models.CharField(max_length=50)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    bank_no = models.CharField(max_length=20, blank=True, null=True)
    ufsc = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.name
