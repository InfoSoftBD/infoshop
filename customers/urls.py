from django.urls import path
from . import views
app_name = 'customers'

urlpatterns = [	
	path('', views.CustomerList.as_view(), name='customer_list'),
	path('<slug>/', views.CustomerDetails.as_view(), name='customer_detail'),
	
]