$("button").button();

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
        var i, detname, site_detector, site, detector, det_cell;
        
        // enable rootfile dir button
        diagnostics_base_url = data['base_url'];
        diagnostics_rootfile_dir = diagnostics_base_url + data['rootfile_dir'];
        $("#diagnostics_rootfile_dir").click( function() {
           window.location =  diagnostics_rootfile_dir;
        });
        
        // initialize the diagnostics section
        for (detname in data['detectors']) {
            diagnostics_detector_list.push(detname);                
        }
        diagnostics_detector_list.sort();
        diagnostics_figure_list = data['detectors'];
        if (diagnostics_detector_list.length>0) {
            
            // enable live detectors
            for (i=0; i<diagnostics_detector_list.length; i++) {
                site_detector = parse_detname(diagnostics_detector_list[i]);
                site = site_detector[0];
                detector = site_detector[1];    
                det_cell = $("#diagnostics_site_det tr." + site + " td." + detector + " a" );
                det_cell.removeClass("det").addClass("live_det").attr("href", "#");
            }
            
            // build table of plots
            build_diagnostics(diagnostics_detector_list[0]); 
        }
        else {
            $("#diagnostics_detector").html('Diagnositics Unavailable');
            $('#diagnostic_section').empty();        
        }
        
        // enable live detectors click
        $("#diagnostics_site_det a.live_det").click( function(){
            var td = $(this).parent();
            var tr = td.parent();
            var site = tr.attr("class");
            var detector = td.attr("class");
            build_diagnostics(site+detector);
            // build_pmtmap(site+detector);  
            return false; 
        });
        
        // remove the loading animation
        $("#diagnostics_loading").remove();
    }); // .getJSON done
}

function build_diagnostics(detname) {
    $("#diagnostics_detector").html(detname);
    
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
}

// parse detname 'DayaBayAD1' into ['DayaBay', 'AD1']
function parse_detname(detname) {
    var sites = ['DayaBay', "LingAo", "Far", "SAB"];
    var site = "";
    var detector = "";
    var i=0;
    for (i=0; i<sites.length; i++) {
        site = sites[i];
        detector = detname.replace(site, "");
        if (detector.length < detname.length) { break; } // found
    }
    return [site, detector];
    // in not found, it returns ['','']
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
