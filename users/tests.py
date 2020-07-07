from django.test import TestCase
from .models import CustomUser
from rest_framework import status
from django.urls import reverse
from .models import CustomUser


class UserTests(TestCase):
    reg_url = reverse('users:rest_register')
    login_url = reverse('users:rest_login')
    user_url = reverse('users:rest_user_details')
    user_data = {
        "username": "tommy",
        "email": "tommy@gmail.com",
        "password1": "myPassword1",
        "password2": "myPassword1"
    }
    login_data = {
        "email": "tommy@gmail.com",
        "password": "myPassword1"
    }
    # The Email must be set

    def test_user_registration(self):
        """
        Ensure that we can create a user
        """
        response = self.client.post(
            self.reg_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_user_registration_no_email(self):
        """
        Ensure that we cannot create a user without email
        """
        wrong_user_data = {
            "username": "tommy",
            "password1": "myPassword1",
            "password2": "myPassword1"
        }
        response = self.client.post(
            self.reg_url, wrong_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('This field is required.', response.data['email'])

    def test_user_login(self):
        """
        Ensure that we can login a user
        """
        self.client.post(self.reg_url, self.user_data, format='json')
        response = self.client.post(
            self.login_url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_wrong_user_login(self):
        """
        Ensure that we cannot login a wrong user
        """
        wrong_login_data = {
            "email": "tommy@wrong.com",
            "password": "passw3e4"
        }
        response = self.client.post(
            self.login_url, wrong_login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Unable to log in with provided credentials.',
                      response.data['non_field_errors'])

    def test_user_detail(self):
        """
        get the loggedin user details
        """
        self.client.post(self.reg_url, self.user_data, format='json')
        self.client.post(self.login_url, self.login_data, format='json')
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('date_of_birth', response.data)
