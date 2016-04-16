from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    picture = models.ImageField('Listing picture',
                                upload_to='listing_images/%Y-%m-%d/',
                                null=True,
                                blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', 'location', 'price')
