from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import WorkerProfile



class WorkerProfileTests(APITestCase):
    # python manage.py dumpdata users.WorkerProfile --format=yaml --indent=4 > users/fixtures/workers.yaml
    fixtures = ['workers']

    def setUp(self):
        self.worker = WorkerProfile.objects.get(pk=1)


    def test_worker_detail(self):
        url = reverse('workerprofile-detail', args=[self.worker.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_worker_update(self):
        url = reverse('workerprofile-detail', args=[self.worker.pk])
        data = {
            "user": 2,
            "first_name": "Zuxra",
            "last_name": "string",
            "bio": "string",
            "gender": "man",
            "hourly_rate": "10.00",
            "experience_years": 2,
            "availability": True,
            "location": "string",
            "portfolio_images": {},
            "created_at": "2025-08-13T06:04:22.338042Z"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_worker_delete(self):
        url = reverse('workerprofile-detail', args=[self.worker.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)