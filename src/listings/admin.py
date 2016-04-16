from django.contrib import admin
from listings.models import Listing


class ListingAdmin(admin.ModelAdmin):
    model = Listing
    list_display = ('title', 'location', 'slug', 'price', 'user')
    prepopulated_fields = {'slug': ('title', 'location',)}

# Register your models here.
admin.site.register(Listing, ListingAdmin)
