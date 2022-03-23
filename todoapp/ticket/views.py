from dataclasses import fields
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Ticket
# Create your views here.
class CreateTicket(CreateView):
    model = Ticket
    fields = ['ticket_name','ticket_description']
    template_name = 'ticket/create_ticket.html'
    success_url = '/ticket/view/'

