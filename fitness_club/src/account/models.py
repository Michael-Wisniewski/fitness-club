from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_client = models.BooleanField('client_status', default=False)
    is_employee = models.BooleanField('employee_status', default=False)

    def __str__(self):
        fullname = '{} {}'.format(self.first_name, self.last_name)
        return fullname
