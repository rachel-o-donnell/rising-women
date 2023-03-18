from django.test import TestCase
from django.utils import timezone
from mentors.models import Mentor, Category, Subcategory


class MentorModelTestCase(TestCase):

    def setUp(self):
        # Create a Category instance to associate with Subcategory instances
        category = Category.objects.create(name='Test Category')

        # Create two Subcategory instances and associate them with the Category
        subcategory1 = Subcategory.objects.create(name='Test Subcategory 1',
                                                  category=category)
        subcategory2 = Subcategory.objects.create(name='Test Subcategory 2',
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
        self.mentor.subcategory.add(subcategory1)
        self.mentor.subcategory.add(subcategory2)

    def test_mentor_has_name(self):
        # Test that the Mentor has a name
        self.assertEqual(str(self.mentor), 'Test Mentor')

    def test_mentor_has_expertise(self):
        # Test that the Mentor has an expertise
        self.assertEqual(self.mentor.expertise, 'Test Expertise')

    def test_mentor_has_bio(self):
        # Test that the Mentor has a bio
        self.assertEqual(self.mentor.bio, 'Test Bio')

    def test_mentor_has_category(self):
        # Test that the Mentor has a category
        self.assertEqual(self.mentor.category.name, 'Test Category')

    def test_mentor_has_subcategories(self):
        # Test that the Mentor has the expected subcategories
        subcategory_names = [
            subcategory.name for subcategory in self.mentor.subcategory.all()
        ]
        self.assertCountEqual(subcategory_names,
                              ['Test Subcategory 1', 'Test Subcategory 2'])

    def test_mentor_has_joined_date(self):
        # Test that the Mentor has a joined date
        self.assertIsNotNone(self.mentor.joined)

    def test_mentor_has_slug(self):
        # Test that the Mentor has a slug after saving
        mentor = Mentor.objects.create(
            name='Test Mentor 2',
            expertise='Test Expertise 2',
            bio='Test Bio 2',
            category=Category.objects.first(),
            joined=timezone.now(),
        )
        self.assertIsNotNone(mentor.slug)
