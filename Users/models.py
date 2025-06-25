from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    income = models.IntegerField(max_length=100000, null = True, blank = True, default=0)
    expense = models.IntegerField(max_length=100000, null = True, blank = True, default=0)
    invoice = models.IntegerField(max_length=100000, null = True, blank = True, default=0)
    profit_after_tax = models.IntegerField(max_length=100000, null = True, blank = True, default=0)

    def __str__(self):
        return self.user.username

