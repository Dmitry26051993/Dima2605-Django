from django.db import models
class Group(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.lastname}'
# Create your models here.
