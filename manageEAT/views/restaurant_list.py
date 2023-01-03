from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from manageEAT.models.restaurant import Restaurant


class RestaurantList(LoginRequiredMixin, ListView):
    model = Restaurant
    template_name = "restaurant/restaurant_list.html"
