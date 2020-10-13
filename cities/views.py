from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Cities
from .countries import countries

from django.shortcuts import get_object_or_404

class CityCountryDetail(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # context['countries'] = list(x[1] for x in countries)
        context['countries'] =  Cities.objects.filter(admin='Seoul').last().country
        return context


class CityCountryList(ListView):
    template_name = 'home'

    def get_queryset(self):
        queryset = get_list_or_404(Cities, Iso3='UA')