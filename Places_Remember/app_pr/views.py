from django.shortcuts import render, redirect
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_page_vk(request):
    # vk_data = None
    # profile_photo_url = None
    # if request.user.is_authenticated:
    #     vk_account = SocialAccount.objects.filter(user=request.user,
    #                                               provider='vk').first()
    #     if vk_account:
    #         vk_data = vk_account.extra_data
    #         profile_photo_url = vk_data.get('photo_max_orig')
    # context = {'vk_data': vk_data, 'profile_photo_url': profile_photo_url}
    # return render(request, 'login_page_vk.html', context)
    # vk_data = None
    # if request.user.is_authenticated:
    #     vk_account = SocialAccount.objects.filter(user=request.user,
    #                                               provider='vk').first()
    #     if vk_account:
    #         vk_data = vk_account.extra_data
    # context = {'vk_data': vk_data}
    # return render(request, 'login_page_vk.html', context)

    # user_id = None
    # if request.user.is_authenticated:
    #     user_id = request.user.id

    return render(request, 'login_page_vk.html')


#     vk_data = {}
#     if request.user.is_authenticated:
#         vk_account = SocialAccount.objects.filter(user=request.user,
#                                                   provider='vk').first()
#         if vk_account:
#             vk_data = vk_account.extra_data
#         # return {'vk_data': vk_data}
#     context = {'vk_data': vk_data}
#     return render(request, 'login_page_vk.html', context)
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
