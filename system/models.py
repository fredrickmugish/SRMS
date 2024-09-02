from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)  
    duration = models.CharField(max_length=50)  
    fee = models.IntegerField()

    def __str__(self):
        return self.title
    
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    full_name = models.CharField(max_length=255, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    application_form = models.FileField(upload_to='applications/')

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('LIPA KWA SIMU', 'LIPA KWA SIMU'),
        ('TIGO PESA', 'TIGO PESA'),
        ('AIRTEL MONEY', 'AIRTEL MONEY'),
        ('NMB', 'NMB'),
    ]

    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='payments')
    amount = models.IntegerField()
    date = models.DateField()
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    is_completed = models.BooleanField(default=False)  # Track if payment is completed

    def __str__(self):
        return f'{self.registration.full_name} - {self.amount} on {self.date}'

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
