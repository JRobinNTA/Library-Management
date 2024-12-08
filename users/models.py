from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    MEMBERSHIP_CHOICES = [
        ('REGULAR', 'Regular'),
        ('PREMIUM', 'Premium')
    ]
    
    membership_type = models.CharField(
        max_length=10, 
        choices=MEMBERSHIP_CHOICES, 
        default='REGULAR'
    )
    registered_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.username