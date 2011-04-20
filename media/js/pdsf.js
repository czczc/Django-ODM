var this_url = window.location.href;
var index_of_run = this_url.indexOf('pdsf');
var base_url = this_url.substring(0,index_of_run);

var Users = new Object;

$('button').button();
$('#table_pdsf_users').tablesorter();

$('#btn_pdsf_logout').click(function(){
    $.newt_ajax({
        url: '/logout',       
        type: 'GET',
        success: function(data) {
            window.location = base_url;
        }
    });
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
                html += '<tr>';
                html += '<td>' + _user.user_id + '</td>';
                url = base_url + 'pdsf/user/' + _user.uname + '/';
                html += '<td class="uname"><a href="' + url + '">' + _user.uname + '</a></td>';
                html += '<td>' + _user.gecos + '</td>';
                html += '<td class="jobs_total"></td>';
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
                }
            }
            
            $('#table_pdsf_users .uname').each(function(){
               var uname = $(this).find('a').html();
               var User = Users[uname];
               $(this).siblings('.jobs_total').html(User.jobs.total); 
               $(this).siblings('.jobs_r').html(User.jobs.r); 
               $(this).siblings('.jobs_qw').html(User.jobs.qw); 
            });
            $.noticeRemove($('.notice-item-wrapper'), 400);
            
            $('#table_pdsf_users .jobs_total').each(function(){
               var total = $(this).html();
               if (parseInt(total,10) > 0) {
                    $(this).css('color', 'red');
               }
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
                    $(this).css('color', 'blue');
               }
            });
            $('#table_pdsf_users').trigger('update');
        }
    });
}

// cmd  = "#!/bin/bash\n";
// cmd += "export SGE_ROOT=/usr/common/nsg/sge/sge6_2u2_1\n";
// cmd += "/usr/common/nsg/sge/sge6_2u2_1/bin/lx24-x86/qstat -u chaoz\n";
// run_command(cmd);

function run_command() {
    $.newt_ajax({
        url: '/queue/pdsf',    
        type: 'POST',
        // data: {"executable": cmd}, 
        data: {"jobscript": cmd}, 
        success: function(data) {
            console.log(data);
        }
    });
}