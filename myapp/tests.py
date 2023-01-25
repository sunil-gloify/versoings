import json
from myapp.models import *
from rest_framework.test import APITestCase
from .api.base.views import *
from django.test import Client
from rest_framework.test import APIRequestFactory



class UserModelViewsTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
        first_name='test', last_name='user', age=20)
        self.view = USerVS.as_view(actions={'post': 'create'})


    def test_model_create(self):
        user = User.objects.create(first_name='test', last_name='user', age=20)
        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'user')
        self.assertEqual(user.age, 20)

    def test_view_create(self):
        data = {'first_name': 'newuser', 'last_name': 'newlastname', 'age': 30}
        request = self.factory.post('/users/', data=data)
        view = USerVS.as_view(actions={'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(
            first_name='newuser').last_name, 'newlastname')
        self.assertEqual(User.objects.get(first_name='newuser').age, 30)

    