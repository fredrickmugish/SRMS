from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)  
    duration = models.CharField(max_length=50)  
    fee = models.IntegerField()
    def __str__(self):
        return self.title