```python
from django.db import models

class Limo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='limos/')
    availability = models.BooleanField(default=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tracking(models.Model):
    limo = models.ForeignKey(Limo, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=200)

    def __str__(self):
        return f'Tracking for {self.limo.name}'
```