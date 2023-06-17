from django.shortcuts import render

def booking(request):
    return render(request, 'booking/index.html')

def routes(request):
    return render(request, 'routes/index.html')