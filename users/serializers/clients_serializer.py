from rest_framework import serializers
from users.models import ClientProfile


class ClientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = '__all__'