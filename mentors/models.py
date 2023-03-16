from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    categories = [
                ('Technical Skills', 'Technical Skills'),
                ('Leadership Skills', 'Leadership Skills'),
                ('Management Development', 'Management Development'),
                ('Interpersonal Skills', 'Interpersonal Skills'), ]

    name = models.CharField(max_length=60, choices=categories, null=False,
                            blank=False)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,)

    def __str__(self):
        return self.name


class Mentor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    verified = models.BooleanField(null=False, default=False)
    bio = models.CharField(max_length=1000, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    website = models.CharField(max_length=250)
    linkin = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ManyToManyField(Subcategory,
                                         related_name='subcategories',
                                         blank=True)
    joined = models.DateField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
