from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from portfolio.models import Project

# Home page
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'last_projects' : projects})

# Entire project
def more(request, id, slug):
    project = get_object_or_404(Project, id=id, slug=slug)
    return render(request, 'layouts/project.html', {'project':project})