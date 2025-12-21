from django.db import models
from api.models import StudentInfo

class Attendance(models.Model):
    student=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.BooleanField(choices=((True, "Present"), (False, "Absent")),default=True)
    date = models.DateField()
