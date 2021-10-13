from django.db import models
from django.utils import timezone

# Project model
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Project title")
    slug = models.SlugField(max_length=100, null=True)
    image = models.ImageField(upload_to='gallery', null=True, verbose_name="Project\'s Image")
    labels = models.CharField(max_length=100, null=True, verbose_name="Languages used")
    desc = models.TextField(null=True, verbose_name="Project description")
    github = models.CharField(max_length=200, null=True, blank=True, verbose_name="GitHub URL")
    demo = models.CharField(max_length=200, null=True, blank=True, verbose_name="Demo URL")
    date = models.DateTimeField(default=timezone.now, verbose_name="Day of publication")
    
    class Meta:
        verbose_name = "Project"
        ordering = ['-date']
    
    def __str__(self):
        return self.name

# Upload file in Django Admin
class UploadImg(models.Model):
    projet = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, verbose_name="Picture name")
    link = models.ImageField(upload_to='gallery', null=True, verbose_name="Picture")
    
    class Meta:
        verbose_name = "Picture"
        ordering = ['-name']

    def __str__(self):
        return self.name

# Contact model
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(max_length=100, verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    date = models.DateTimeField(default=timezone.now, verbose_name="Day of publication")

    class Meta:
        verbose_name = "Contact"
        ordering = ['-date']

    def __str__(self):
        return self.name