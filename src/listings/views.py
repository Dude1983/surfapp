from django.shortcuts import render
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.prefetch_related('user').all()
    return render(request, "index.html", {
        'listings': listings,
    })
