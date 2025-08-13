from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class WorkerProfile(models.Model):

    class GenderChoices(models.TextChoices):
        MAN = 'man', 'Man'
        WOMAN = 'woman', 'Woman'
        PREFER_NOT_TO_SAY = 'not_say', 'Prefer not to say'


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker_profile')
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)

    bio = models.TextField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        blank=True,
        null=True
    )
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=True)
    # skills = models.ManyToManyField('categories.Category', related_name='workers')
    location = models.CharField(max_length=255)  # Or use GeoDjango later
    portfolio_images = models.JSONField(blank=True, null=True)  # URLs to uploaded images
    id_verification = models.FileField(upload_to='verifications/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username=self.first_name+ ' '+self.last_name
        return f"{username}'s Profile"