var this_url = window.location.href;
var index_of_run = this_url.indexOf('pdsf');
var base_url = this_url.substring(0,index_of_run);
var remainder_url = this_url.substring(index_of_run+10);
var index_of_user = remainder_url.indexOf('/');
var uname = remainder_url.substring(0, index_of_user);
var cmd_prefix = '/project/projectdirs/dayabay/webcommands';
var Jobs = new Object;

$('button').button();
$('#table_pdsf_jobs').tablesorter({
    headers : {
        6 : { sorter : false },  // output log
        7 : { sorter : false }   // error log
    }
});
$('#table_pdsf_recent_jobs').tablesorter({
    // headers : {
    //     6 : { sorter : false },  // output log
    //     7 : { sorter : false }   // error log
    // }
});

load_user(uname);
load_jobs(uname);
load_recent_jobs(uname);

function load_user(uname) {
    $.newt_ajax({
        url: '/account/user/' + uname + '/persons',
        type: 'GET',
        success: function(data) {
            if (data.items) {
                var user = data.items[0];
                $('#table_user_info td.value').each(function(){
                    attr =  $(this).attr('id');
                    if (user[attr]) {
                        $(this).html(user[attr]);
                    }
                });
            }
        } // success done.
    });
}

function load_jobs(uname) {
    var table = $('#table_pdsf_jobs');
    var cmd =  cmd_prefix + table.attr('command');
    var desc = table.attr('desc');
    $.noticeAdd({ text : "Loading " + desc + "... ", stay : true });
    $.newt_ajax({
       url: '/command/pdsf',    
       type: 'POST',
       data: {"executable": cmd}, 
       success: function(data) {
           var xml = $( $.parseXML( $.trim(data.output) ) );
           var html = '';
           var nJobs = 0;
           xml.find('job_list').each(function(){
               nJobs += 1;
               html += '<tr>';
               html += '<td class="jobid"><a href="#">' + $(this).find('JB_job_number').text() + '</a></td>';        
               html += '<td class="jobscript"><a href="#">' + $(this).find('JB_name').text() + '</a></td>';
               html += '<td>' + $(this).find('state').text() + '</td>';
               html += '<td>' + $(this).find('JAT_prio').text() + '</td>';
               html += '<td>' + $(this).find('JAT_start_time').text().replace('T', ' ') + '</td>';
               html += '<td>' + $(this).find('queue_name').text() + '</td>';
               html += '<td class="out_log"><a href="#">OUTPUT</a></td>';
               html += '<td class="err_log"><a href="#">ERROR</a></td>';
               html += "</tr>\n";
           });
           $('#nJobs_rqw').append('(' + nJobs + ')');
           table.find('tbody').html(html);
           $('#table_pdsf_jobs').trigger('update');
           $.noticeRemove($('.notice-item-wrapper'), 400);
           enable_qstat_jobid();
           enable_job_out_log();   
           enable_job_err_log();
           enable_job_script();
       }
    });
}

function load_recent_jobs(uname) {
    var table = $('#table_pdsf_recent_jobs');
    var cmd =  cmd_prefix + table.attr('command');
    var desc = table.attr('desc');
    $.noticeAdd({ text : "Loading " + desc + "... ", stay : true });
    $.newt_ajax({
       url: '/command/pdsf',    
       type: 'POST',
       data: {"executable": cmd}, 
       success: function(data) {
           var lines = data.output.split("\n");
           var i = 0;
           var html = '';
           var nJobs = 0;
           var RECORD_LENGTH = 13; // 13 lines per record
           while (i<lines.length) {
               if (!lines[i]) { i++; continue; } // skipe empty lines
               if (!lines[i+1]) { i++; continue; } // skipe last line
               nJobs += 1;
               html += '<tr>';
               html += '<td class="recent_jobid"><a href="#">' + $.trim(lines[i+4].replace('jobnumber','')) + '</a></td>';        
               html += '<td>' + $.trim(lines[i+3].replace('jobname','')) + '</td>';
               html += '<td>' + $.trim(lines[i+8].replace('failed','')).split(':')[0] + '</td>';
               html += '<td>' + $.trim(lines[i+6].replace('start_time','')) + '</td>';
               html += '<td>' + $.trim(lines[i+7].replace('end_time','')) + '</td>';
               html += '<td>' + $.trim(lines[i+9].replace('cpu','')) + '</td>';
               html += '<td>' + $.trim(lines[i+10].replace('mem','')) + '</td>';
               html += '<td>' + $.trim(lines[i+11].replace('io','')) + '</td>';
               html += '<td>' + $.trim(lines[i+12].replace('maxvmem','')) + '</td>';
               html += '<td>' + $.trim(lines[i+1].replace('hostname','')) + '</td>';
               html += "</tr>\n";
               
               i += RECORD_LENGTH;
           }
           $('#nJobs_recent').append('(' + nJobs + ')');
           table.find('tbody').html(html);
           $('#table_pdsf_recent_jobs').trigger('update');
           $.noticeRemove($('.notice-item-wrapper'), 400);
           enable_qacct_jobid();
       }
    });    
}

function enable_qstat_jobid() {
    $('#table_pdsf_jobs td.jobid a').click(function(){
       var jobid = $(this).html();
       if (Jobs[jobid]) {
           show_modal_pre(Jobs[jobid].details);
       }
       else {
           run_qstat_j(jobid, { show_modal : true });
        }
       return false;
    });
}

function enable_qacct_jobid() {
    $('#table_pdsf_recent_jobs td.recent_jobid a').click(function(){
       var jobid = $(this).html();
       var cmd = cmd_prefix + '/sge/qacct_raw -j ' + jobid;
       run_command(cmd);
       $.noticeAdd({ text : 'Loading job ' + jobid + ' ...', stay : true });
       return false;
    });
}

function enable_job_out_log() {
    $('#table_pdsf_jobs td.out_log a').click(function(){
       var jobid = $(this).parent().siblings('.jobid').find('a').html();
       if (Jobs[jobid]) {
           show_log(Jobs[jobid].out_log);
       }
       else {
           run_qstat_j(jobid, { show_log : 'out_log' });
       }
       return false;
    });
}

function enable_job_err_log() {
    $('#table_pdsf_jobs td.err_log a').click(function(){
       var jobid = $(this).parent().siblings('.jobid').find('a').html();
       if (Jobs[jobid]) {
           show_log(Jobs[jobid].err_log);
       }
       else {
           run_qstat_j(jobid, { show_log : 'err_log' });
       }
       return false;
    });
}

function enable_job_script() {
    $('#table_pdsf_jobs td.jobscript a').click(function(){
       var jobid = $(this).parent().siblings('.jobid').find('a').html();
       if (Jobs[jobid]) {
           show_full(Jobs[jobid].script);
       }
       else {
           run_qstat_j(jobid, { show_full : 'script' });
       }
       return false;
    });
}

function run_qstat_j(jobid, options) {
    var cmd = cmd_prefix + '/sge/qstat -j ' + jobid; 
    $.newt_ajax({
        url: '/command/pdsf',    
        type: 'POST',
        data: {"executable": cmd}, 
        success: function(data) {
            parse_job_details(data.output);
            $.noticeRemove($('.notice-item-wrapper'), 400);
            if (options.show_modal) { show_modal_pre(data.output); }
            else if (options.show_log) {
                if (Jobs[jobid]) { show_log(Jobs[jobid][options.show_log]); }          
            }
            else if (options.show_full) {
                if (Jobs[jobid]) { show_full(Jobs[jobid][options.show_full]); }          
            }
        }
    });
    $.noticeAdd({ text : 'Loading job ' + jobid + ' info ...', stay : true});    
}

function parse_job_details(details) {
    var lines = $.trim(details).split("\n");
    var jobid = lines[1].split(/\s+/).pop();
    var job  = Jobs[jobid] = new Object;
    job.details = details;
    
    var i, fields;
    for (i=2; i<lines.length; i++) {
        line = lines[i];
        fields = line.split(/:\s+/);
        if (! (fields.length == 2)) { continue; }
        job[fields[0]] = fields[1];
    }
    // console.log(job);
    if (job.stderr_path_list) {
        job.err_path = job.stderr_path_list.split(':').pop();
    }
    else { job.err_path = job.sge_o_workdir; }
    if (job.stdout_path_list) {
        job.out_path = job.stdout_path_list.split(':').pop();
    }
    else { job.out_path = job.sge_o_workdir; }    
    job.err_log = [ job.err_path, 
        job.err_path + '/' + job.job_name + '.e' + jobid, 
        job.sge_o_workdir + '/' + job.err_path
    ];
    job.out_log = [ job.out_path,
        job.out_path + '/' + job.job_name + '.o' + jobid,
        job.sge_o_workdir + '/' + job.out_path
    ];
    job.script = [ job.script_file,
        job.sge_o_workdir + '/' + job.script_file
    ];
}

function show_modal_pre(output) {
    $.modal('<div><pre>' + output + '</pre></div>',
        {
            'overlayClose' : true,
            'maxWidth' : 900,
            'maxHeight' : 600
        }
    );
}

function show_log(file_path_list) {
    var cmd = cmd_prefix + '/common/headtail -n 20 ' + file_path_list.join(':');
    run_command(cmd);
    $.noticeAdd({ text : 'Loading log file ...', stay : true });
}

function show_full(file_path_list) {
    var cmd = cmd_prefix + '/common/cat ' + file_path_list.join(':');
    run_command(cmd);
    $.noticeAdd({ text : 'Loading file ...', stay : true });
}

function run_command(cmd) {
    $.newt_ajax({
        url: '/command/pdsf',    
        type: 'POST',
        data: {"executable": cmd}, 
        success: function(data) {
            $.noticeRemove($('.notice-item-wrapper'), 400);
            $.modal('<div><pre>' + data.output + '</pre></div>',
                {
                    'overlayClose' : true,
                    'maxWidth' : 900,
                    'maxHeight' : 600
                }
            );
        }
    });
}
