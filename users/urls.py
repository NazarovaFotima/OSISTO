from django.urls import path
from .views import SMSLoginViewSet


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import ClientsViewSet, WorkersViewSet


router = DefaultRouter()
router.register(r'clients', ClientsViewSet)
router.register(r'workers', WorkersViewSet)



urlpatterns = [
    path(' ', include(router.urls)),
]