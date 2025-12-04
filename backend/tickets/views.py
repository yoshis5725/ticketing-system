from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tickets.filters import TicketFilter
from tickets.models import Ticket
from tickets.serializers import TicketSerializer


@api_view(['GET'])
def filtered_tickets(request):
    filterset = TicketFilter(request.GET, queryset=Ticket.objects.all())

    if not filterset.is_valid():
        return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = TicketSerializer(filterset.qs, many=True)
    return Response(serializer.data)
