"""
This is used to create the filter-set for the APIs. Tickets will be filtered by:
 - target_date
 - id (ticket uuid)
 - ticket number
 - urgency
 - status
 - group
 - agent
 - date ranges (start, end)
"""
import django_filters

from .models import Ticket


class TicketFilter(django_filters.FilterSet):
    start = django_filters.DateFilter(field_name="target_date", lookup_expr="gte")
    end = django_filters.DateFilter(field_name="target_date", lookup_expr="lte")

    class Meta:
        model = Ticket
        fields = [
            'id','target_date', 'ticket_number', 'status', 'urgency', 'agent', 'group', 'customer'
        ]