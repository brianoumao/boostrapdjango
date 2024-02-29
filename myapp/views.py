from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def blogdetails(request):
    return render(request, 'blog-details.html')


def projects(request):
    return render(request, 'projects.html')


def projectsdetails(request):
    return render(request, 'project-details.html')


def services(request):
    return render(request, 'services.html')


def servicesdetails(request):
    return render(request, 'service-details.html')


def sampleinnerpage(request):
    return render(request, 'sample-inner-page.html')
