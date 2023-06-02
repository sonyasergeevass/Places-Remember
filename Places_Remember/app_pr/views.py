from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from .models import Memory
from django.shortcuts import get_object_or_404


# Create your views here.

def return_vk_data(request):
    vk_data = {}
    if request.user.is_authenticated:
        vk_account = SocialAccount.objects.filter(user=request.user,
                                                  provider='vk').first()
        if vk_account:
            vk_data = vk_account.extra_data
    return vk_data


def custom_login_required(view_func):
    actual_decorator = login_required(view_func)

    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_vk')
        return actual_decorator(request, *args, **kwargs)

    return wrapper_func


def login_page_vk(request):
    return render(request, 'login_page_vk.html')


@custom_login_required
def home_page(request):
    memories = Memory.objects.filter(user=request.user)
    context = {'vk_data': return_vk_data(request), 'memories': memories}
    return render(request, 'home_page.html', context)


@custom_login_required
def add_mem(request):
    context = {'vk_data': return_vk_data(request)}
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


@custom_login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    context = {'vk_data': return_vk_data(request), 'memory': memory}
    return render(request, 'memory_detail.html', context)
