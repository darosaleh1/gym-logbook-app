from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_custom = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rest_period = models.IntegerField(help_text="Rest period in seconds")
    
    class Meta:
        unique_together = ['name', 'created_by']
