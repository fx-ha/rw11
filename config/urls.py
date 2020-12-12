"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.event import views as eventviews
from apps.team import views as teamviews

urlpatterns = [
    path('admin/', admin.site.urls),

    # core
    path('', include('apps.core.urls', namespace='core')),

    # event
    path('spielplan/', eventviews.events, name='events'),
    path('veranstaltung/<int:event_id>', eventviews.event, name='event_detail'),
    path('archiv/', eventviews.archive, name='archive'),

    # team
    path('team/', teamviews.team, name='team'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "RW11"