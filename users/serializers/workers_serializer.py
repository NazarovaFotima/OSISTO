from rest_framework import serializers
from users.models import WorkerProfile


class WorkersSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)

    class Meta:
        model = WorkerProfile
        fields = ['id', 'user', 'avg_rating', 'first_name',  'last_name', 'bio', 'gender',
                  'hourly_rate', 'experience_years', 'availability', 'location',
                  'portfolio_images', 'id_verification',  'created_at']