import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField

from utils.helpers import create_random_ticket_number


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    ticket_number = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='tickets/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='ticket')

    # planning
    target_date = models.DateField()
    urgency = models.CharField(
        max_length=30,
        choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High'), ('critical', 'Critical')],
    )

    # processing
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, related_name='processing')
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, related_name='processing')
    status = models.CharField(
        max_length=30,
        choices=[
            ('open', 'Open'), ('closed', 'Closed'), ('assigned', 'Assigned'), ('appointment_set', 'Appointment Set')
        ]
    )

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = create_random_ticket_number()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['ticket_number']

    def __str__(self):
        return self.title


class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = CharField(max_length=15)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, related_name='agents')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = CharField(max_length=15)
    office = models.ForeignKey('Office', on_delete=models.SET_NULL, null=True, related_name='customers')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='customers')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Office(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    office_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.office_name}'


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.department_name}'


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name


class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.ticket.title} - {self.comment}'
