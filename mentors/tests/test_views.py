from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from mentors.models import Mentor, Category, Subcategory


class MentorDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a user and log them in
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a Category instance
        category = Category.objects.create(name='Test Category')

        # Create a Subcategory instance and associate it
        # with the Category instance
        subcategory = Subcategory.objects.create(name='Test Subcategory',
                                                 category=category)

        # Create a Mentor instance and associate it with the
        # Category and Subcategory instances
        self.mentor = Mentor.objects.create(
            name='Test Mentor',
            expertise='Test Expertise',
            bio='Test Bio',
            category=category,
            joined=timezone.now(),
        )
        self.mentor.subcategory.add(subcategory)

    def test_mentor_detail_view_invalid_slug(self):
        url = reverse('mentor-detail', kwargs={'mentor_slug': 'invalid-slug'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
