$('button').button();
$(".draggable").draggable({ cursor: 'move', opacity: 0.35 });
$('#jumper button').click(function() {
    window.location = $(this).attr('href');
});
$('button.to_top').click(function() {
    window.location = '#top';
});
$("#id_pmtspec_rollback").datepicker({ defaultDate: +0 });

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

var Ref = new Object;
set_ref(parseInt($('#ref_runno').html(), 10));
function set_ref(runno) {
    Ref.runno = runno;
    Ref.diagnostics_seg = sprintf('runs_%07d/runs_%07d/run_%07d', 
        Math.floor(Ref.runno/1000)*1000, Math.floor(Ref.runno/100)*100, Ref.runno);
    Ref.diagnostics_base_index = 60; // nersc
    Ref.pqm_shown = Ref.diagnostics_shown = false; // is currently displaying Ref?
}
$('#form_refrun_submit').click(function() {
    var field = $('#id_refrun');
    Ref.runno = parseInt(field.val(), 10) ;
    Ref.diagnostics_seg = sprintf('runs_%07d/runs_%07d/run_%07d', 
        Math.floor(Ref.runno/1000)*1000, Math.floor(Ref.runno/100)*100, Ref.runno);
    field.val(Ref.runno).css('color', 'green');
    return false; 
});


$('#sumit_pmtspec_rollback').click(function() {
    date = $('#id_pmtspec_rollback').val().split('/');
    if (date.length == 3) {
        Run.rollback = true;
        Run.rollback_month = date[0];
        Run.rollback_day = date[1];
        Run.rollback_year = date[2];
    }
    detname = $('#pmtinfo_detector').html();
    load_pmt(detname);
});
// $('#reload_pmtfigures').click(function() {
//     detname = $('#pmtinfo_detector').html();
//     load_pmtfigures(detname, Run.pmtinfo_data);
// });

// DAQ settings
Run.daq_detector_list = [];

// PMT info
Run.pmtinfo_data = null;

// Diagnostic plots
Run.diagnostics_base_url = '';
Run.diagnostics_detector_list = [];
Run.diagnostics_rootfile_dir = '#';
Run.diagnostics_data = null;
Run.diagnostics_seg = sprintf('runs_%07d/runs_%07d/run_%07d', 
    Math.floor(Run.runno/1000)*1000, Math.floor(Run.runno/100)*100, Run.runno);

// PQM plots
Run.pqm_detector_list = [];

// load everything
if (!Run.is_sim) {
    load_run_datetime();
    load_daq();
    load_production('pqm');
}
load_production('diagnostics');

// ==================================================================

function load_run_datetime() {
    if ($('#run_start_utc').html()) {
        var datetime_splitted = $('#run_start_utc').html().split(' ');
        var date = datetime_splitted[0]; 
        var time = datetime_splitted[1];
        var date_splitted = date.split('-');
        Run.year = date_splitted[0];
        Run.month = date_splitted[1];
        Run.day = date_splitted[2];
    }
    else { // set to be far in the future
        Run.year = 2020;
        Run.month = 1;
        Run.day = 1;
    }

}

function load_daq() {
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
            enable_live_detectors('daq', detector_list);
            // enable_live_detectors('pmtinfo', detector_list);
            
            // build daq tables
            build_daq_tables(detector_list[0], data);
            
            // load pmt info
            // site_detector = parse_detname(detector_list[0]);
            // load_pmt(site_detector[0]+site_detector[1]);
        }
        else {
            $("#daq_detector").html('NO Detector!');
            $("#daq_section").empty();  
        }
        
        $('#btn_more_daq').click( function(){
           $('#daq_section .hidden').toggle();
        });
        
        // enable daq live detectors click
        $("#daq_site_det a.live_det").click( function(){
            var td = $(this).parent();
            var tr = td.parent();
            var site = tr.attr("class");
            var detector = td.attr("class");
            if (Run.rtranslation[site]) { site = Run.rtranslation[site]; }
            if (Run.rtranslation[detector]) { detector = Run.rtranslation[detector]; }
            build_daq_tables(site+'-'+detector, data);
            $("#daq_section table").show('slide');
            return false;
        });
        
        // enable pmt live detectors click
        // $("#pmtinfo_site_det a.live_det").click( function(){
        //     var td = $(this).parent();
        //     var tr = td.parent();
        //     var site = tr.attr("class");
        //     var detector = td.attr("class");
        //     if (detector == 'RPC') {
        //         $("#pmtinfo_detector").html(site+detector);
        //         $('#pmt_section').hide('blind');
        //         return false;
        //     }
        //     $('#pmt_info td.value').html('');
        //     $('#pmt_section').show('slide');
        //     load_pmt(site+detector);
        //     return false;
        // });
        
        // remove the loading animation
        $("#daq_loading").remove();
    }); // .getJSON done
}

function enable_live_detectors(name, detector_list) {
    for (i=0; i<detector_list.length; i++) {                
        site_detector = parse_detname(detector_list[i]);
        site = site_detector[0];
        detector = site_detector[1];    
        det_cell = $("#"+ name + "_site_det tr." + site + " td." + detector + " a" );
        det_cell.removeClass("det").addClass("live_det").attr("href", "#");
    }
}

function load_pmt(detname) {
    $("#pmtinfo_detector").html(detname);

    var site_detector = parse_detname(detname);
    var site = site_detector[0];
    var detector = site_detector[1];
    if (detector.indexOf('AD') > -1) { 
        $('#muonpmtmap_table').hide(); 
        $('#adpmtmap_table').show(); 
    }
    else if (detector.indexOf('WS') > -1) {
        $('#adpmtmap_table').hide();
        //  temoprarily disable muon map until I figure out a good way to layout
        $('#muonpmtmap_table').hide();
    }
    
    if (!Run.year) { 
        load_pmtfigures(site+detector);
        return; 
    }

    var url = base_url + 'pmt/' + site + '/' + detector + '/'
            + Run.year + '/' + Run.month + '/' + Run.day + '/';
    if (Run.rollback) {
        url += 'rollback/' + Run.rollback_year + '/' + Run.rollback_month + '/' + Run.rollback_day + '/';
        $('#pmtspec_vld_seqno').html('loading ...');
        $('#pmtspec_vld_insert').html('');
        $('#pmtspec_vld_from').html('');
        $('#pmtspec_vld_to').html('');
        $('#sumit_pmtspec_rollback').attr('disabled', 'disabled');
    }
    $.getJSON( url, function(data) {
        Run.pmtinfo_data = data;
        
        if (data.cablemap_vld_seqno) { $('#cablemap_vld_seqno').html(data.cablemap_vld_seqno).css('color', '#333'); }
        else { $('#cablemap_vld_seqno').html('NO DBI RECORD !!').css('color','red'); }
        $('#cablemap_vld_from').html(data.cablemap_vld_from);
        $('#cablemap_vld_to').html(data.cablemap_vld_to);
        $('#cablemap_vld_insert').html(data.cablemap_vld_insert);
        if (data.pmtspec_vld_seqno) { $('#pmtspec_vld_seqno').html(data.pmtspec_vld_seqno).css('color', '#333'); }
        else { $('#pmtspec_vld_seqno').html('NO DBI RECORD !!').css('color','red'); }
        $('#pmtspec_vld_from').html(data.pmtspec_vld_from);
        $('#pmtspec_vld_to').html(data.pmtspec_vld_to);
        $('#pmtspec_vld_insert').html(data.pmtspec_vld_insert);
        $('#sumit_pmtspec_rollback').removeAttr('disabled');
        enable_pmt_mouse_actions(site+detector, data);
        load_pmtfigures(site+detector, data);
    }); // .getJSON done
}

function load_pmtfigures(detname, data) {
    var site_detector = parse_detname(detname);
    detname = site_detector[0] + site_detector[1];
    if (Run.is_sim) { production = 'simulation'; }
    else { production = 'diagnostics'; }
    
    diagnostics_data = Run.diagnostics_data;
    if (!diagnostics_data) {
        return;
    }
    else {
        var feemap_tds = $('#feemap_table td');
        feemap_tds.each(function() {
            var html = '';
            var board = $(this).attr("board");
            var connector = $(this).parent().attr("connector");
            if (board && connector) {
                $(this).html('');
                figures = diagnostics_data.detectors[detname];
                channels = diagnostics_data.channels[detname];
                if (figures) {
                    if(channels[board+'_'+connector]) {
                        html += '<a href="';
                        link = base_url + 'production/' + production + '/run/' + Run.runno + '/';
                        link += site_detector[0] + '/' + site_detector[1];
                        link += '/board/' + board + '/connector/' + connector + '/';
                        html += link +  '">O</a>';
                        $(this).html(html);
                        // console.log(html);
                        if (data) {
                            var pmtid = data.feename_to_id[detname + '-board' + board + '-connector' + connector];
                            var pmt = data.pmts[pmtid];
                            if (pmt) {
                                var ring = pmt.ring;
                                var column = pmt.column;                    
                                var selector = 'tr[ring="' + ring + '"] td[column="' + column + '"]';
                                var adpmt_td = $(selector);
                                if (adpmt_td) { adpmt_td.html(html); }
                            }
                        } // if (data) done
                    } // if(channels[board+'_'+connector]) done
                } // if (figures) done
            } // if (board && connector) done
        }); // feemap_tds.each() done.
         
        // $('#reload_pmtfigures').hide('blind');
    } // else done

}

function enable_pmt_mouse_actions(detname, data) {
    var pmt_ring = $("#pmt_ring");
    var pmt_column = $("#pmt_column");
    var pmt_board = $("#pmt_board");
    var pmt_connector = $("#pmt_connector");
    var pmt_wall = $("#pmt_wall");
    var pmt_spot = $("#pmt_spot");
    var pmt_spehigh = $("#pmt_spehigh");
    var pmt_spelow = $("#pmt_spelow");
    var pmt_toffset = $("#pmt_toffset");
    
    var color_select = '#4682B4';
    
    // enable feemap table cell mouse actions
    var feemap_tds = $('#feemap_table td');
    feemap_tds.unbind();
    feemap_tds.each(function() {
        var board = $(this).attr("board");
        var connector = $(this).parent().attr("connector");
        
        if (board && connector) {
            var pmtid = data.feename_to_id[detname + '-board' + board + '-connector' + connector];
            var pmt = data.pmts[pmtid];

            if (pmt) {
                var ring = pmt.ring;
                var column = pmt.column;                    
                var selector = 'tr[ring="' + ring + '"] td[column="' +column + '"]';
                var adpmt_td = $(selector);
                 
                var wall = pmt.wall;
                var spot = pmt.spot;
                var in_out = pmt.in_out;
                var spehigh = pmt.spehigh;
                var spelow = pmt.spelow;
                var toffset = pmt.toffset;
            }
            
            $(this).bind('click', function(){
                // console.log(pmt);
            });
            
            // setup fee table cell mouse over
            $(this).bind('mouseover', function(){
                 pmt_board.html(board);
                 pmt_connector.html(connector);
                 if (pmt) {
                     pmt_ring.html(ring);
                     pmt_column.html(column);
                     pmt_wall.html(wall);
                     pmt_spot.html(spot + ' ' + in_out);
                     pmt_spehigh.html(spehigh);
                     pmt_spelow.html(spelow);
                     pmt_toffset.html(toffset);
                 }
                 else {
                     pmt_ring.html('');
                     pmt_column.html('');
                 }
                $(this).css('background-color', color_select); 
                if(adpmt_td) { adpmt_td.css('background-color', color_select); }
            
            }); // bind mouseover done
            
            $(this).bind('mouseout', function(){
                $(this).css('background-color', 'white');
                if(adpmt_td) { adpmt_td.css('background-color', "white"); }
            }); // bind mouseout done
        }

        // 
    }); // tds.each() done

    // enable AD PMT map table cell mouse actions
    var adpmtmap_tds = $('#adpmtmap_table td');        
    adpmtmap_tds.unbind();
    adpmtmap_tds.each(function() {
        var column = $(this).attr("column");
        var ring = $(this).parent().attr("ring");
        
        if (ring && column) {
            var pmtid = data.pmtname_to_id[detname + '-ring' + ring + '-column' + column];
            var pmt = data.pmts[pmtid];
            if (pmt) {
                var board = pmt.board;
                var connector = pmt.connector;                    
                var selector = 'tr[connector="' + connector + '"] td[board="' + board + '"]';
                var fee_td = $(selector);

                var spehigh = pmt.spehigh;
                var spelow = pmt.spelow;
                var toffset = pmt.toffset;
            }
            
            // setup admpt table cell mouse over
            $(this).bind('mouseover', function(){
                pmt_ring.html(ring);
                pmt_column.html(column);
                if (pmt) {
                     pmt_board.html(board);
                     pmt_connector.html(connector);
                     pmt_spehigh.html(spehigh);
                     pmt_spelow.html(spelow);
                     pmt_toffset.html(toffset);
                 }
                 else {
                      pmt_board.html('');
                      pmt_connector.html('');
                  }
                $(this).css('background-color', color_select); 
                if(fee_td) { fee_td.css('background-color', color_select); }
            
            }); // bind mouseover done
            
            $(this).bind('mouseout', function(){
                $(this).css('background-color', 'white');
                if(fee_td) { fee_td.css('background-color', "white"); }
            }); // bind mouseout done
        }
    }); // tds.each() done

}

function build_daq_tables(detname, data) {
    $("#daq_detector").html(detname);
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
                // html += '<a href="#">' + FEEnumber + '</a>&nbsp;&nbsp;&nbsp;';
                html += FEEnumber + '&nbsp;&nbsp;&nbsp;';
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
            Run.diagnostics_data = data;
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
            enable_live_detectors(name, detector_list);

            // build table of plots
            build_plots(name, detector_list[0], data);
            if (Run.is_sim) {
                build_mc_plots(data);
            }
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
            $('#table_'+name+'_plots').show('drop');

            return false;
        });
        // remove the loading animation
        $("#"+name+"_loading").remove();
        
        if (name == 'diagnostics') {
            // load pmt info
            if (detector_list.length>0) {
                enable_live_detectors('pmtinfo', detector_list);
                site_detector = parse_detname(detector_list[0]);
                load_pmt(site_detector[0]+site_detector[1]);
                // enable pmt live detectors click
                $("#pmtinfo_site_det a.live_det").click( function(){
                    var td = $(this).parent();
                    var tr = td.parent();
                    var site = tr.attr("class");
                    var detector = td.attr("class");
                    if (detector == 'RPC') {
                        $("#pmtinfo_detector").html(site+detector);
                        $('#pmt_section').hide('blind');
                        return false;
                    }
                    $('#pmt_info td.value').html('');
                    $('#pmt_section').show('slide');
                    load_pmt(site+detector);
                    return false;
                });
            }
            else {
                $("#pmtinfo_detector").html('Detector Unavailable');
                $('#pmt_section').empty();
            }

        }
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
             + '<span class="figname">' + figure_list[i].figname
             + '<span class="ui-icon ui-icon-search img_comp"></span>'
             + '</span></td>';
        column_index++;
        if (column_index == 3) {html += "</tr>\n"; column_index=0;}
    }
    table_plots.append(html);

    // enable image double click to origninal size
    modal_by_click('#table_'+name+'_plots .img_db');
    // enable sub-detector comparison
    enable_img_comp('#table_'+name+'_plots .img_comp', detname, data);
    // check if need to show ref plots
    if (Ref[name+'_shown']) {
        $('#table_'+name+'_plots').find('.img_ref').remove();
        $('#table_'+name+'_plots').find('.img_db').each(function(){
            var this_link = $(this).attr('src');
            var ref_link = find_ref_plot(name, this_link);
            $(this).parent().append('<img class="img_ref" src="' + ref_link + '" width=300 height=225/>'); 
            modal_by_click($(this).siblings('.img_ref'));
            $(".ref_runno").html('Reference Run: ' + Ref.runno);
        });
    }
    // enable refenece plot comparison
    enable_toggle_img_ref();    
}

function build_mc_plots(data) {
    var production_url = Run.diagnostics_base_url;
    var table_plots = $('#table_truth_plots');
    var source_list = ['Muon', 'U238', 'Th232', 'K40', 'Co60', 'IBD'];
    var figure_list;
    var column_index, html, i;
    for (j=0; j<source_list.length; j++) {
        source = source_list[j];
        figure_list = data.Sources[source];
        column_index = 0;
        html = '<tr><th colspan="3" style="text-align:center;">Source ' 
            + source + ' Truth Info</th></tr>';
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
    }
    // enable image double click to origninal size
    modal_by_click('#table_truth_plots .img_db');
}

// parse detname 'DayaBayAD1' into ['DayaBay', 'AD1']
// or 'EH1-AD1' into ['DayaBay', 'AD1']
function parse_detname(detname) {
    var index = detname.indexOf('-');
    var site, detector;
    
    // DAQ convention EH1-AD1
    if (index>0) {
        site = detname.substring(0, index);
        detector = detname.substring(index+1);
        if (Run.translation[site]) { site = Run.translation[site]; }
        if (Run.translation[detector]) { detector = Run.translation[detector]; }
        return [site, detector];
    }
    
    // Analysis convention DayaBayAD1
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

// display image modal window by single click
function modal_by_click(selector) {
    // change cursor shape
    $(selector).hover(function() {
        $(this).css('cursor','pointer');
    }, function() {
        $(this).css('cursor','auto');
    });
    // single click
    $(selector).click(function() {
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


function enable_img_comp(selector, detname, data) {
    var site_detector = parse_detname(detname);
    var site = site_detector[0];
    var detector = site_detector[1];
    var has_AD1 = false; 
    var has_AD2 = false;
    if ((data.detectors)[site+'AD1']) { has_AD1 = true; }
    if ((data.detectors)[site+'AD2']) { has_AD2 = true; }
    $(selector).hover(function() {
        $(this).css('cursor','pointer');
    }, function() {
        $(this).css('cursor','auto');
    });
    $(selector).click(function() {
        var this_link = $(this).parent().prev('img').attr('src');
        var AD1 = "<h4>N/A</h4>";
        var AD2 = "<h4>N/A</h4>";
        if (has_AD1) { 
            AD1 = '<img src="' + this_link.replace(detector, 'AD1') + '" width=400 height=300 />'; 
        }
        if (has_AD2) {
            AD2 = '<img src="' + this_link.replace(detector, 'AD2') + '" width=400 height=300 />'; 
        }
        var html = '<div id="content"><table class="production"><tr>';
        html += '<td>' + AD1 + '<span class="figname">AD1</span></td>';
        html += '<td>' + AD2 + '<span class="figname">AD2</span></td>';
        html += '</tr></table></div>';
        // console.log(AD1);
        // console.log(AD2);
        $.modal(html,
            {
                'overlayClose' : true
            }
        );
        return false;
    });
}

function enable_toggle_img_ref() {
    $(document).unbind('keypress');
    $(document).bind('keypress', toggle_img_ref);
    $('.toggle_img_ref').bind('click', toggle_img_ref);
}

function toggle_img_ref(e) {
    var names = ['diagnostics', 'pqm'];
    var i, name;
    for (i=0; i<names.length; i++) {
        name = names[i];
        if(e.charCode == 92){            
            if (Ref[name+'_shown']) {
                $('#table_'+name+'_plots').find('.img_ref').remove();
                Ref[name+'_shown'] = false;
                $(".ref_runno").html('');
                
                // console.log(name+' emptied');
            }
            else {
                // console.log(name+' added');
                Ref[name+'_shown'] = true;
                $('#table_'+name+'_plots').find('.img_db').each(function(){
                    var this_link = $(this).attr('src');
                    var ref_link = find_ref_plot(name, this_link);
                    // console.log(ref_link);
                    $(this).parent().append('<img class="img_ref" src="' + ref_link + '" width=300 height=225/>'); 
                    modal_by_click($(this).siblings('.img_ref'));
                    $(".ref_runno").html('Reference Run: ' + Ref.runno);
                });
            }
        }
    } // for loop done.
}

// find the reference plot link 
function find_ref_plot(name, link) {
    if (name == 'diagnostics') {
        return link.replace(Run.diagnostics_seg, Ref.diagnostics_seg);
        // 
        // return link.substring(0,Ref.diagnostics_base_index) 
        //     + Ref.diagnostics_seg 
        //     + link.substring(Ref.diagnostics_base_index+37);
    }
    else {
        return link.replace('run'+Run.runno, 'run'+Ref.runno);
    }
}

function basename(path) {
    return path.replace(/\\/g,'/').replace( /.*\//, '' );
}
 
function dirname(path) {
    return path.replace(/\\/g,'/').replace(/\/[^\/]*$/, '');
}

// print raw calib info
printrawinfo();
function printrawinfo() {
    $('.raw a').click(function(){
        var url = $(this).attr('href');
        $.getJSON( url, function(data) {
            var html = '<div id="content"><table>';
            var descr = '';
            for (attr in data) {
                if (attr == 'vld') { descr = 'vld seqno'; }
                else { descr = attr; } 
                html += '<tr><td class="descr">' + descr 
                      + '</td><td class="value">' + data[attr] + '</td></tr>';
            }
            html += '</table></div>';
            // console.log(str);
            $.modal(html,
                {
                    'overlayClose' : true
                }
            );
        }); // .getJSON done
        return false;
    });
}