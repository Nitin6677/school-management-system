from django.shortcuts import render
from .models import Attendance

def attendance_view(request):
    template_name='attendance/attendance.html'
    context={}
    return render(request,template_name,context)
