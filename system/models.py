from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)  
    duration = models.CharField(max_length=50)  
    fee = models.IntegerField()
    def __str__(self):
        return self.title
    
class Registration(models.Model):
    full_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    application_form = models.FileField(upload_to='applications/')

    def __str__(self):
        return self.full_name