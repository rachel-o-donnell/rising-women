from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=100, null=False,
                                        blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    areas_of_expertise = models.CharField(max_length=250, null=False, blank=False)
    website = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=500, null=False, blank=False)
    why_you_want_to_become_a_mentor = models.TextField(max_length=500, null=False, blank=False)
    # automatically create and add date when a contact is sent
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
