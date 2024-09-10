
from django.test import TestCase
from django.contrib.auth.models import User

class UserAuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_user_registration(self):
        response = self.client.post('/accounts/register/', {
            'username': 'newuser',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        response = self.client.post('/accounts/login/', {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
