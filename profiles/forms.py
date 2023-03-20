from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('executive_summary', 'technical_skills',
                  'leadership_skills', 'my_achievements',
                  'my_linkedin', 'my_website', 'my_published_articles',
                  'my_mentors', 'my_inspirational_women', 'testimonials_given',
                  'testimonials_received')
