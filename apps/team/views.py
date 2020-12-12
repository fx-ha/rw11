from django.shortcuts import render

from .models import TeamMember


def team(request):
    """View function for team"""
    team_members = TeamMember.objects.all()
    context = {
        'team_members': team_members,
    }
    
    return render(request, 'event/team.html', context)