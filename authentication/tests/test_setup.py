from rest_framework.test import APITestCase
from django.urls import reverse
from authentication.models import User

class TestSetup(APITestCase):
    def setUp(self):
        self.login_url=reverse('login')
        self.register_url=reverse('register')

        self.user_data={'username':"username",'email':"email@test.com","password": "password1@212"}
        return super().setUp()


    def register_user(self):
        return User.objects.create_user(**self.user_data)
        

