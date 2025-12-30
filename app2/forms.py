from django import forms
from .models import Hajeri


class HajeriForm(forms.ModelForm):
   class Meta:
        model = Hajeri
        unique_together = ("Hajeri", "date") 
        ordering = ["-date"]
        fields = ['teacher', 'date', 'status'] 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})}
        
   