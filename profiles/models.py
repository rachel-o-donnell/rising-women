from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ A user profile model for rendering a user's bio and other info """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=False)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    executive_summary = models.TextField(max_length=1000, null=True,
                                         blank=True)
    technical_skills = models.TextField(max_length=500, null=True, blank=True)
    leadership_skills = models.TextField(max_length=500, null=True, blank=True)
    my_achievements = models.TextField(max_length=500, null=True, blank=True)
    my_linkedin = models.CharField(max_length=250, null=True, blank=True)
    my_website = models.CharField(max_length=250, null=True, blank=True)
    my_published_articles = models.TextField(max_length=500, null=True,
                                             blank=True)
    my_mentors = models.CharField(max_length=250, null=True, blank=True)
    my_inspirational_women = models.CharField(max_length=250, null=True,
                                              blank=True)
    testimonials_given = models.TextField(max_length=500, null=True,
                                          blank=True)
    testimonials_received = models.TextField(max_length=500, null=True,
                                             blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
