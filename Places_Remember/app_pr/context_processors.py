from allauth.socialaccount.models import SocialAccount


def vk_data(request):
    vk_account = SocialAccount.objects.filter(user=request.user,
                                              provider='vk').first()
    if vk_account:
        vk_data = vk_account.extra_data
    else:
        vk_data = {}
    return {'vk_data': vk_data}
