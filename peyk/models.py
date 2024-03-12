from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES=[('0', 'Pending acceptance'),
                ('1', 'Courier in route to pickup location'),
                ('2', 'Courier in route to destination'),
                ('3', 'Completed'),
                ('4', 'Cancelled')]

USER_ROLES=[('customer', 'customer'),
            ('driver', 'driver')]

class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 11)
    role = models.CharField(choices = USER_ROLES, max_length = 50)
    
    def __str__(self) -> str:
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT, related_name = 'user')
    driver = models.ForeignKey(User, on_delete = models.PROTECT, related_name = 'driver')
    origin = models.CharField(max_length = 20)
    destination = models.CharField(max_length = 20)
    price = models.PositiveIntegerField()
    time_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(choices =STATUS_CHOICES, max_length = 100, default = '0')
    duration = models.DurationField()
    is_payed = models.BooleanField()
    description = models.TextField(blank = True)
