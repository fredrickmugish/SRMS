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
    
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('LIPA KWA SIMU', 'LIPA KWA SIMU'),
        ('TIGO PESA', 'TIGO PESA'),
        ('AIRTEL MONEY', 'AIRTEL MONEY'),
        ('NMB', 'NMB'),
    ]

    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    is_completed = models.BooleanField(default=False)  # Track if payment is completed

    def __str__(self):
        return f'{self.registration.full_name} - {self.amount} on {self.date}'