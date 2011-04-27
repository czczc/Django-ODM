enable_ajax_csrf();

var this_url = window.location.href;
var first_seg = this_url.indexOf('production');
var base_url = this_url.substring(0,first_seg);
var remainder_url = this_url.substring(first_seg+11);
var second_seg = remainder_url.indexOf('/');
var production_name = remainder_url.substring(0, second_seg);

$('#hide_scripts_viewer').click(function(){
    $('#scripts_viewer').hide("slide", { direction: "up" }, "fast");
    $(this).hide();
    return false;
});

enable_form('form_view');
enable_form('form_clear');
enable_form('form_process');

function enable_form(name) {
    $("#submit_"+name).click( function() {
        $('#'+name+' .errorlist').html('');
        var jqxhr = $.post(this_url, $("#"+name).serialize(),
            function(data) {
                var i;
                if (data.errors) { 
                    // server form validation failed
                    for (attr in data.errors) {
                        str_error = '';
                        for (i in data.errors[attr]) { 
                            str_error += '<li>' + data.errors[attr][i] + '</li>'; 
                        }
                        $('#'+name+'_'+attr+'_error').html(str_error);
                    }
                }
                else {
                    var script = data.script;
                    $('#scripts_viewer').empty()
                    .html(script)
                    .show("slide", { direction: "up" }, "fast");
                    prettyPrint();
                    $('#hide_scripts_viewer').show();
                }
            }, "json"); // post done.
        jqxhr.error(function() { 
            ;
        });
        return false; 
    }); // $("#submit_form_view").click() done.
}