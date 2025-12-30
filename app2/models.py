from django.db import models
from Teacher.models import Teacher

class Hajeri(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    status = models.BooleanField(choices=((True, "Present"), (False, "Absent")),default=True)
    date = models.DateField()


    def __str__(self):
        return f"{self.teacher} - {self.date}"