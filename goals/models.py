from django.db import models
from shortuuid.django_fields import ShortUUIDField

class Goal(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.TextField(max_length=50)
    completed = models.BooleanField()
    date = models.DateField()
