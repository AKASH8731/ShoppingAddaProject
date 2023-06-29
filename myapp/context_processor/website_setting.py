from cms.models import WebsiteSetting


def website_setting(request):
    """ website_setting context processor to display dynamic logo and fotter address phone email """

    website_Setting = WebsiteSetting.objects.all().last()
    context = {
        'website_Setting': website_Setting
    }
    return (context)
