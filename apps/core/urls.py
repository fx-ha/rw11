from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('reservierung/', views.contact, name='contact'),
    path('impressum/', views.imprint, name='imprint'),
    path('datenschutz/', views.privacy_policy, name='privacy_policy'),
    path('offline/', views.offline, name='offline'),
]