var this_url = window.location.href;
var index_of_run = this_url.indexOf('run');
var base_url = this_url.substring(0,index_of_run);
var remainder_url = this_url.substring(index_of_run+4);
var runno = remainder_url.substring(0, remainder_url.indexOf('/'));

// diagnostic variables
var diagnostics_base_url = '';
var diagnostics_detector_list = [];
var diagnostics_figure_list = {};
var diagnostics_rootfileDir = '#';
load_diagnostics();

function load_diagnostics() {
    var url = base_url + 'production/diagnostics/run/' + runno + '/';
    $.getJSON( url, function(data) {
        diagnostics_base_url = data['base_url'];
        diagnostics_rootfileDir = diagnostics_base_url + data['roofile_dir'];
        var detector;
        for (detector in data['detectors']) {
            diagnostics_detector_list.push(detector);                
        }
        diagnostics_detector_list.sort();
        diagnostics_figure_list = data['detectors'];
        if (diagnostics_detector_list.length>0) {
            build_diagnostics(diagnostics_detector_list[0]); 
        }
        else {
            $('#diagnostic_section')
            .empty()
            .html('<h3 align="center">Not Available</h3>');
        }
        
        $("#diagnostics_loading").remove();
    }); // .getJSON done
}

function build_diagnostics(detname) {
    var figure_list = diagnostics_figure_list[detname];
    var table_diagnostic_plots = $('#table_diagnostic_plots');
    table_diagnostic_plots.empty();
    var column_index = 0;
    var html = '';
    var i;
    for (i=0; i<figure_list.length; i++) {
        if (column_index == 0) {html += '<tr>';}
        html += '<td><image class="img_db" src="'
             + url_force_reload(diagnostics_base_url + figure_list[i]['figpath'])
             + '" width=300 height=225 />'
             + '<span class="figname">' + figure_list[i]['figname'] + '</span></td>';
        column_index++;
        if (column_index == 3) {html += "</tr>\n"; column_index=0;}
    }
    table_diagnostic_plots.append(html);

    // enable image double click to origninal size
    modal_by_dbclick('.img_db');
    console.log(html);
}

// force reload url by appending a random query string
function url_force_reload(url) {  
    var date_now = new Date();
    return url + '?v=' + date_now.getTime();  
}

// display image modal window by double click
function modal_by_dbclick(selector) {
    $(selector).dblclick(function() {
        $.modal('<div><img src="' 
            + $(this).attr("src")
            + '" /></div>',
            {
                'overlayClose' : true
            }
        );
        return false;
    });
}
