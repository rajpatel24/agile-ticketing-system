from django.db import models
from users.models import User


class Ticket(models.Model):
    TICKET_STATUS = [
        ('DRAFT', 'Draft'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('ARCHIVED', 'Archived'),

    ]
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField('Description')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TICKET_STATUS)
    file = models.FileField(upload_to="files/%Y/%m/%d")
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
