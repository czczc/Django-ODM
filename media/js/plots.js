$("#pb_bar").progressbar({ value: 33 }); //start loading run list
$('#pb_bar .pb_label').text('Loading Run Info ...');
$('#submit').removeAttr('disabled');

enable_ajax_csrf();

var this_url = window.location.href;
var first_seg = this_url.indexOf('production');
var base_url = this_url.substring(0,first_seg);
var remainder_url = this_url.substring(first_seg+11);
var second_seg = remainder_url.indexOf('/');
var production_name = remainder_url.substring(0, second_seg);

var Runinfo = null;


if ( production_name == 'simulation' ) {
    $("#pb_bar").progressbar({ value: 100 });
    $('#pb_bar .pb_label').text('Ready for Searching');
    enable_submit();
}
else {
    load_runinfo();
    enable_submit();
}


function load_runinfo() {
    var url = base_url + 'run/json/list/';
    $.getJSON( url, function(data) {
        Runinfo = data;
        $('#table_runlist td a').each(function(){
            var runno = $(this).html();
            var run = Runinfo[runno];
            if (run) {
                $(this).addClass(run.runtype);
                // console.log($(this).attr('class') + ':' + run.runtype);
            }
        }); // $('#table_runlist td a').each() done
        $("#pb_bar").progressbar({ value: 100 });
        $('#pb_bar .pb_label').text('Ready for Searching');
    }); // .getJSON done
}

function enable_submit() {
    $("#submit").click( function() {
        var form_data = null;
        $(this).attr('disabled', 'disabled');
        // console.log(form_data);
        var jqxhr = $.post("", $("#form_searchplots").serialize(),
            function(data) {
                form_data = data;
            }, "json");

        jqxhr.error(function() { 
            console.log("error"); 
            $('#submit').removeAttr('disabled');
        });
        
        jqxhr.complete(function() { 
            console.log("complete"); 
            $('#submit').removeAttr('disabled');
        });
        
        return false; 
    });
}


