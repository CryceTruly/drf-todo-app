from .test_setup import TestSetup
from rest_framework import status

class TestViews(TestSetup):
    def test_creates_user(self):
        response=self.client.post(self.register_url,self.user_data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_gives_descriptive_errors_on_register(self):
        response=self.client.post(self.register_url,{'email':self.user_data['email']})
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_logins_user(self):
        user=self.register_user()
        response=self.client.post(self.login_url, {'email':user.email,'password':self.user_data['password']})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(response.data['token'],str)

    def test_gives_descriptive_errors_on_login(self):
        response=self.client.post(self.login_url, {'email':'test@site.com','password':self.user_data['password']})
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
