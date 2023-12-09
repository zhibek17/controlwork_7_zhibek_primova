from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', guest_add, name='guest_add')
]
