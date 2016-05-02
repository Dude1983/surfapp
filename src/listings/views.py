from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import generic
import redis
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from braces.views import LoginRequiredMixin
from django.contrib import messages
from listings.forms import ListingForm

# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)

def listing_detail(request, slug):
    listing = get_object_or_404(Listing, slug=slug)

    try:
        r.ping
        # increment total image views by 1
        total_views = r.incr('listing:{}:views'.format(listing.slug))
        return render(request, 'listings/show_listing.html', {'section': 'listings', 'listing': listing, 'total_views': total_views})
    except redis.ConnectionError:
        return render(request, 'listings/show_listing.html', {'section': 'listings', 'listing': listing })

class ListingListView(ListView):
    model = Listing
    paginate_by = 3
    template_name = "index.html"
    queryset = Listing.published.prefetch_related('user')


# class ShowListing(DetailView):
#     model = Listing
#     template_name = "listings/show_listing.html"
#
#     def get_context_data(self, **kwargs):
#         listing = Listing.get(id=id, slug=slug)



@method_decorator(login_required(), name='dispatch')
class ListingCreate(SuccessMessageMixin, CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listings_form.html"
    success_url = '/'
    success_message = "Thank You. Your listing will be reviewed and approved within 24 hours."

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        return super(ListingCreate, self).form_valid(form)
