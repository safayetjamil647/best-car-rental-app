from django.shortcuts import render
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def pricing(request):
    return render(request, 'home/pricing.html')
