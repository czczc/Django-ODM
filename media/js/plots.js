$("#pb_bar").progressbar({ value: 33 }); //start loading run list
$('#pb_bar .pb_label').text('Loading Run Info ...');

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
}
else {
    load_runinfo();
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