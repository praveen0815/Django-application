from django.db import models

class Student(models.Model):
    sid = models.CharField(max_length=200)
    sname = models.CharField(max=250)
    age = models.IntegerField(default=20)
     
    def __str__(self):
        return self.sname
    