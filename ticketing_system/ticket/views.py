from django.shortcuts import render, redirect

from .filters import TicketFilter
from .models import Ticket


def index(request):
    """
    List the assigned tickets
    """
    tickets = Ticket.objects.order_by('-created_at')[:5]
    return render(request, 'index.html', {'tickets': tickets})


def ticket_by_id(request, ticket_id):
    """
    List the details of ticket
    """
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticket_by_id.html', {'ticket': ticket})


def change_ticket_status(request, ticket_id):
    """
    Update the status of ticket
    """
    success_url = '/'
    ticket_obj = Ticket.objects.get(pk=ticket_id)
    ticket_obj.status = "COMPLETED"
    ticket_obj.save()
    return redirect(success_url)


def search(request):
    """
    Filter for tickets
    """
    ticket_list = Ticket.objects.all()
    ticket_filter = TicketFilter(request.GET, queryset=ticket_list)
    return render(request, 'index.html', {'filter': ticket_filter})
