from django.db import models

class StudentInfo(models.Model):
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name=models.CharField(max_length=30,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city_name=models.CharField()
    roll_number=models.IntegerField(default=101)
    school_name=models.CharField(max_length=40)
    class_name=models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    year_in_school = models.CharField(null=True, blank=True)

