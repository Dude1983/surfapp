from django.conf.urls import url
from . import views
from listings.views import (ListingListView, ShowListing)

urlpatterns = [
    url(r'^$', views.ListingListView.as_view(), name='listings'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowListing.as_view(),
        name='listing_detail'),
]
