# ads/views.py
from django.shortcuts import render, redirect
from .forms import AdvertisementForm
from .models import Advertisement


def render_interface(request):
    return render(request, "upload.html")

def upload_ad(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save()
            return redirect('view_ad', ad_id=ad.id)
    else:
        form = AdvertisementForm()
    return render(request, 'ads/upload_ad.html', {'form': form})

def view_ad(request, ad_id):
    ad = Advertisement.objects.get(pk=ad_id)
    return render(request, 'ads/view_ad.html', {'ad': ad})
