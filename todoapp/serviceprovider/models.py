from django.db import models

# Create your models here.
class ServiceProvider(models.Model):
    name = models.CharField(max_length=50)
    address =  models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone =  models.CharField(max_length=50)
    website =  models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now='True')
    class Meta:
        db_table = 'service_provider'