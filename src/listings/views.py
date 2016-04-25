from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from braces.views import LoginRequiredMixin
from django.contrib import messages
from listings.forms import ListingForm

# Create your views here.
#def index(request):
#    listings = Listing.objects.prefetch_related('user').all()
#    return render(request, "index.html", {
#        'listings': listings,
#    })

class ListingListView(ListView):
    model = Listing
    template_name = "index.html"
    queryset = Listing.objects.prefetch_related('user').distinct()

class ShowListing(DetailView):
    model = Listing
    template_name = "listings/show_listing.html"

