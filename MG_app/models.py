from django.db import models

# Create your models here.

class contectus(models.Model):

    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name