from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=20)
    secondName = models.CharField(max_length=20)
    year = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.firstName} - {self.secondName} | {self.year} | {self.phone}'