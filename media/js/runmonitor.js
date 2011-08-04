var this_url = window.location.href;
var index_of_run = this_url.indexOf('run');
var base_url = this_url.substring(0,index_of_run);
var remainder_url = this_url.substring(index_of_run+4);

var Run = new Object;
Run.runno = remainder_url.substring(0, remainder_url.indexOf('/'));

var FIGLIST = {
    // 'AD1' : {},
    // 'AD2' : {},
    // 'IWS' : {},
    // 'OWS' : {},
    // 'RPC' : {}
};

Run.has_diagnostics = false;
Run.has_pqm = false;

Run.diagnostics_base_url = '';
Run.diagnostics_detector_list = [];

Run.pqm_base_url = '';
Run.pqm_detector_list = [];

load_production('diagnostics');
load_production('pqm');


function load_production(name) {
    // name: 'diagnostics' or 'pqm'
    var url = base_url + 'production/' + name + '/run/' + Run.runno + '/';
    $.getJSON( url, function(data) {
        var i, detname, site_detector, site, detector, det_cell;
        var detector_list, figure_list;
        
        if (name == 'diagnostics') {
            Run.has_diagnostics = true; 
            Run.diagnostics_base_url = data.base_url;

            detector_list = Run.diagnostics_detector_list;
            
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
            build_figlist(data);
            build_table(name, data);
        }
        else {  
        }

    }); // .getJSON done
}

function build_figlist(data) {
    var detname, fig;
    for (detname in data.detectors) {
        if (!FIGLIST[detname]) {
            FIGLIST[detname] = {};
        }
        figs = (data.detectors)[detname];
        var i;
        for (i=0; i<figs.length; i++) {
            FIGLIST[detname][figs[i].figname] = data.base_url + figs[i].figpath;
        }
    }
    // console.log(FIGLIST);
}

function build_table(name, data) {
    $(".production td." + name).each(function(){
        var site = 'DayaBay';
        var detector = $(this).attr('detector');
        var detname = '';
        if (FIGLIST[site + detector]) {detname = site +detector;}
        var html = $(this).html();
        var html2 = 'N/A<br/>';
        if (detname) {            
            var figname = $(this).attr('figname');
            if (FIGLIST[detname][figname]) {                
                html2 = '<image class="img_db" src="'
                       + url_force_reload(FIGLIST[detname][figname])
                       + '" width=450 height=338 />';
            }
        }
        $(this).html(html2 + html);
        
    });
    
    // $(".production").each(function(){
    //     var detector = $(this).attr('detector');
    //     var detname = '';
    //     if (data.detectors['DayaBay'+detector]) {detname = 'DayaBay'+detector;}
    //     if (detname) {
    //         figs = (data.detectors)[detname];
    //         var i;
    //         for (i=0; i<figs.length; i++) {
    //             fig_list[detector][figs[i].figname] = figs[i].figpath;
    //         }
    //         // console.log(fig_list);
    //         $(this).find("td."+name).each(function(){
    //             figname = $(this).attr('figname');
    //             if (fig_list[detector][figname]) {
    //                 html = '<image class="img_db" src="'
    //                        + url_force_reload(data.base_url + fig_list[detector][figname])
    //                        + '" width=300 height=225 />'
    //                        + '<span class="figname">' + figname + '</span>';
    // 
    //             }
    //             else {
    //                 html = '<span class="figname">' + figname + '</span>';
    //             }
    //             $(this).html(html);
    //         });
    //     }
    // });
    
    modal_by_click('.img_db');
    
}

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