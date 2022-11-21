from django.urls import path
from . import views

app_name = 'dashboard'


urlpatterns = [
    path('', views.home, name='home'),
    path('transactions/', views.transactions, name='transactions'),
    path('profile/', views.profile, name='profile'),
]