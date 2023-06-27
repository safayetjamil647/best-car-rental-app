from django.shortcuts import render

# Create your views here.
def pricing(request):
    return render(request, 'pricing/pricing.html')

def add_pricing(request):
    return render(request, 'pricing/pricing.html')

def remove_pricing(request):
    return render(request, 'pricing/pricing.html')

def update_pricing(request):
    return render(request, 'pricing/pricing.html')