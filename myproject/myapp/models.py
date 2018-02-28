from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	telephone=models.CharField(max_length=15)
	dob=models.DateField(blank=True,null=True)
	credit_amount=models.DecimalField(max_digits=15, decimal_places=2)
	memo=models.CharField(max_length=500)

class Car(models.Model):
	model=models.CharField(max_length=100)
	detail=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=10,decimal_places=2)

class Rent(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	car=models.ForeignKey(Car, on_delete=models.CASCADE)
	fee=models.DecimalField(max_digits=10,decimal_places=2)
	start_datetime=models.DateTimeField()
	stop_datetime=models.DateTimeField()

class Return(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	car=models.ForeignKey(Car, on_delete=models.CASCADE)
	#fee=models.DecimalField(max_digits=10,decimal_places=2)
	#start_datetime=models.DateTimeField()
	return_datetime=models.DateTimeField()
		
