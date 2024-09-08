from django.urls import path
from . import views
from .views import process_date, home

urlpatterns = [
    path('', home, name='home'),
    path('date', process_date, name='process_date'),
]