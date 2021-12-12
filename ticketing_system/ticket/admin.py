from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status', 'assigned_to')
    list_display = ('id', 'name', 'status', 'assigned_to', 'description', 'updated_at')
    search_fields = ['title', 'status']


admin.site.register(Ticket, TicketAdmin)
