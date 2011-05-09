from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

@login_required
def users(request):
    '''user list'''
    
    # blame NERSC who do not currently support IE auth login toolbar 
    if isIE(request):
        return HttpResponse('Sorry, your browser is not supported')

    return direct_to_template(request, 
        template = 'pdsf/users.html',
        extra_context = {
            'host' : 'PDSF',
        })

@login_required
def user(request, uname):
    '''user details'''
    
    if isIE(request):
        return HttpResponse('Sorry, your browser is not supported')
        
    return direct_to_template(request, 
        template = 'pdsf/user.html',
        extra_context = {
            'uname' : uname,
        })

# ======================================================
def isIE(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    try:
        user_agent.index('MSIE')
        return True
    except ValueError:
        return False
    