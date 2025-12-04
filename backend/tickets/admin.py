from django.contrib import admin

from .models import *


admin.site.register(Office)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Customer)

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'group']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment', 'commenter']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'ticket_number', 'customer']
