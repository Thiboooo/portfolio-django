from django.db import models
from django.utils import timezone

# Project model
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du projet")
    slug = models.SlugField(max_length=100, null=True)
    image = models.CharField(max_length=500, null=True, verbose_name="Image du projet")
    labels = models.CharField(max_length=100, null=True, verbose_name="Langages utilisés")
    desc = models.TextField(null=True, verbose_name="Description du projet")
    github = models.CharField(max_length=200, null=True, blank=True, verbose_name="Lien GitHub")
    demo = models.CharField(max_length=200, null=True, blank=True, verbose_name="Lien Démonstration")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    
    class Meta:
        verbose_name = "Projet"
        ordering = ['-date']
    
    def __str__(self):
        return self.name

# Upload file in Django Admin
class UploadFile(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Nom de l'image")
    specifications = models.ImageField(upload_to='portfolio/static/img', null=True, verbose_name="Image")
    
    class Meta:
        verbose_name = "Fichier"

    def __str__(self):
        return self.name