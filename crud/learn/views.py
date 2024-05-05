from django.shortcuts import render
from django.views.generic import ListView
from .models import customers


# Create your views here.
class ListCustomers(ListView):

    model=customers
    template_name='customer_list.html'
    context_object_name="articles"

 
 