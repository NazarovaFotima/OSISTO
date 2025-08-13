from django.db import models
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from users.models import ClientProfile
from users.serializers import ClientsSerializer


class CustomPagination(PageNumberPagination):
    page_size = 5


class ClientsViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    """
    ViewSet for WorkerProfile that supports:
    - GET /workers/{id}/
    - PUT /workers/{id}/
    - PATCH /workers/{id}/
    - DELETE /workers/{id}/
    """
    queryset = ClientProfile.objects.all()
    serializer_class = ClientsSerializer
    pagination_class = CustomPagination
    # Add permissions if needed
    # permission_classes = [IsAuthenticated]

    # Include the mixins to enable retrieve, update, destroy
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

