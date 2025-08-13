from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import  ClientProfile


class ClientProfileTests(APITestCase):
    # python manage.py dumpdata users.ClientProfile --format=yaml --indent=4 > users/fixtures/clients.yaml
    fixtures = ['clients']

    def setUp(self):

        self.client1= ClientProfile.objects.get(pk=2)



    def test_client_detail(self):
        url = reverse('clientprofile-detail', args=[self.client1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_client_update(self):
        url = reverse('clientprofile-detail', args=[self.client1.pk])
        data = {
            "first_name": "Alijon",
            "last_name": "Alijon",
            "bio": "string",
            "user": 3
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.status_code)

    def test_worker_delete(self):
        url = reverse('clientprofile-detail', args=[self.client1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)