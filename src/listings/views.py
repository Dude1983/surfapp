from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
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
    queryset = Listing.objects.prefetch_related('user').filter(approved=True)

class ShowListing(DetailView):
    model = Listing
    template_name = "listings/show_listing.html"

@method_decorator(login_required(), name='dispatch')
class ListingCreate(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listings_form.html"
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        return super(ListingCreate, self).form_valid(form)

