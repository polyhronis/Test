from django.db import models

class Lead(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    interested_in = models.ForeignKey('limo_brokerage.Limo', on_delete=models.CASCADE)

    def __str__(self):
        return self.name