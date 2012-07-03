from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings

class MaintainenceMiddleware:
    """
    Middleware that bring downs the whole site
    """
    def process_request(self, request):
        if settings.MAINTAINENCE:
            return HttpResponse('Site under maintainence, please check back later.')
            

class BlockingMiddleware(object):
    """
    Middleware that block certain remote access
    """
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in settings.BLACKLIST_IPS:
            return HttpResponseForbidden('<h1>Forbidden</h1>')
