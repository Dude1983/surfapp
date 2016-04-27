from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Listing(models.Model):
    approved = models.BooleanField(default=False, blank=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='get_slug_name', unique_with='pub_date')
    picture = models.ImageField('Listing picture',
                                upload_to='listing_images/%Y-%m-%d/',
                                null=True,
                                blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateTimeField('date created', default=datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_slug_name(self):
        return self.title + '-' + self.location

    def get_absolute_url(self):
        return reverse('listing-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', 'location', 'description', 'price', 'picture')
