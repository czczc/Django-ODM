# odm context processors

def setting(request):
    "custom setting variables"
    from django.conf import settings
    return {
        'SITE_ROOT': settings.SITE_ROOT,
        'VERSION': settings.VERSION,
        'SITE_IHEP': settings.SITE_IHEP,
        'SITE_NERSC': settings.SITE_NERSC,
        'SITE_LOCAL': settings.SITE_LOCAL,
    }