from django.db import models
from django.utils import timezone
from django.urls import reverse

class CustomerInfo(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	slug = models.SlugField(max_length=100, unique='email')
	telephone = models.CharField(max_length=20)
	address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=20)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		return reverse('customer:customer_detail',args=[self.slug])
		
	class Meta:
		ordering = ('last_name',)
		def __str__(self):
			return self.last_name