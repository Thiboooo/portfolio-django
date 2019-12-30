from django.db import models
from django.utils import timezone

# Project Model
class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    
    class Meta:
        verbose_name = "project"
        ordering = ['date']
    
    def __str__(self):
        return self.name