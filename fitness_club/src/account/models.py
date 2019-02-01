from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_client = models.BooleanField('client_status', default=False)
    is_employee = models.BooleanField('employee_status', default=False)

    def __str__(self):
        fullname = '{} {}'.format(self.first_name, self.last_name)
        return fullname

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE,
                                related_name='profile')
    picture = models.ImageField(upload_to='employees/',
                                blank=True)
    miniature = models.ImageField(upload_to='employees/',
                                blank=True)
    description = models.TextField(max_length=2000,
                                   null=True,
                                   blank=True)