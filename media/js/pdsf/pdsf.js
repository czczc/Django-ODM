var this_url = window.location.href;
var index_of_run = this_url.indexOf('pdsf');
var base_url = this_url.substring(0,index_of_run);
var cmd_prefix = '/project/projectdirs/dayabay/webcommands';

var Users = new Object;

$('button').button();
$('#table_pdsf_users').tablesorter();
$('#table_pdsf_jobs').tablesorter();

$('button.show_div').click(function(){
   var div_class = $(this).attr('id'); 
   $('div .' + div_class).toggle("slide", { direction: "up" }, "normal");
});

$('button.command').click(function(){
    var cmd = cmd_prefix + $(this).attr('command'); 
    var desc = $(this).html(); 
    run_command(cmd);
    $.noticeAdd({
       text : "Loading " + desc + "... ",
       stay : true
    });
});

$('#hide_jobs_table').click(function(){
    $('#table_pdsf_jobs').hide("slide", { direction: "up" }, "normal");
    $(this).hide();
    return false;
});


$('#btn_all_users').click(function(){
    load_users('dayabay');
    return false; 
});

load_group('dayabay');
load_users('dayabay');

function load_group(group) {
    $.newt_ajax({
        url: '/account/group/' + group,
        // url: '/account/project/' + group,
        // url: '/account/repo/' + group,        
        type: 'GET',
        success: function(data) {
            if (data.items) {
                group = data.items[0];
                $('#fiscal_year').html(group.fiscal_year);
                $('#gname').html(group.gname);
                $('#gid').html(group.gid);
                // console.log(data);
            }
        }
    });
}

function load_users(group) {
    $.newt_ajax({
        url: '/account/group/' + group + '/users',
        type: 'GET',
        success: function(data) {
            var _users = data.items;
            _users.sort(by_uname);
            var i, _user, User;
            url = html = '';
            for (i=0; i<_users.length; i++) {
                _user = _users[i];
                User = Users[_user.uname] = new Object;
                User.user_id = _user.user_id;
                User.gecos = _user.gecos;
                User.jobs = new Object;
                User.jobs.total = User.jobs.r = User.jobs.qw = 0;
                User.jobs.items = [];
                html += '<tr>';
                html += '<td>' + _user.user_id + '</td>';
                url = base_url + 'pdsf/user/' + _user.uname + '/';
                html += '<td class="uname"><a href="' + url + '">' + _user.uname + '</a></td>';
                html += '<td>' + _user.gecos + '</td>';
                html += '<td class="jobs_total"><a href="#"></a></td>';
                html += '<td class="jobs_r"></td>';
                html += '<td class="jobs_qw"></td>';
                html += "</tr>\n";
            }
            $('#table_pdsf_users tbody').empty().html(html);
            $('#table_pdsf_users').show('drop');
            $('#table_pdsf_users thead th').removeClass('headerSortDown headerSortUp');
            $.noticeAdd({
               text : 'loading job queue ...',
               stay : true
            });
            load_queue();
            // $('#users_loading').remove();
        }
    });
}

function by_uname(a, b) {
    if (a.uname < b.uname) { return -1; }
    else { return 1; }
}

function load_queue() {
    $.newt_ajax({
        url: '/queue/pdsf',     
        type: 'GET',
        success: function(data) {
            var i, job;
            for (i=0; i<data.length; i++) { 
                job = data[i];
                uname = job.user;
                if (Users[uname]) {
                    status = job.status;
                    Users[uname].jobs[status] += 1;
                    Users[uname].jobs.total += 1;
                    Users[uname].jobs.items.push(job);
                }
            }
            // console.log(Users.cjslin);
            $('#table_pdsf_users .uname').each(function(){
               var uname = $(this).children('a').html();
               var User = Users[uname];
               $(this).siblings('.jobs_total').children('a').html(User.jobs.total); 
               $(this).siblings('.jobs_r').html(User.jobs.r); 
               $(this).siblings('.jobs_qw').html(User.jobs.qw); 
            });
            $.noticeRemove($('.notice-item-wrapper'), 400);
            
            $('#table_pdsf_users .jobs_total a').click(function(){
                build_jobs_table($(this).parent().siblings('.uname').children('a').html());
                return false;
            });
            $('#table_pdsf_users .jobs_r').each(function(){
               var total = $(this).html();
               if (parseInt(total,10) > 0) {
                    $(this).css('color', 'green');
               }
            });
            $('#table_pdsf_users .jobs_qw').each(function(){
               var total = $(this).html();
               if (parseInt(total,10) > 0) {
                    $(this).css('color', 'red');
               }
            });
            $('#table_pdsf_users').trigger('update');
        }
    });
}

function build_jobs_table(uname) {
    var job;
    var html= '';
    for (i=0; i<Users[uname].jobs.items.length; i++) {
        job = Users[uname].jobs.items[i];
        html += '<tr>';
        html += '<td class="jobid"><a href="#">' + job.jobid + '</a></td>';
        html += '<td>' + job.priority + '</td>';
        html += '<td>' + job.name + '</td>';
        html += '<td>' + job.user + '</td>';
        html += '<td>' + job.status + '</td>';
        html += '<td>' + job.starttime + ' ' + job.queue + '</td>';
        html += '<td>' + job.slots + '</td>';
        html += "</tr>\n";
    }
    $('#table_pdsf_jobs tbody').empty().html(html);
    $('#table_pdsf_jobs thead th').removeClass('headerSortDown headerSortUp');
    $('#table_pdsf_jobs')
    .show("slide", { direction: "up" }, "normal")
    .trigger('update');
    $('#hide_jobs_table').show();
    enable_qstat_jobid();
}

function enable_qstat_jobid() {
    $('#table_pdsf_jobs td.jobid a').click(function(){
       var jobid = $(this).html();
       var cmd = cmd_prefix + '/sge/qstat -j ' + jobid; 
       run_command(cmd);
       $.noticeAdd({
          text : 'Loading job ' + jobid + ' info ...',
          stay : true
       });
       return false;
       // console.log(cmd);
    });
}
