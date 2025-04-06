from django.test import Client, TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('login') 
        print("Setup Sucess!!")

    def test_homepage_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_logout_flow(self):
        user = User.objects.create_user(username='testuser', password='testpass')

        login_response = self.client.post(reverse('login'), {'username': 'testuser', 'password1': 'testpass'})
        self.assertEqual(login_response.status_code, 302)  

        logout_response = self.client.get(reverse('logout'))
        self.assertEqual(logout_response.status_code, 200)
        self.assertContains(logout_response, "Logged Out Successfully.")