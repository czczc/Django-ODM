var this_url = window.location.href;
var index_of_run = this_url.indexOf('pdsf');
var base_url = this_url.substring(0,index_of_run);

$('button').button();

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
            var users = data.items;
            users.sort(by_uname);
            var i, user;
            html = '';
            for (i=0; i<users.length; i++) {
                user = users[i];
                html += '<tr>';
                html += '<td>' + user.user_id + '</td>';
                html += '<td>' + user.uname + '</td>';
                html += '<td>' + user.gecos + '</td>';
                html += '<td><a href="#">Jobs</a></td>';
                html += "</tr>\n";
            }
            $('#table_pdsf_users tbody').empty().html(html);
            $('#table_pdsf_users').show('slide');
            // $('#users_loading').remove();
            // console.log(data);
        }
    });
}

function by_uname(a, b) {
    if (a.uname < b.uname) { return -1; }
    else { return 1; }
}

// load_user('chaoz');
function load_user(username) {
    $.newt_ajax({
        url: '/account/user/' + username + '/persons',
        type: 'GET',
        success: function(data) {
            // console.log(data);
        }
    });
}

$.newt_ajax({
    url: '/queue/pdsf/4698945',
    type: 'GET',
    success: function(data) {
        console.log(data);
    }
});

