from django.shortcuts import render, reverse
from django.http.request import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Organisation


def index(request: HttpRequest):
    return render(request, 'base.html')


class CreateOrganisation(CreateView, LoginRequiredMixin):
    model = Organisation
    template_name = 'website/organisation/form.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListOrganisation(ListView, LoginRequiredMixin):
    model = Organisation
    template_name = 'website/organisation/list.html'

    def get_queryset(self):
        return Organisation.objects.filter(user=self.request.user)

