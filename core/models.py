from django.db import models

# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=80, blank=True, null=True)
    service_description = models.CharField(max_length=200, blank = True, null = True)
    service_icon = models.ImageField(upload_to='images/uploads/')
    service_link_name = models.CharField(max_length=80, blank = True, null = True)


    def __str__(self):
        return self.service_name