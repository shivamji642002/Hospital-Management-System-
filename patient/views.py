from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Appointment
from django import forms

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'date', 'reason']

def patient_home(request):
    return render(request, 'patient/home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})

def patient_create(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patient:patient_list')
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patient:patient_list')
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patient:patient_list')

def appointment_request(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patient:patient_home')
    return render(request, 'patient/appointment_form.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'patient/appointment_list.html', {'appointments': appointments})

def approve_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.doctor_approved = True
    appointment.save()
    return redirect('patient:appointment_list')