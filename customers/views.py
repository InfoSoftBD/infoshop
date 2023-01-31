from django.shortcuts import render
from .models import CustomerInfo
from django.views.generic import ListView, DetailView


class CustomerList(ListView):
	queryset = CustomerInfo.objects.all()
	context_object_name = 'customers'
	template_name = 'customer_list.html'

class CustomerDetails(DetailView):
	model = CustomerInfo
	context_object_name = 'customer'
	template_name = 'customer_details.html'


	

	

