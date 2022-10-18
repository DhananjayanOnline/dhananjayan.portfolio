from django.shortcuts import redirect, render

from my_Site.models import MyWorks, Contact, Resume

# Create your views here.

def project(request):

    projects = MyWorks.objects.all()
    resume = Resume.objects.get(id=1)
    context = {
        'projects':projects,
        'resume':resume,
    }
    return render(request, 'index.html', context)


def project_details(request, project_id):
    project = MyWorks.objects.get(id = project_id)
    context = {
        'project':project,
    }
    return render(request, 'portfolio-details.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        crec = Contact(name = name, email=email, subject=subject, message=message)
        crec.save()
    return render(request, 'index.html')

