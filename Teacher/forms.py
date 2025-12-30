from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    Department = forms.ChoiceField(
        choices=(('', "Select Department"),('Science', "Science"),('Art', "Art"),('Commerce','Commerece'),('other','Other')),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    city_name =forms.ChoiceField(
        choices=(('','select city'),('Pune','Pune'),('Mumbai','Mumbai'),('Hyderabad','Hyderabad'),('surat','Surat')),
        widget=forms.Select(attrs={'class': 'form-select'})

    )

    class Meta:
        model= Teacher
        fields = "__all__"
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
            'adhar_number':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter aadhar card'
            }),
            # 'city_name': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Enter city'
            # }),
            'roll_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number'
            }),
            'school_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter school name'
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
            'addmission_in_school': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter year in school'
            }),
        }
        labels={
            'first_name': 'FIRST NAME',
            'last_name': 'LAST NAME',
            'date_of_birth':'DATE OF BIRTH',
            'city_name':'CITY NAME',
            'adhar_number':'ADHAR NUMBER',
            'roll_number':'ROLL NUMBER',
            'school_name':'SCHOOL NAME',
            # 'Department':'DEPARTMENT',
            'email':'EMAIL',
            'phone_number':'PHONE NUMBER',
            'address':'ADDRESS',
            'addmission_in_school':'ADDMISSION IN SCHOOL'
        }
        
