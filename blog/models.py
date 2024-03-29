from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=64)
    pub_date = models.DateField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
