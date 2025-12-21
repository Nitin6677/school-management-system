from django import forms
from .models import StudentInfo

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'city_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city'
            }),
            'roll_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number'
            }),
            'school_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter school name'
            }),
            'class_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter class'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
                'rows': 3
            }),
            'year_in_school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter year in school'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.filter = kwargs.pop("filter", False) 
        super().__init__(*args, **kwargs)

        if self.filter:
            for field in self.fields.values():
                field.required = False
                field.widget.attrs.pop("required", None)
