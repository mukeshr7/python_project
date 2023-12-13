from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
