from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfileTestViews(TestCase):
    """ Test module for profiles app views """

    def setUp(self):
        testuser = User.objects.create_user(
            username='test_username',
            password='secret',
            email='testuser@email.com',
        )
        testuser.save()

    def tearDown(self):
        """ Test delete test user """
        User.objects.all().delete()

    def testGetProfilePage(self):
        """
        Test that a user can login, access their profile page
        (post) and verifies
        """
        self.client.login(username='test_username', password='secret')
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
