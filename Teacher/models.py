from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name=models.CharField(max_length=30,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city_name=models.CharField()
    adhar_number=models.CharField()
    roll_number=models.IntegerField()
    school_name=models.CharField(max_length=40)
    Department=models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    addmission_in_school = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

