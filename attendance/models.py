from django.db import models
from api.models import StudentInfo


class Attendance(models.Model):
    student=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    status = models.BooleanField(choices=((True, "Present"), (False, "Absent")),default=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.date}"
