from django.shortcuts import render, redirect
from django.contrib.auth import logout
# from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def login_page_vk(request):
    # if request.user.is_authenticated:
    #     # Redirect to the profile page if the user is already authenticated
    #     return redirect('home')
    # else:
    #     return render(request, 'login_page_vk.html')
    # vk_account = SocialAccount.objects.filter(user=request.user,
    #                                           provider='vk').first()
    # context = {'vk_account': vk_account}
    # return render(request, 'login_page_vk.html', context)
    return render(request, 'login_page_vk.html')


def home_page(request):
    return render(request, 'home_page.html')


def logout_view(request):
    logout(request)
    return redirect('login_vk')
