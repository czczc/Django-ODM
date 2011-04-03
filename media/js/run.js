$("button").button();
$(".draggable").draggable({ cursor: 'move', opacity: 0.35 });
$('#show_pmtmap').click(function() {
    $("#pmt_section").slideToggle('fast');
});

var this_url = window.location.href;
var index_of_run = this_url.indexOf('run');
var base_url = this_url.substring(0,index_of_run);
var remainder_url = this_url.substring(index_of_run+4);

var Run = new Object;
Run.runno = remainder_url.substring(0, remainder_url.indexOf('/'));
if (remainder_url.indexOf('/sim/')>0) { Run.is_sim = true; }
else { Run.is_sim = false; }
Run.has_diagnostics = false;
Run.has_pqm = false;
Run.translation = new Object; Run.rtranslation = new Object;
Run.translation.EH1 = 'DayaBay'; Run.rtranslation.DayaBay = 'EH1';
Run.translation.EH2 = 'LingAo'; Run.rtranslation.LingAo = 'EH2';
Run.translation.EH3 = 'Far'; Run.rtranslation.Far = 'EH3';
Run.translation.WPI = 'IWS'; Run.rtranslation.IWS = 'WPI';
Run.translation.WPO = 'OWS'; Run.rtranslation.OWS = 'WPO';

// DAQ settings
Run.daq_detector_list = [];

// Diagnostic plots
Run.diagnostics_base_url = '';
Run.diagnostics_detector_list = [];
Run.diagnostics_rootfile_dir = '#';

// PQM plots
Run.pqm_detector_list = [];

// load everything
if (!Run.is_sim) {
    load_daq('daq');
    load_production('pqm');
}
load_production('diagnostics');

// ==================================================================

function load_daq(name) {
    // name: 'diagnostics' or 'pqm'
    var url = base_url + 'run/daq/' + Run.runno + '/';
    $.getJSON( url, function(data) {
        var detector_list = Run.daq_detector_list;
        var i, detname, site_detector, site, detector, det_cell;
        for (detname in data.detectors) {
            detector_list.push(detname);        
        }
        detector_list.sort();
        if (detector_list.length>0) {
            // enable live detectors
            for (i=0; i<detector_list.length; i++) {                
                site_detector = parse_detname(detector_list[i]);
                site = site_detector[0];
                detector = site_detector[1];    
                det_cell = $("#"+ name + "_site_det tr." + site + " td." + detector + " a" );
                det_cell.removeClass("det").addClass("live_det").attr("href", "#");
            }
            // build daq tables
            build_daq_tables(name, detector_list[0], data);
        }
        else {
            $("#"+name+"_detector").html('Plots Unavailable');
            $("#"+name+"_section").empty();  
        }
        
        $('#btn_more_daq').click( function(){
           $('#daq_section .hidden').toggle();
        });
        // enable live detectors click
        $("#"+name+"_site_det a.live_det").click( function(){
            var td = $(this).parent();
            var tr = td.parent();
            var site = tr.attr("class");
            var detector = td.attr("class");
            if (Run.rtranslation[site]) { site = Run.rtranslation[site]; }
            if (Run.rtranslation[detector]) { detector = Run.rtranslation[detector]; }
            build_daq_tables(name, site+'-'+detector, data);
            $("#"+name+"_section table").show('slide');
            return false;
        });
        
        // remove the loading animation
        $("#"+name+"_loading").remove();
    }); // .getJSON done
}

function build_daq_tables(name, detname, data) {
    $("#"+name+"_detector").html(detname);
    $("#daq_section td.value").html('');
    
    var daq = data.detectors[detname];
    var attr, i;
    var FEEnumber = FEEprefix = '';
    var FEEregex = /(FEE.*_)(\d+)$/;
    var html = '';
    for (attr in daq) {
        if (attr == 'FEEBoards') {
            for (i in daq[attr]){
                FEEnumber = daq[attr][i].replace('FEE_'+daq.FEEPrefix+'_', '');
                html += '<a href="#">' + FEEnumber + '</a>&nbsp;&nbsp;&nbsp;';
            }
            $('#FEEBoards').html(html).click(function(){
                return false;
            });
        }
        else {
            $('#'+attr).html(daq[attr]);
        }
    }
    $('#FEEPrefix').html('FEE_' + daq.FEEPrefix);
    
    if(detname.indexOf('RPC')>0) {
        $('.FEESetting td.value').html('');
    }

}

function load_production(name) {
    // name: 'diagnostics' or 'pqm'
    var url = '';
    if (Run.is_sim) { url = base_url + 'production/simulation/run/' + Run.runno + '/';}
    else { url = base_url + 'production/' + name + '/run/' + Run.runno + '/'; }
    $.getJSON( url, function(data) {
        var i, detname, site_detector, site, detector, det_cell;
        var detector_list, figure_list;
        
        if (name == 'diagnostics') { 
            Run.has_diagnostics = true; 
            Run.diagnostics_base_url = data.base_url;
            
            detector_list = Run.diagnostics_detector_list;
            
            // enable rootfile dir button
            Run.diagnostics_rootfile_dir = Run.diagnostics_base_url + data.rootfile_dir;
            $("#diagnostics_rootfile_dir").click( function() {
               window.location =  Run.diagnostics_rootfile_dir;
            });
        }
        else if (name == 'pqm') { 
            Run.has_pqm = true; 
            Run.pqm_base_url = data.base_url;
            
            detector_list = Run.pqm_detector_list;
        }
        
        // initialize the production section
        for (detname in data.detectors) {
            detector_list.push(detname);        
        }
        detector_list.sort();
        if (detector_list.length>0) {
            // enable live detectors
            for (i=0; i<detector_list.length; i++) {
                site_detector = parse_detname(detector_list[i]);
                site = site_detector[0];
                detector = site_detector[1];    
                det_cell = $("#"+ name + "_site_det tr." + site + " td." + detector + " a" );
                det_cell.removeClass("det").addClass("live_det").attr("href", "#");
            }
            // build table of plots
            build_plots(name, detector_list[0], data);
            // build fee/pmt map 
            build_pmtmap(name, detector_list[0], data);
            // load channel info
            load_channels(name, detector_list[0], data);
        }
        else {
            $("#"+name+"_detector").html('Plots Unavailable');
            $("#"+name+"_section").empty();  
        }

        // enable live detectors click
        $("#"+name+"_site_det a.live_det").click( function(){
            var td = $(this).parent();
            var tr = td.parent();
            var site = tr.attr("class");
            var detector = td.attr("class");
            build_plots(name, site+detector, data);
            build_pmtmap(name, site+detector, data);
            load_channels(name, site+detector, data);
            return false;
        });

        // remove the loading animation
        $("#"+name+"_loading").remove();
    }); // .getJSON done
}

function build_plots(name, detname, data) {
    $("#"+name+"_detector").html(detname);
    var production_url = '';
    if (name == 'diagnostics') {
        production_url = Run.diagnostics_base_url;
    }
    else if (name == 'pqm') {
        production_url = Run.pqm_base_url;
    }
    figure_list = (data.detectors)[detname];
    var table_plots = $('#table_'+name+'_plots');
    // table_plots.hide('slide');
    table_plots.empty();
    var column_index = 0;
    var html = '';
    var i;
    for (i=0; i<figure_list.length; i++) {
        if (column_index == 0) {html += '<tr>';}
        html += '<td><image class="img_db" src="'
             + url_force_reload(production_url + figure_list[i].figpath)
             + '" width=300 height=225 />'
             + '<span class="figname">' + figure_list[i].figname + '</span></td>';
        column_index++;
        if (column_index == 3) {html += "</tr>\n"; column_index=0;}
    }
    table_plots.append(html);
    table_plots.show('slide');
    // enable image double click to origninal size
    modal_by_dbclick('#table_'+name+'_plots .img_db');
}

function build_pmtmap(name, detname, data) {
    if (name == 'pqm') { return; }
    var site_detector, site, detector;
    var i, html, board, connector, str_board, str_connector, link;
    
    site_detector = parse_detname(detname);
    site = site_detector[0];
    detector = site_detector[1];
    
    var feemap_table = $("#feemap_table");
    feemap_table.empty();
    html = "<tr><td>connector</td>";
    for (i=1; i<=16; i++) {
        html += "<td>" + sprintf("%02d", i) + "</td>";
    }
    html += "</tr>";    
    for (board=5; board<=18; board++) {
        str_board = sprintf("%02d", board);
        html += "<tr board="
              + '"' + str_board + '"'
              + "><td>board " + str_board + "</td>";
        for (connector=1; connector<=16; connector++) {
            str_connector = sprintf("%02d", connector);
            html += '<td connector="' + str_connector + '"><a href="';
            link = Run.diagnostics_base_url+dirname(data.detectors[detname][0].figpath);
            link += '/channel_board' + str_board + '_connector' + str_connector;
            html += link;
            html += '">O</a></td>';
        }
        html += "</tr>";
    }
    feemap_table.append(html);
    
    var pmtmap_table = $("#pmtmap_table");
    pmtmap_table.empty();
    var ring, column, str_ring, str_column;
    if (detector.indexOf('AD') != -1) {
        html = "<tr><td>column</td>";
        for (i=1; i<=24; i++) {
            html += "<td>" + sprintf("%02d", i) + "</td>";
        }
        html += "</tr>";    
        for (ring=8; ring>=0; ring--) {
            str_ring = sprintf("%02d", ring);
            html += "<tr ring="
                  + '"' + str_ring + '"'
                  + "><td>ring " + str_ring + "</td>";
            for (column=1; column<=24; column++) {
                str_column = sprintf("%02d", column);
                html += '<td column="' + str_column + '">';
                html += "</td>";
            }
            html += "</tr>";
        }
        pmtmap_table.append(html);
                
    }
    else if (detector.indexOf('WS') != -1) {
        html = "<tr><td>spot</td>";
        for (i=1; i<=29; i++) {
            html += "<td>" + sprintf("%02d", i) + "</td>";
        }
        for (ring=1; ring<=9; ring++) {
            str_ring = sprintf("%02d", ring);
            html += "<tr ring="
                  + '"' + str_ring + '"'
                  + "><td>" + str_ring + "</td>";
            for (column=1; column<=29; column++) {
                str_column = sprintf("%02d", column);
                html += '<td column="' + str_column + '">';
                html += "</td>";
            }
            html += "</tr>";
        }
        pmtmap_table.append(html);
        $("#td_ring").prev().html('<h6>Wall</h6>');
        $("#td_column").prev().html('<h6>Spot</h6>');
    }
        
}

function load_channels(name, detname, data) {
    if (name == 'pqm') { return; }
    // $('#th_pmtinfo').html('Loading ...');
    channel_info = (data.channels)[detname];
    $('#feemap_table td').each(function(){
        var connector = $(this).attr("connector");
        var board = $(this).parent().attr("board");
        var channelname = board + '_' + connector;
        if (board && connector && !channel_info[channelname]) {
            $(this).empty();
        }
    });
}

// parse detname 'DayaBayAD1' into ['DayaBay', 'AD1']
function parse_detname(detname) {
    var index = detname.indexOf('-');
    var site, detector;
    
    // DAQ convention
    if (index>0) {
        site = detname.substring(0, index);
        detector = detname.substring(index+1);
        if (Run.translation[site]) { site = Run.translation[site]; }
        if (Run.translation[detector]) { detector = Run.translation[detector]; }
        return [site, detector];
    }
    
    // Analysis convention
    var sites = ['DayaBay', "LingAo", "Far", "SAB"];
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

function basename(path) {
    return path.replace(/\\/g,'/').replace( /.*\//, '' );
}
 
function dirname(path) {
    return path.replace(/\\/g,'/').replace(/\/[^\/]*$/, '');
}

