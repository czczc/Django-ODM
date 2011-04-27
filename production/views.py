from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.conf import settings

from odm.production.diagnostics import Diagnostics
from odm.production.pqm import Pqm
from odm.production.simulation import Simulation
from odm.production.forms import SearchPlotsForm, PQMSearchPlotsForm

import json, os

# ======= Diagnostics =======

@login_required
def diagnostics_runlist(request):
    '''return list of processed diagnostics runs'''
    
    run = Diagnostics()
    run.fetch_all()
    
    if request.is_ajax():
        return HttpResponse(json.dumps(run.run_list))
    else:
        raise Http404

@login_required      
def diagnostics_run(request, runno):
    '''single run diagnostic info'''
    
    run = Diagnostics(runno)
    run.fetch_all()
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(run.info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(run.info))
    else:
        raise Http404


@login_required      
def diagnostics_channel(request, production, runno, site, detector, board, connector):
    '''extract channel plots from tar file'''
    
    if production == 'diagnostics':
        run = Diagnostics(runno)
    elif production == 'simulation':
        run = Simulation(runno)
    else:
        return HttpResponse('invalid production name.')
    
    run.fetch_all()
    import tarfile, glob
    if settings.SITE_NERSC:
        TMPDIR = os.path.join(run.local_base_dir, 'tmp')
    elif settings.SITE_LOCAL:
        TMPDIR = os.path.join(settings.PROJECT_PATH, '../tmp')
            
    if run.info['detectors'].get(site+detector, []):
        figpath = os.path.join(run.local_base_dir, 
            run.info['detectors'][site+detector][0]['figpath'])
        figdir = os.path.dirname(figpath)
        channel_tarfile = os.path.join(figdir, 'channels.tar')
        
        try:
            tar = tarfile.open(channel_tarfile)
            extract_dir = "%s/run_%07d/detector_%s%s" % (
                TMPDIR, int(runno), site, detector)
            if not os.path.exists(extract_dir):
                os.makedirs(extract_dir)
                tar.extractall(extract_dir)
            channel_dir = "%s/channel_board%02d_connector%02d" % ( 
                extract_dir, int(board), int(connector))
            channel_figlist = glob.glob(channel_dir + '/*.png')
            channel_figlist = [ figpath.replace(TMPDIR, run.xml_base_url+'tmp') 
                for figpath in channel_figlist ]
                
        except IOError:
            # tar file not created yet
            channel_dir = "%s/channel_board%02d_connector%02d" % (
                figdir, int(board), int(connector))
            channel_figlist = glob.glob(channel_dir + '/*.png')
            channel_figlist = [ 
                figpath.replace(run.local_base_dir+'/', run.xml_base_url) 
                for figpath in channel_figlist ]

        return direct_to_template(request, 
            template = 'run/channelfigure.html',
            extra_context = {
                'figlist' : channel_figlist,
                'runno' : runno,
                'site' : site, 'detector' : detector,
                'board' : board, 'connector' : connector,
            })
        
    else:
        return HttpResponse('Detector does not exist.')


@login_required      
def diagnostics_cleantmp(request):
    '''clean up tmp directory'''
    run = Diagnostics()
    if settings.SITE_NERSC:
        TMPDIR = os.path.join(run.local_base_dir, 'tmp')
    elif settings.SITE_LOCAL:
        TMPDIR = os.path.join(settings.PROJECT_PATH, '../tmp')
    
    import shutil, glob
    dir_list = glob.glob(TMPDIR + '/run*')
    log = ''
    for run_dir in dir_list:
        # this is safe, web users only allowed to delete under 'apache' permissions
        shutil.rmtree(run_dir)
        log += run_dir + " removed.\n"
        
    return HttpResponse('<pre>' + log + '</pre>')
    
        
# ======= Simulation =======

@login_required      
def simulation_run(request, runno):
    '''single run diagnostic info'''
    
    run = Simulation(runno)
    run.fetch_all()
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(run.info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(run.info))
    else:
        raise Http404

            
# =========== PQM ===========

@login_required
def pqm_runlist(request):
    '''return list of processed pqm runs'''
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(Pqm().run_list, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(Pqm().run_list))
    else:
        raise Http404
        
@login_required
def pqm_run(request, runno):
    '''single run diagnostic info'''
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(Pqm(runno).info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(Pqm(runno).info))
    else:
        raise Http404


# =========== general view =========== 

@login_required
def view(request, production):
    '''general view of production plots'''
    
    is_diagnostics = is_simulation = is_pqm = False
    
    if production == 'diagnostics':
        is_diagnostics = True
        SearchForm = SearchPlotsForm
    elif production == 'simulation':
        is_simulation = True
        SearchForm = SearchPlotsForm
    elif production == 'pqm':
        is_pqm = True
        SearchForm = PQMSearchPlotsForm
    else:
        raise Http404
    
    # Validate the form if send though Ajax, otherwise initialize the form
    if request.method == 'POST':
        if request.is_ajax():
            form = SearchForm(request.POST)
            if form.is_valid():
                return HttpResponse(json.dumps(form.cleaned_data))
            else:
                return HttpResponse(json.dumps( {
                    'errors': form.errors,
                }))
        else:
            return HttpResponse('You seem to have disabled JavaScript in your Browser.')
    else:
        form = SearchForm() # An unbound form
    
    # fetch production run list    
    if is_diagnostics:
        diagnostics = Diagnostics()
        diagnostics.fetch_all()
        run_list = diagnostics.run_list.keys()
        title = 'Diagnostic Plots'
        jump_to = '#diagnostics'
    elif is_simulation:
        simulation = Simulation()
        simulation.fetch_all()
        run_list = simulation.run_list.keys()
        title = 'Simulation Plots'
        jump_to = 'sim'
        SearchForm = SearchPlotsForm
    elif is_pqm:
        run_list = Pqm().run_list.keys()
        title = 'PQM Plots'
        jump_to = '#pqm'
    else:
        return HttpResponse("Strange, you shouldn't reach here")

    if not run_list:
        return HttpResponse('<h1>No ' + title + ' Found</h1>')

    from odm.common.util import reversepage_runlist
    paged_runlist = reversepage_runlist(run_list)
    # return HttpResponse('<pre>'+json.dumps(paged_runlist, indent=4) + '</pre>')

    return direct_to_template(request, 
        template = 'production/view.html',
        extra_context = {
            'jump_to' : jump_to,
            'title' : title,
            'paged_runlist' : paged_runlist,
            'form' : form,
        })    
    
@login_required
def search(request, production, runno):
    '''production plots searching result'''
    
    is_diagnostics = is_simulation = is_pqm = False
    
    if production == 'diagnostics':
        is_diagnostics = True
        SearchForm = SearchPlotsForm
    elif production == 'simulation':
        is_simulation = True
        SearchForm = SearchPlotsForm
    elif production == 'pqm':
        is_pqm = True
        SearchForm = PQMSearchPlotsForm
    else:
        raise Http404

    
    if request.is_ajax():
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            plot_list = data['plot_list']
            detname = data['site'] + data['detector']
            
            if is_diagnostics:
                run = Diagnostics(runno)
                run.fetch_all()
            elif is_simulation:
                run = Simulation(runno)
                run.fetch_all()
            elif is_pqm:
                run = Pqm(runno)
            else:
                return HttpResponse('This is odd.')

            info = {
                'runno' : runno,
                'figures' : {},
            }            
            if not detname in run.info['detectors']: 
                return HttpResponse(json.dumps(info))

            info['figures'] = dict(
                [ (figure['figname'], run.info['base_url']+figure['figpath']) 
                    for figure in run.info['detectors'][detname] 
                    if figure['figname'] in plot_list ]
            )
            return HttpResponse(json.dumps(info))
            
        else:
            return HttpResponse(json.dumps( {
                'errors': form.errors,
            }))
    else:
        raise Http404
    

# =========== Jobs =========== 

@login_required
def diagnostics_scripts(request, production):
    '''diagnostic scripts generator'''
    from odm.production.forms import ViewRunProcessForm, ClearRunProcessForm, ProcessRunProcessForm
    from odm.production.forms import SimulationViewRunProcessForm, SimulationClearRunProcessForm, SimulationProcessRunProcessForm
    
    if not production in ['diagnostics', 'simulation']:
        raise Http404
        
    form_dict = {
        'diagnostics' : {
            'form_view' : ViewRunProcessForm,
            'form_clear' : ClearRunProcessForm,
            'form_process' : ProcessRunProcessForm,
        },
        'simulation' : {
            'form_view' : SimulationViewRunProcessForm,
            'form_clear' : SimulationClearRunProcessForm,
            'form_process' : SimulationProcessRunProcessForm,
        },
    }
    
    if request.is_ajax():
        form_name = request.POST.get('form_name', '')
        try:
            form = form_dict[production][form_name](request.POST)
        except:
            return HttpResponse('not valid form name')
        # if form_name == 'form_view':
        #     form = ViewRunProcessForm(request.POST)
        # elif form_name == 'form_clear':
        #     form = ClearRunProcessForm(request.POST)
        # elif form_name == 'form_process':
        #     form = ProcessRunProcessForm(request.POST)
        # else:
            
        
        if form.is_valid():
            data = form.cleaned_data
            info = {
                'data' : data,
                'script' : _script_generator(data)
            }            
            return HttpResponse(json.dumps(info))
        else:
            return HttpResponse(json.dumps( {
                'errors': form.errors,
            })) 
    else:
        form_view = form_dict[production]['form_view']() # An unbound form
        form_clear = form_dict[production]['form_clear']()
        form_process = form_dict[production]['form_process']()
        
    return direct_to_template(request, 
        template = 'production/scripts.html',
        extra_context = {
            'production' : production,
            'form_view' : form_view,
            'form_clear' : form_clear,
            'form_process' : form_process,
        })


def _script_generator(data):
    script = 'runProcess.py '
    if data.get('print_state', False):
        script += '--print-state '
    if data.get('clear_sequence', False):
        script += '--clear-sequence '
    if data.get('clear_stats', False):
        script += '--clear-sequence-stats '
    if data.get('clear_summary', False):
        script += '--clear-summary '
    if data.get('batch', False):
        script += '--batch '
    if data.get('run_nuwa', False):
        script += '--run-nuwa '
    if data.get('add_stats', False):
        script += '--add-stats '
    if data.get('summarize_run', False):
        script += '--summarize-run '
    script += '--cluster=%s ' % data.get('cluster', 'local')
    script += '-j %s ' % data.get('job_name', 'odm_v3')
    if data.get('data_file', ''):
        script += '-f %s ' % data['data_file']
    else:
        if data.get('run_no', ''):
            script += '-r %d ' % data.get('run_no', 0)
        if data.get('seq_no', ''):
            script += '-s %d ' % data['seq_no']
        elif data.get('all_sequences', False):
            script += '--all-sequences '

    return script
    
    
    