from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

@login_required
def users(request):
    '''user list'''
        
    return direct_to_template(request, 
        template = 'pdsf/users.html',
        extra_context = {
            'host' : 'PDSF',
        })

@login_required
def user(request, uname):
    '''user details'''
        
    return direct_to_template(request, 
        template = 'pdsf/user.html',
        extra_context = {
            'uname' : uname,
        })