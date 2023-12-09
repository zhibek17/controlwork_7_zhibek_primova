from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/', guest_add, name='guest_add'),
    path('update/<int:pk>/', guest_update, name='guest_update'),
    path('delete/<int:pk>/', guest_delete, name='guest_delete'),
]
