from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.
    """
    list_display = [
        'contact_fullname',
        'contact_email',
        'expertise_areas',
        'date',
    ]


admin.site.register(Contact, ContactAdmin)
