from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from .models import Memory
from django.shortcuts import get_object_or_404


# Create your views here.

def login_page_vk(request):
    return render(request, 'login_page_vk.html')


@login_required
def home_page(request):
    vk_data = {}
    memories = Memory.objects.filter(user=request.user)
    if request.user.is_authenticated:
        vk_account = SocialAccount.objects.filter(user=request.user,
                                                  provider='vk').first()
        if vk_account:
            vk_data = vk_account.extra_data
    context = {'vk_data': vk_data, 'memories': memories}
    return render(request, 'home_page.html', context)


# def logout_view(request):
#     logout(request)
#     return redirect('login_vk')


def add_mem(request):
    vk_data = {}
    if request.user.is_authenticated:
        vk_account = SocialAccount.objects.filter(user=request.user,
                                                  provider='vk').first()
        if vk_account:
            vk_data = vk_account.extra_data
    context = {'vk_data': vk_data}
    if request.method == 'POST':
        user = request.user
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        title = request.POST.get('title')
        description = request.POST.get('description')

        Memory.objects.create(user=user, latitude=latitude,
                              longitude=longitude,
                              title=title, description=description)
        return redirect('home')

    return render(request, 'add_mem.html', context)


def memory_detail(request, memory_id):
    vk_data = {}
    if request.user.is_authenticated:
        vk_account = SocialAccount.objects.filter(user=request.user,
                                                  provider='vk').first()
        if vk_account:
            vk_data = vk_account.extra_data
    memory = get_object_or_404(Memory, id=memory_id)
    context = {'vk_data': vk_data, 'memory': memory}
    return render(request, 'memory_detail.html', context)
