from django.contrib import admin

from .models import WorkerProfile, ClientProfile
from .models.users_auth import CustomUser

admin.site.register(CustomUser)
admin.site.register(WorkerProfile)
admin.site.register(ClientProfile)
