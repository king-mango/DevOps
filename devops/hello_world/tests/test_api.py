from http import client
from urllib import response
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
import json

# Create your tests here.

class APITest(APITestCase):
    
    def test_status(self):
        client = APIClient()
        response = client.get(path='http://127.0.0.1:8000/hello-world/test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hello(self):
        client = APIClient()
        data = json.dumps({"name": "nexus"})
        response = client.post(path='http://127.0.0.1:8000/hello-world/hello', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    
