# ads/views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AdvertisementForm
from .models import Advertisement

@login_required
def upload_ad(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save()
            return redirect(f'/view_ad/{ad.id}')
    else:
        form = AdvertisementForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def view_ad(request, ad_id):
    ad = Advertisement.objects.get(pk=ad_id)
    return render(request, 'view_ad.html', {'ad': ad})

def embed_ad(request, ad_id):
    ad = get_object_or_404(Advertisement, pk=ad_id)
    ad.impressions += 1
    ad.save()
    return render(request, 'embed_ad.html', {'ad': ad})

@login_required
def landing_page(request):
    ads = Advertisement.objects.all()
    return render(request, 'index.html', {'ads': ads})   