from django.contrib import admin
from .models import Mentor, Category, Subcategory

# Register your models here.


@admin.register(Mentor)
class Mentor(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'subcategory')
    search_fields = ['category', 'subcategory', ]
    list_display = ('name', 'verified', 'expertise', 'bio', 'image',
                    'website', 'linkedin', 'category',
                    'joined',)
    list_editable = ['verified']


@admin.register(Category)
class Mentor(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Subcategory)
class Mentor(admin.ModelAdmin):
    list_display = ('name',)
