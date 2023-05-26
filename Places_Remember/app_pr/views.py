from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_page_vk(request):
    return render(request, 'login_page_vk.html')


@login_required
def home_page(request):
    return render(request, 'home_page.html')
