from django.db import models


class Contact(models.Model):
    contact_fullname = models.CharField(max_length=100, null=False,
                                        blank=False)
    contact_email = models.EmailField(max_length=100, null=False, blank=False)
    expertise_areas = models.CharField(max_length=250, null=False, blank=False)
    contact_website = models.CharField(max_length=100, null=True, blank=True)
    contact_linkedin = models.CharField(max_length=100, null=True, blank=True)
    contact_bio = models.TextField(max_length=500, null=False, blank=False)
    why_mentor = models.TextField(max_length=500, null=False, blank=False)
    # automatically create and add date when a contact is sent
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
