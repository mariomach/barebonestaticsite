from django.db import models

# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.subject} - {self.duration}"

class Student(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    grade = models.IntegerField()
    enrollment = models.ForeignKey(Course, related_name="enrolled", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first} {self.last} , grade {self.grade} , enrolled in {self.enrollment}"
        

