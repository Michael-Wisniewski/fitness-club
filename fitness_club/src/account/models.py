from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_client = models.BooleanField('client status', default=False)
    is_employee = models.BooleanField('employee status', default=False)
