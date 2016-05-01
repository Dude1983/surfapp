from django.contrib import admin
from listings.models import Listing


class ListingAdmin(admin.ModelAdmin):
    model = Listing
    list_display = ('title', 'location', 'slug', 'price', 'user', 'status')
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        queryset.update(status='published')

    def unpublish(self, request, queryset):
        queryset.update(status='draft')


    publish.short_description = "Publish Listings"
    unpublish.short_description = "Unpublish Listings"


# Register your models here.
admin.site.register(Listing, ListingAdmin)
