from django.db import models

class LevelType(models.TextChoices):
    BRONZE = 'BRONZE', 'Bronze'
    SILVER = 'SILVER', 'Silver'
    GOLD = 'GOLD', 'Gold'
    PLATINUM = 'PLATINUM', 'Platinum'

class WithdrawalType(models.TextChoices):
    BANK = 'BANK', 'Bank'
    UPI = 'UPI', 'UPI'
