from django.http import HttpResponse
from django.conf import settings

class MaintainenceMiddleware:
    """
    Middleware that bring downs the whole site
    """
    def process_request(self, request):
        if settings.MAINTAINENCE:
            return HttpResponse('Site under maintainence, please check back later.')