from django import template

register = template.Library()

from ..models import Listing

@register.simple_tag
def total_listings():
    return Listing.published.count()
