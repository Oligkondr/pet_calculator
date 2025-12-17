from django.db import models


# Create your models here.
class Calculation(models.Model):
    OPERATION_CHOICES = [
        ('add', 'Addition'),
        ('sub', 'Subtraction'),
        ('mul', 'Multiplication'),
        ('div', 'Division'),
    ]

    number1 = models.FloatField()
    number2 = models.FloatField()
    operation = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    result = models.FloatField(null=True, blank=True)
    error = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
