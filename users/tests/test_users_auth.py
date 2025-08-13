from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase



class SMSLoginViewSetTestCase(APITestCase):

    def test_send_sms(self):
        self.client.force_authenticate(user=None)  # "Log out" to make the client anonymous
        url = reverse('send_sms')
        data = {'phone_number': '+998998668370'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_send_sms(self):
        self.client.force_authenticate(user=None)  # "Log out" to make the client anonymous
        url = reverse('verify_sms')
        data = {'phone_number': '+998998668370', 'verification_code': '123456'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
