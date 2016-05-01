from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListingListView.as_view(), name='listings'),
    # url(r'^(?P<slug>[\w\-]+)$', views.ShowListing.as_view(), name='listing_detail'),
    url(r'^(?P<slug>[\w\-]+)$', views.listing_detail, name='listing_detail'),
    url(r'^create/$', views.ListingCreate.as_view(), name='create'),
]
