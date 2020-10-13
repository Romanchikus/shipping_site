from django.urls import path
from .views import CityCountryDetail

urlpatterns = [
    path('', CityCountryDetail.as_view(), name='country'),
]