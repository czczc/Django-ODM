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
