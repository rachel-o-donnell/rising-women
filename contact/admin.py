from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.
    """
    list_display = [
        'fullname',
        'email',
        'areas_of_expertise',
        'website',
        'linkedin',
        'bio',
        'why_you_want_to_become_a_mentor',
        'date',
    ]


admin.site.register(Contact, ContactAdmin)
