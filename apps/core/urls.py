from django.urls import path, re_path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('reservierung/', views.contact, name='contact'),
    path('impressum/', views.imprint, name='imprint'),
    path('datenschutz/', views.privacy_policy, name='privacy_policy'),

    # pwa
    path('offline/', views.offline, name='offline'),
    # The service worker cannot be in /static because its scope will be limited to /static.
    # Since we want it to have a scope of the full application, we rely on this TemplateView
    # trick to make it work. re_path for regex to avoid trailing slash.
    re_path(r'^sw.js', views.ServiceWorkerView.as_view(), name='sw.js'),
]