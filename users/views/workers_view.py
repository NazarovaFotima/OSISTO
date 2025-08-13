from django.db import models
from rest_framework import mixins, viewsets
# from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
from users.models import WorkerProfile
from users.serializers import WorkersSerializer


class CustomPagination(PageNumberPagination):
    page_size = 5


class WorkersViewSet(viewsets.GenericViewSet,
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
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkersSerializer
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

    # @action(detail=False, methods=['get'])
    # def top_rated(self, request):
    #
    #     # Assuming a related name of "reviews" from Review model to Product model
    #     top_products = WorkerProfile.objects.annotate(avg_rating=models.Avg('reviews__rating')).order_by('-avg_rating')[:2]
    #     serializer = WorkersSerializer(top_products, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=True, methods=['get'])
    # def average_rating(self, request, pk=None):
    #     product = self.get_object()
    #     reviews = product.reviews.all()
    #
    #     if reviews.count() == 0:
    #         return Response({"average_rating": "No reviews yet!"})
    #
    #     avg_rating = sum([review.rating for review in reviews]) / reviews.count()
    #
    #     return Response({"average_rating": avg_rating})