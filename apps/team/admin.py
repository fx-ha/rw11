from django.contrib import admin

from .models import TeamMember


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = 'last_name', 'first_name', 'active'

admin.site.register(TeamMember, TeamMemberAdmin)