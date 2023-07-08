from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=75)
    lastname = models.CharField(max_length=75)
    age = models.SmallIntegerField()
    profession = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return f"{self.lastname}-{self.name}"
# Create your models here.

