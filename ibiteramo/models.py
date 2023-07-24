from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ibiteramo(models.Model):
    id = models.BigAutoField(primary_key=True)
    ahobizobera = models.CharField(max_length=15)
    debut = models.TimeField(max_length=15)
    fin = models.TimeField(max_length=15)
    ibeyi = models.PositiveIntegerField()
    date = models.DateTimeField()

class Meta():
       verbose_name_plural = "Ibiteramo"

def __str__(self):
       return f"{self.debut} -  {self.fin} - {self.Ahobizobera} isaha {self.date}"

class Itike(models.Model):
    id = models.BigAutoField(primary_key=True)
    ibiteramo = models.ForeignKey(Ibiteramo, null=False, on_delete=models.PROTECT)
    place = models.SmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    uwayimuhaye = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta():
       verbose_name_plural = "Itike"
       