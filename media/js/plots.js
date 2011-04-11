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
var sim_link = ''; if (production_name == 'simulation') { sim_link = 'sim/'; }

var Runinfo = null;
var ProductionRunList = new Object;
var ProductionSearchList = [];

if ( production_name == 'simulation' ) {
    $('#table_runlist td a').each(function(){
        var runno = $(this).html();
        ProductionRunList[runno] = '1';
    });
    $("#pb_bar").progressbar({ value: 100 });
    $('#pb_bar .pb_label').text('Ready for Searching');
    enable_submit();
}
else {
    load_runinfo();
    enable_submit();
}

// for bookkeeping ajax calls
var xhr_array = [];
var loaded_run = '';
var loaded_run_count = 0;
var is_ajax_finished = false; //ajax call started
var is_ajax_aborted = false;

function load_runinfo() {
    $('#submit').attr('disabled', 'disabled');
    var url = base_url + 'run/json/list/';
    $.getJSON( url, function(data) {
        Runinfo = data;
        $('#table_runlist td a').each(function(){
            var runno = $(this).html();
            ProductionRunList[runno] = '1';
            var run = Runinfo[runno];
            if (run) {
                $(this).addClass(run.runtype);
            }
        }); // $('#table_runlist td a').each() done
        $("#pb_bar").progressbar({ value: 100 });
        $('#pb_bar .pb_label').text('Ready for Searching'); 
        $('#submit').removeAttr('disabled');           
    }); // .getJSON done    
}

function enable_submit() {
    $("#submit").click( function() {
        var form_data = null;
        $(this).attr('disabled', 'disabled');
        $('.errorlist').html('');
        // console.log(form_data);
        var jqxhr = $.post("", $("#form_searchplots").serialize(),
            function(data) {
                var i;
                if (data.errors) { 
                    // server form validation failed
                    console.log('server form validation failed');
                    for (attr in data.errors) {
                        str_error = '';
                        for (i in data.errors[attr]) { 
                            str_error += '<li>' + data.errors[attr][i] + '</li>'; 
                        }
                        $('#'+attr+'_error').html(str_error);
                    }
                    $('#submit').removeAttr('disabled');
                }
                else {
                    form_data = data;
                    runlist = filter_runlist(form_data);
                    if (runlist.length == 0) {
                        $("#pb_bar").progressbar({ value: 100 });
                        $('#pb_bar .pb_label').text('No Run Matches. Double Click to Clear.');
                    }
                    else {
                        $('#submit').attr('disabled', 'disabled');
                        create_table(runlist, form_data);
                        submit_runlist(runlist, form_data);
                    }

                }
            }, "json");
        
        jqxhr.error(function() { 
            // console.log("error"); 
            $('#submit').removeAttr('disabled');
        });
        
        return false; 
    });
}

function filter_runlist(form_data) {
    var runlist = []; // the filtered run list
    
    var runtype = form_data.runtype;
    var txtlist = form_data.run_list.split(/\s+/);
    var i, j, runno;
    for(i=0; i<txtlist.length; i++) {
        runno = txtlist[i];
        if(runno.match('-')) {
            run_min_max = runno.split('-');
            run_min = parseInt(run_min_max[0],10);
            run_max = parseInt(run_min_max[1],10);
            if (!(run_min>=0 && run_max>0)) continue; 
            for (j=run_min; j<=run_max; j++) {                
                if(ProductionRunList[j]) {
                    
                    if(production_name == 'simulation') { runlist.push(j); }
                    else if (Runinfo[j] && (runtype == 'All' || Runinfo[j].runtype == runtype)) {
                        runlist.push(j);
                    }
                }     
            }
        }
        else {
            runno = parseInt(runno, 10);
            if (!(runno>=0)) continue;
            if(ProductionRunList[runno]) {
                if(production_name == 'simulation') { runlist.push(runno); }
                else if (Runinfo[runno] && (runtype == 'All' || Runinfo[runno].runtype == runtype)) {
                    runlist.push(runno);
                }
            }
        }            
    }
    if (form_data.sort_run == 'ASC') { runlist.sort( function(a,b){return a-b;} ); }
    else if (form_data.sort_run == 'DESC') { runlist.sort( function(a,b){return b-a;} ); }
    
    return runlist;
}

function create_table(runlist, form_data) {
    var showcase = $('#showcase');
    showcase.empty().hide();
    showcase.append('<table id="fig_table"></table>');
    var fig_table = showcase.find('#fig_table');
    
    var plot_list = form_data.plot_list;
    var nPlots = plot_list.length;
    var num_col = 3;
    if (form_data.num_col) { num_col = form_data.num_col; }

    var str, i, j, id, runno;
    if (nPlots > 1) { // num_col will not be used, one run perl table row
        str = "\n<thead>\n<tr><th>Run No.</th>";
        for (i=0; i<nPlots; i++) {
            str += ("<th>" + plot_list[i] + "</th>");
        }
        str += " </tr>\n</thead>\n";
        fig_table.append(str);
        
        fig_table.append("<tbody>\n");
        for (i=0; i<runlist.length; i++ ) {
            runno = runlist[i]; 
            str = "<tr><td>" + '<a href="'
            + base_url + 'run/' + runno + '/' + sim_link + '">' + runno
            + "</a></td>";
            
            for (j=0; j<nPlots; j++) {
                id = runno + plot_list[j];
                str += ('<td id="' + id + '">loading ...</td>');
            }
            str += "</tr>\n";
            fig_table.append(str);
        }
        fig_table.append("</tbody>");
        $("#showcase").show("slide", { direction: "up" }, "normal");
        return;
    }
    
    // only one plot from here on
    plot = plot_list[0];
    if (num_col == 1) { 
        // | runno | figure | 
        fig_table.append("\n<thead>\n<tr>"
            + "<th>Run No.</th>"
            + "<th>" + plot + "</th>" 
            + " </tr>\n</thead>\n"
        );
    
        fig_table.append("<tbody>\n");
        for (i=0; i<runlist.length; i++ ) {
            runno = runlist[i];
            fig_table.append("<tr><td>" + '<a href="'
                + base_url + 'run/' + runno + '/' + sim_link + '">' + runno
                + "</a></td>"
                + '<td id="' + runno + plot + '">loading ...</td>'
                + "</tr>\n");
        }
        fig_table.append("</tbody>");       
    }
    else if (num_col > 1) {
        // | plot_1 | plot_2 | ... | plot_num_col | 
        var nRuns = 0;
        fig_table.append("<tbody>\n");
        
        while (nRuns < runlist.length) {
            var str_row = "<tr>";
            for (i=0; i<num_col; i++) {
                if (nRuns < runlist.length) {
                    str_row += ('<td id="' + runlist[nRuns] + plot + '">'
                    + runlist[nRuns] + '<br />loading ...</td>');
                }
                else {
                    str_row += ('<td></td>'); 
                }
                nRuns++;
            }
            str_row += "</tr>\n";
            fig_table.append(str_row);
        }
        fig_table.append("</tbody>");
    }
    $("#showcase").show("slide", { direction: "up" }, "normal");
    
}

function submit_runlist(runlist, form_data) {
    // reset ajax calls
    xhr_array = [];
    loaded_run = '';
    loaded_run_count = 0;
    is_ajax_finished = false;
    is_ajax_aborted = false;
    
    $('#pb_bar .pb_label').text('Searching ...');
    $("#pb_bar").progressbar({ value: 1 });
    
    var plot_list = form_data.plot_list;
    var nPlots = plot_list.length;
    var num_col = 3;
    if (form_data.num_col) { num_col = form_data.num_col; }
    if (nPlots>1) { num_col = nPlots; }
    
    var i, runno, url;
    for(i=0; i<runlist.length; i++) { 
        runno = runlist[i];   
        url = base_url + 'production/' + production_name +'/search/run/' + runno + '/';
        var xhr = $.post(url, $("#form_searchplots").serialize(), function(data) {
            var thisrun = data.runno;
            loaded_run = thisrun;
            loaded_run_count++;
            
            var width = 860 / num_col;
            var height = width * 3 / 4;
            var link = '';
            if (nPlots==1) {
                link = '<br /><a href="' + base_url + 'run/' + thisrun + '/' 
                     + sim_link + '">' + thisrun + '</a>';
            }
            var j;
            for (j=0; j<nPlots; j++) {
                plot = plot_list[j];
                if (data.figures[plot]) {
                    html = '<img class="img_db" src="' 
                    + data.figures[plot] + '"'
                    + ' width=' + width 
                    + ' height=' + height + ' />';
                    html += link;                    
                }
                else { html = 'N/A' + link; }
                $('#'+thisrun+plot).html(html);
            }            
        }, "json")
        .complete(function() { 
            $('#pb_bar .pb_label').text('Run ' + loaded_run + ' Loaded (Double Click to Abort)');
            var percent = loaded_run_count*100 / runlist.length;
            $("#pb_bar").progressbar({ value: percent });
            if (percent == 100 && !is_ajax_aborted) {
                $('#pb_bar .pb_label').text('All Plots Loaded. Double Click to Clear.');
                is_ajax_finished = true;
                is_ajax_aborted = false;
                modal_by_dbclick('.img_db');
                $('#submit').removeAttr('disabled');
            }
        });
        xhr_array.push(xhr);
    }
}

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

$("#pb_bar").dblclick(function() {
    if(is_ajax_finished) {
        $("#showcase").empty();
        $('.pb_label').text('Ready for Searching');
        is_ajax_finished = true;
        is_ajax_aborted = false;
        $('#submit').removeAttr('disabled');
    }
    else {
        //stop all ajax calls, do not empty tables;
        for (var i=0; i<xhr_array.length; i++) {
            xhr_array[i].abort();
        }
        $('.pb_label').text('Loading Aborted. Double Click to Clear');
        is_ajax_aborted = true;
        is_ajax_finished = true;
        $('#submit').removeAttr('disabled');
    }
    $("#pb_bar").progressbar({ value: 100 });
});

$("#id_plot_list option").click(function() {
   nSelected = $('#id_plot_list option:selected').length;
   if (nSelected>1) {
       $("#id_num_col").attr('disabled', 'disabled');
   }
   else {
       $("#id_num_col").removeAttr('disabled');
   }
});

