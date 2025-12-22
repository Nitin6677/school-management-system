from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):
   class Meta:
        model = Attendance
        unique_together = ("student", "date")  # one record per day
        ordering = ["-date"]
        fields = ['student', 'date', 'status'] 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})}
        
   
   def __init__(self, *args, **kwargs):
        self.filter = kwargs.pop("filter", False) 
        super().__init__(*args, **kwargs)

        if self.filter:
            for field in self.fields.values():
                field.required = False
                field.widget.attrs.pop("required", None)
