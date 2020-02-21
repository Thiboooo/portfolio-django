from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from portfolio.models import Project, UploadImg
from portfolio.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages

# Home page
def index(request):
    projects = Project.objects.all()
    formInit = contact(request)
    return render(request, 'index.html', {'last_projects' : projects, 'form' : formInit})

# Entire project
def more(request, id, slug):
    project = get_object_or_404(Project, id=id, slug=slug)
    fichiers = UploadImg.objects.filter(projet=project)
    formInit = contact(request)
    return render(request, 'layouts/project.html', {'project':project, 'fichiers':fichiers, 'form' : formInit})

# Contact form
def contact(request):
    formInit = ContactForm

    if request.method == 'POST':
        form = formInit(data=request.POST)
        if form.is_valid():
            contactName = request.POST.get('contactName', '')
            contactEmail = request.POST.get('contactEmail', '')
            message = request.POST.get('message', '')
            template = get_template('contactTemplate.txt')
            context = {'contactName': contactName,'contactEmail': contactEmail,'message': message,}
            content = template.render(context)
            email = EmailMessage("New message", content, "Portfolio Website" +'', "", headers = {'Reply-To': contactEmail })
            email.send()
            # Notification of success for the contact form
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully !')
            return redirect('index')
        messages.add_message(request, messages.ERROR, 'Your message could not be sent, please try again.')
        return redirect('index')