from django.db import models
from django.utils import timezone

# Project model
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du projet")
    slug = models.SlugField(max_length=100,null=True)
    desc = models.TextField(null=True, verbose_name="Description du projet")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    
    class Meta:
        verbose_name = "Projet"
        ordering = ['date']
    
    def __str__(self):
        return self.name