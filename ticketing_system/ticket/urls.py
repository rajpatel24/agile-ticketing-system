from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path('change_ticket_status/<int:ticket_id>', views.change_ticket_status, name='change_ticket_status'),
]
