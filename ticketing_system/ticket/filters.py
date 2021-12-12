from .models import Ticket
import django_filters


class TicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = {'status', 'created_at', 'updated_at'}
