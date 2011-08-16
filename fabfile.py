# fabric tasks
from fabric.api import *

env.hosts = ['portal-auth.nersc.gov']
env.user = 'chaoz'

# =============================
def scrape(site='local', target='odmrun', dryrun='dryrun'):
    '''scrape records into odm database'''
    
    cmd = './manage.py runscript scrape --script-args "%s %s"' % (target, dryrun)
    
    if site == 'local':
        if dryrun != 'dryrun':
            local('cp -f db/odm.db ~/bin/backup/')
        local(cmd)
    elif site == 'portal':
        run('source dayabay/load_odm_env.sh')
        with cd('dayabay/odm'):
            # back up database
            if dryrun != 'dryrun':
                run('cp -f db/odm.db ~/backup/')
            with prefix('source ~/dayabay/load_odm_env.sh'):
                # run('echo $PYTHONPATH')
                run(cmd)
    else:
        print 'site not found %s' % site
        return

# =============================
@hosts('chaoz@pdsf3.nersc.gov')
def deploy_pdsf(dryrun=False):
    '''deploy to production site'''
    from fabric.contrib.project import rsync_project
    
    if dryrun: 
        dry_run = ' --dry-run'
    else: 
        dry_run = ''
    
    # media server
    rsync_project(
        remote_dir='/project/projectdirs/dayabay/www/odm_media/',
        # remote_dir='~/tmp/odm_media/',
        local_dir='./media/',
        exclude='.svn/',
        extra_opts='--update' + dry_run,
    )
    # wsgi server
    rsync_project(
        remote_dir='/project/projectdirs/dayabay/django-sites/',
        # remote_dir='~/tmp/django-sites/',
        exclude=('.svn/', '.htaccess', '*.pyc', 'db/'),
        extra_opts='--update' + dry_run,
    )


# =============================
@hosts('zhangchao@202.122.37.74')
def deploy_ihep(dryrun=False):
    '''deploy to production site'''
    from fabric.contrib.project import rsync_project
    
    if dryrun: 
        dry_run = ' --dry-run'
    else: 
        dry_run = ''
    
    # media server
    rsync_project(
        remote_dir = '/data/odm/odmweb/',
        # remote_dir   = '~/tmp/odm_media/',
        local_dir    = './media/',
        exclude      = '.svn/',
        extra_opts   = '--update' + dry_run,
    )
    rsync_project(
        remote_dir = '~/django-sites/',
        # remote_dir   = '~/tmp/django-sites/',
        exclude      = ('.svn/', '.htaccess', '*.pyc', 'db/'),
        extra_opts   = '--update' + dry_run,
    )
                
# =============================
def test_remote():
    run('cd dayabay')
    run('pwd')
    run('ls')

