from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


# Create your models here.
class Doctor(models.Model):
  name = models.CharField(max_length=255)
  mode = ArrayField(models.CharField(max_length=120))
  specialty = models.CharField(max_length=255) #models.ForeignKey(Specialty, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  idioms = ArrayField(models.CharField(max_length=120))
  years_experience = models.IntegerField()
  university = models.CharField(max_length=255)
  description = models.TextField()
  url_map = ArrayField(models.FloatField())  # [latitud, longitud]
  photo = models.URLField()

  class Meta:
    db_table = "doctor"

  def __str__(self):
        return self.name

class Specialty(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)

  class Meta:
    db_table = "specialty"