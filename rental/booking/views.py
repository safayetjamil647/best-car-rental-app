from django.shortcuts import render, redirect,get_object_or_404
from .forms import BookingForm
from .models import Bookings
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings:booking_list')
    else:
        form = BookingForm()
    
    return render(request, 'booking/add_booking.html', {'form': form})

def list_booking(request):
    bookings = Bookings.objects.all()
    return render(request, 'booking/list_booking.html', {'bookings': bookings})

def detail_booking(request, booking_id):
    booking = get_object_or_404(Bookings, pk=booking_id)
    return render(request, 'booking/detail_booking.html', {'booking': booking})

def remove_booking(request, booking_id):
    booking = get_object_or_404(Bookings, pk=booking_id)
    booking.delete()
    return redirect('bookings:booking_list')