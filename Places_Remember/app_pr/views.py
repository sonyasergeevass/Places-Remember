from django.shortcuts import render


# Create your views here.

def login_page_vk(request):
    return render(request, 'login_page_vk.html')


def home_page(request):
    return render(request, 'home_page.html')
