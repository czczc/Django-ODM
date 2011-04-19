
load_users();

function load_users() {
    $.newt_ajax({
        url: '/account/group/dayabay/users',
        type: 'GET',
        success: function(data) {
            // console.log(data);
        }
    });
}


