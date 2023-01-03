from django.views.generic import DetailView

from manageEAT.models.restaurant import Restaurant


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = "restaurant/restaurant_detail.html"
