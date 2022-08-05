from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'Birthday_app/index.html')

def other(request):
    return render(request, 'Birthday_app/other.html')

def base(request):
    return render(request, 'Birthday_app/base.html')

def relative(request):
    return render(request, 'Birthday_app/relative_url_templates.html')
