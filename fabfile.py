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
def test_remote():
    run('cd dayabay')
    run('pwd')
    run('ls')

