from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from manageEAT.models.restaurant import Restaurant


class QuestionListView(LoginRequiredMixin, ListView):
    model = Restaurant
    template_name = "restaurant/dashboard.html"