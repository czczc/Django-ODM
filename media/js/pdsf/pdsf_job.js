var cmd_prefix = '/project/projectdirs/dayabay/webcommands';

$('#submitjobs').click(function(){
   submit_job(); 
   return false;
});

function submit_job(){
    show_notice("Submitting Jobs ...");
    // var cmd =  cmd_prefix + '/sge/qsub -V /project/projectdirs/dayabay/django-sites/odm/templates/jobs/runProcess.sh';
    
    $.newt_ajax({
        url: '/queue/pdsf',
        // url: '/command/pdsf',    
        type: 'POST',
        // data: {"executable": cmd}, 
        
        data: {"jobfile": '/u/chaoz/dayabay/project_home/django-sites/odm/templates/jobs/runProcess.sh'},
        success: function(data) {
            show_modal_pre(
                "\n ==== Output ====\n" + data.output 
              + "\n ==== Error ====\n" + data.error
            );
            remove_notice();
        }, // success done.
        error: function() {
            show_error('operation failed');
        }
        
    });
}