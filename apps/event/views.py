from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Event


def events(request):
    """View function for event overview"""
    events = Event.objects.filter(Q(startdate__gte=timezone.now()) | Q(enddate__gte=timezone.now())).order_by('startdate')
    paginator = Paginator(events, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'event/events.html', context)


def event(request, event_id):
    """View function for event details"""
    event = get_object_or_404(Event, pk=event_id)

    if event.startdate >= timezone.now().date():
        is_current_event = True
    else:
        if event.enddate:
            if event.enddate >= timezone.now().date():
                is_current_event = True
            else:
                is_current_event = False
        else:
            is_current_event = False

    if event.bookable == False:
        is_current_event = False

    context = {
        'event': event,
        'is_current_event': is_current_event,
    }
    return render(request, 'event/event_detail.html', context)


def archive(request):
    """View function for archive overview"""
    events = Event.objects.filter(
        Q(startdate__lt=timezone.now()),
        Q(enddate__lt=timezone.now()) | Q(enddate__isnull=True)
    )
    paginator = Paginator(events, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'event/archive.html', context)