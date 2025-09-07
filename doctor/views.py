from django.shortcuts import render, redirect, get_object_or_404
from patient.models import Appointment

# Create your views here.
def doctor_home(request):
    return render(request, 'doctor/home.html')

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'doctor/appointments.html', {'appointments': appointments})


def approve_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.doctor_approved = True
    appointment.save()
    return redirect('doctor:appointment_list')