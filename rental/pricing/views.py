from django.shortcuts import render, redirect, get_object_or_404
from .forms import PricingForm

from .models import Pricing
# Create your views here.
def add_pricing(request):

    if request.method == 'POST':
        form = PricingForm(request.POST)
        if form.is_valid():
            pricing = form.save(commit=False)
            pricing.save()
            return redirect('pricing:list_pricing')
    else:
        form = PricingForm()

    return render(request, 'pricing/add_pricing.html', {'form': form})

def detail_pricing(request, pricing_id):
    pricing = get_object_or_404(Pricing, pk=pricing_id)
    return render(request, 'pricing/details.html', {'pricing': pricing})

def list_pricing(request):
    pricings = Pricing.objects.all()
    return render(request, 'pricing/list_pricing.html', {'pricings': pricings})

def remove_pricing(request, pricing_id):
      pricing = get_object_or_404(Pricing, pk=pricing_id)
      pricing.delete()
      return redirect('pricing:list_pricing')


def update_pricing(request,pricing_id):
    pricing = get_object_or_404(Pricing, pk=pricing_id)
    
    if request.method == 'POST':
        form = PricingForm(request.POST, request.FILES, instance=pricing)
        if form.is_valid():
            form.save()
            return redirect('pricing:detail_pricing', pricing_id=pricing_id)
    else:
        form = PricingForm(instance=pricing)
    
    return render(request, 'pricing/update_pricing.html', {'form': form, 'pricing': pricing})