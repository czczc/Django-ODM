# odm context processors

def setting(request):
    "custom setting variables"
    from django.conf import settings
    return {
        'SITE_ROOT': settings.SITE_ROOT,
        'VERSION': settings.VERSION,
    }