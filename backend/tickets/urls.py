from django.urls import path

from .views import *

urlpatterns = [
    path('tickets/filter/', filtered_tickets, name='filtered_tickets'), # django-filter URL
]
