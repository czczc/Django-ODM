// enable ajax post csrf protetion

function enable_ajax_csrf() {
    $('html').ajaxSend(function(event, xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        // 
        // if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        //     // Only send the token to relative URLs i.e. locally.
        //     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        // }
    });
}
