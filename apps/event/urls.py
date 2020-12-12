from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('spielplan/', views.events, name='events'),
    path('veranstaltung/<int:event_id>', views.event, name='event_detail'),
    path('archiv/', views.archive, name='archive'),
]