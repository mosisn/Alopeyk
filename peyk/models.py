from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

STATUS_CHOICES=[('0', 'Pending acceptance'),
                ('1', 'Courier in route to pickup location'),
                ('2', 'Courier in route to destination'),
                ('3', 'Completed'),
                ('4', 'Cancelled')]

USER_ROLES=[('customer', 'customer'),
            ('driver', 'driver')]

class Account(AbstractUser):
    username = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 11, unique= True)
    role = models.CharField(choices = USER_ROLES, max_length = 50)
    password = models.CharField(max_length= 128)
    otp = models.CharField(max_length = 5, blank=True)
    is_authorized = models.BooleanField(default= False)
    groups = models.ManyToManyField(Group, related_name='user_accounts', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_accounts', blank=True)
    
    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete = models.PROTECT, related_name = 'user')
    driver = models.ForeignKey(Account, on_delete = models.PROTECT, related_name = 'driver')
    origin = models.CharField(max_length = 20)
    destination = models.CharField(max_length = 20)
    price = models.PositiveIntegerField()
    time_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(choices =STATUS_CHOICES, max_length = 100, default = '0')
    duration = models.DurationField()
    is_payed = models.BooleanField()
    description = models.TextField(blank = True)
