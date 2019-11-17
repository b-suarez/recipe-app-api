from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user with email "succesfully"""
        email = 'test@gmail.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test if the email for a new user is normalized"""
        email = 'tESt@gmAIL.com'
        user = get_user_model().objects.create_user(email, 'password')

        self.assertEqual(user.email, email.lower())
