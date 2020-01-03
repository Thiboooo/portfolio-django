from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from portfolio.models import Project, UploadFile
from portfolio.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages

# Home page
def index(request):
    projects = Project.objects.all()
    formInit = ContactForm

    # Contact form
    if request.method == 'POST':
        form = formInit(data=request.POST)
        if form.is_valid():
            contactName = request.POST.get('contactName', '')
            contactEmail = request.POST.get('contactEmail', '')
            message = request.POST.get('message', '')
            template = get_template('contactTemplate.txt')
            context = {'contactName': contactName,'contactEmail': contactEmail,'message': message,}
            content = template.render(context)
            email = EmailMessage("Nouveau message", content, "Portfolio Website" +'', ['contact@sotramp.io'], headers = {'Reply-To': contactEmail })
            email.send()
            # Notification of success for the contact form
            messages.add_message(request, messages.SUCCESS, 'Votre message a été envoyé avec succès !')
            return redirect('index')
        messages.add_message(request, messages.ERROR, 'Votre message n\'a pas pu être envoyé, veuillez réessayez.')
        return redirect('index')

    return render(request, 'index.html', {'last_projects' : projects, 'form' : formInit})

# Entire project
def more(request, id, slug):
    project = get_object_or_404(Project, id=id, slug=slug)
    return render(request, 'layouts/project.html', {'project':project})

# File page (test)
def fichier(request):
    fichiers = UploadFile.objects.all()
    return render(request, 'layouts/fichiers.html', {'fichiers':fichiers})