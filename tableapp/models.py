from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class schedule(models.Model):
        id_user = models.IntegerField()
        date = models.DateField()
        time = models.IntegerField()
