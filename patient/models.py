from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_approved = models.BooleanField(default=False)
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.date}"