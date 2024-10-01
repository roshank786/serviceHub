from django.db import models

# Create your models here.


class CustomerModel(models.Model):

        name = models.CharField(max_length=200)

        phone = models.PositiveIntegerField(unique=True)

        email = models.EmailField(unique=True)

        vehicle_number = models.CharField(max_length=200,unique=True)

        running_kms = models.PositiveIntegerField()

        work_status_choices = (("pending":"pending"),
                               ("in progress":"in progress"),
                               ("completed":"completed"))

        work_status = models.CharField(max_length=200,choices=work_status_choices,default="pending")

        created_date = models.DateTimeField(auto_now_add=True)

    
class WorkModel(models.Model):
        
        customer_object = models.ForeignKey(CustomerModel,on_delete=models.CASCADE)

        description = models.CharField(max_length=200)

        amount = models.FloatField()