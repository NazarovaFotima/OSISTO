from django.contrib import admin
from .models.users_auth import CustomUser

admin.site.register(CustomUser)
