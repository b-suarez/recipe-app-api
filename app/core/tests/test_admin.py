from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """Setup function for all the tests"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test_admin@gmail.com',
            password='password'
        )
        # Logs in with the superuser
        self.client.force_login(self.admin_user)

        # Creates a new user
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='password',
            name='Test user'
        )

    def test_users_listed(self):
        """Test that users are correctly listed in the page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page renders correctly"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
