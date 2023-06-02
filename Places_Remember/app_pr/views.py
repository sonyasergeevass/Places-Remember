from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from .models import Memory
from .forms import MemoryForm
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


def login_page_vk(request):
    return render(request, 'login_page_vk.html')


@login_required
def home_page(request):
    memories = Memory.objects.filter(user=request.user)
    context = {'vk_data': return_vk_data(request), 'memories': memories}
    return render(request, 'home_page.html', context)


@login_required
def add_mem(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = Memory(
                user=request.user,
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude'],
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description']
            )
            memory.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = MemoryForm()

    context = {'vk_data': return_vk_data(request), 'form': form}
    return render(request, 'add_mem.html', context)


@login_required
def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    if memory.user != request.user:
        return render(request, 'access_denied.html')
    context = {'vk_data': return_vk_data(request), 'memory': memory}
    return render(request, 'memory_detail.html', context)
