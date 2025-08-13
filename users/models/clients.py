from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        username =  self.first_name + ' '+ self.last_name
        return f"{username}'s Profile"