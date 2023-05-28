from django.shortcuts import render, redirect
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from .models import Memory


# Create your views here.

def login_page_vk(request):
    return render(request, 'login_page_vk.html')


@login_required
def home_page(request):
    vk_data = {}
    if request.user.is_authenticated:
        vk_account = SocialAccount.objects.filter(user=request.user,
                                                  provider='vk').first()
        if vk_account:
            vk_data = vk_account.extra_data
        # return {'vk_data': vk_data}
    context = {'vk_data': vk_data}
    return render(request, 'home_page.html', context)
    # return render(request, 'home_page.html')


def logout_view(request):
    logout(request)
    return redirect('login_vk')


# def add_mem(request):
#     return render(request, 'add_mem.html')

def add_mem(request):
    if request.method == 'POST':
        user = request.user
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        title = request.POST.get('title')
        description = request.POST.get('description')

        Memory.objects.create(user=user, latitude=latitude,
                              longitude=longitude,
                              title=title, description=description)
        return redirect('memory_list')

    return render(request, 'add_mem.html')
