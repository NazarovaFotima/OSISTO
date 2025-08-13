from rest_framework import status, viewsets
from rest_framework.response import Response
from django.core.cache import cache
import random
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action

from users.serializers import SMSSerializer, VerifySMSSerializer
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

SMS_KEY = settings.SMS_KEY

class SMSLoginViewSet(viewsets.ViewSet):
    """
    SMS-Based Authentication API for OSISTO (Oson Ish Top)

    A service marketplace for finding daily workers (housekeepers, babysitters, caregivers).
    This API handles login/registration via SMS verification.
    """

    @swagger_auto_schema(
        method='post',
        request_body=SMSSerializer,
        responses={
            200: openapi.Response(
                description="SMS sent successfully",
                examples={
                    "application/json": {
                        "message": "SMS sent successfully"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request (invalid phone number or failed SMS)",
                examples={
                    "application/json": {
                        "phone_number": ["Enter a valid phone number."],
                        "message": "Failed to send SMS"
                    }
                }
            ),
        },
        operation_summary="Send SMS Verification Code",
        operation_description="Sends a 6-digit verification code to the given phone number via Infobip SMS gateway.",
    )
    @action(detail=False, methods=['post'], url_path='send-sms')
    def send_sms(self, request):
        serializer = SMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']

            # Generate 6-digit code
            verification_code = str(random.randint(100000, 999999))

            # SMS URL and headers
            url = 'https://wgj441.api.infobip.com/sms/2/text/advanced'
            headers = {
                'Authorization': SMS_KEY,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            payload = {
                'messages': [
                    {
                        'from': 'evos.uz',
                        'destinations': [{'to': phone_number}],
                        'text': f'Your verification code is {verification_code}'
                    }
                ]
            }

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                cache.set(phone_number, verification_code, 300)  # 5 min
                return Response({"message": "SMS sent successfully"}, status=status.HTTP_200_OK)

            return Response({"message": "Failed to send SMS"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        method='post',
        request_body=VerifySMSSerializer,
        responses={
            200: openapi.Response(
                description="Login successful",
                examples={
                    "application/json": {
                        "refresh": "eyJhbGciOiJIUzI1NiIs...",
                        "access": "eyJhbGciOiJIUzI1NiIs..."
                    }
                }
            ),
            400: openapi.Response(
                description="Invalid code or input",
                examples={
                    "application/json": {
                        "message": "Invalid verification code"
                    }
                }
            ),
        },
        operation_summary="Verify Code & Get JWT Tokens",
        operation_description="Verifies the 6-digit code. If valid, returns JWT tokens (creates user if new).",
    )
    @action(detail=False, methods=['post'], url_path='verify-sms')
    def verify_sms(self, request):
        serializer = VerifySMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']
            cached_code = cache.get(phone_number)

            if verification_code == cached_code:
                user, created = User.objects.get_or_create(phone_number=phone_number)
                if created:
                    user.username = phone_number  # Optional: set username
                    user.save()

                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)

            return Response({"message": "Invalid verification code"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)