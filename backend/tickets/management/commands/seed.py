import random
import uuid
from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

from tickets.models import (
    Ticket, Agent, Customer, Office, Department, Group, Comments
)

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with test data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Deleting existing data..."))
        Ticket.objects.all().delete()
        Agent.objects.all().delete()
        Customer.objects.all().delete()
        Office.objects.all().delete()
        Department.objects.all().delete()
        Group.objects.all().delete()
        Comments.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Creating Offices..."))
        offices = [
            Office.objects.create(office_name="New York"),
            Office.objects.create(office_name="Chicago"),
            Office.objects.create(office_name="Los Angeles"),
        ]

        self.stdout.write(self.style.SUCCESS("Creating Departments..."))
        departments = [
            Department.objects.create(department_name="HR"),
            Department.objects.create(department_name="IT"),
            Department.objects.create(department_name="Finance"),
        ]

        self.stdout.write(self.style.SUCCESS("Creating Groups..."))
        groups = [
            Group.objects.create(group_name="Support"),
            Group.objects.create(group_name="Field Team"),
            Group.objects.create(group_name="Escalations"),
        ]

        self.stdout.write(self.style.SUCCESS("Creating Agents + Users..."))
        agents = []
        for i in range(5):
            user = User.objects.create_user(
                username=f"agent{i}",
                email=fake.email(),
                password="password123"
            )

            agent = Agent.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=user.email,
                phone_number=fake.numerify("###-###-####"),
                group=random.choice(groups),
                user=user
            )
            agents.append(agent)

        self.stdout.write(self.style.SUCCESS("Creating Customers + Users..."))
        customers = []
        for i in range(10):
            user = User.objects.create_user(
                username=f"customer{i}",
                email=fake.email(),
                password="password123"
            )

            customer = Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=user.email,
                phone_number=fake.numerify("###-###-####"),
                office=random.choice(offices),
                department=random.choice(departments),
                user=user
            )
            customers.append(customer)

        self.stdout.write(self.style.SUCCESS("Creating Tickets..."))
        tickets = []
        urgency_choices = ["low", "moderate", "high", "critical"]
        status_choices = ["open", "closed", "assigned", "appointment_set"]

        for i in range(20):
            ticket = Ticket.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                customer=random.choice(customers),
                agent=random.choice(agents),
                group=random.choice(groups),
                target_date=timezone.now().date() + timedelta(days=random.randint(1, 21)),
                urgency=random.choice(urgency_choices),
                status=random.choice(status_choices),
            )
            tickets.append(ticket)

        self.stdout.write(self.style.SUCCESS("Creating Comments..."))
        for ticket in tickets:
            for _ in range(random.randint(1, 3)):
                Comments.objects.create(
                    ticket=ticket,
                    comment=fake.sentence(),
                    commenter=random.choice(User.objects.all())
                )

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))
