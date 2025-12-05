"""
Created static methods and full name variables so that I can return them (the full names) to the frontend. Status is
naturally show as the raw string that is saved in the database. The status_display variable will be returned to the
frontend to show the human-readable form of the status. Same with situation with the urgency.
"""


from rest_framework import serializers

from tickets.models import Ticket, Agent, Customer, Group


class AgentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Agent
        fields = '__all__'

    @staticmethod
    def get_full_name(obj):
        return f'{obj.first_name} {obj.last_name}'


class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'

    @staticmethod
    def get_full_name(obj):
        return f'{obj.first_name} {obj.last_name}'


class GroupSerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = '__all__'

    @staticmethod
    def get_group_name(obj):
        return f'{obj.group_name}'


class TicketSerializer(serializers.ModelSerializer):
    agent_first_name = serializers.CharField(source='agent.first_name', read_only=True)
    agent_last_name = serializers.CharField(source='agent.last_name', read_only=True)

    agent_full_name = serializers.SerializerMethodField()

    customer = CustomerSerializer(read_only=True)
    group = GroupSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    urgency_display = serializers.CharField(source='get_urgency_display', read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id', 'title', 'ticket_number', 'description', 'attachment', 'created_at', 'customer', 'target_date',
            'urgency_display', 'agent_full_name', 'agent_first_name', 'agent_last_name', 'group', 'status_display'
        ]


    def get_agent_full_name(self, obj):
        if obj.agent:
            return f'{obj.agent.first_name} {obj.agent.last_name}'
        return None