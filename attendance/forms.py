from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
   class Meta:
        model = Attendance
        unique_together = ("student", "date")  # one record per day
        ordering = ["-date"]

def __str__(self):
        return f"{self.student} - {self.date}"