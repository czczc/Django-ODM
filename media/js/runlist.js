var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('run'));

$("#table_list").tableFilter();

init_searchform();

load_file_list();

load_pqm_list();
load_diagnostics_list();

function init_searchform() {
    $("#id_date_from").datepicker({ defaultDate: +0 });
    $("#id_date_to").datepicker({ defaultDate: +0 });
    $('option[value="All"]').css('color', 'red');
}

function load_file_list() {
    var url = base_url + 'run/file/list/';
    $.getJSON( url, function(data) {
        $("td.NumFiles").each(function() {
           var run = $(this).attr('runno');
           if (!data[run]) { $(this).html('N/A'); }
           else { 
               link = base_url + 'run/' + run + '/files/';
               $(this).html('<a href="' + link + '">' + data[run] + '</a>'); 
           }
        });
    }); // .getJSON done
};

function load_pqm_list() {
    var url = base_url + 'production/pqm/run/list/';
    $.getJSON( url, function(data) {
        $("td.PQM").each(function() {
           var run = $(this).attr('runno');
           if (!data[run]) { $(this).html('N/A'); }
           else { 
               link = base_url + 'run/' + run + '#pqm';
               $(this).html('<a href="' + link + '">PQM</a>'); 
           }
        });
    }); // .getJSON done
};

function load_diagnostics_list() {
    var url = base_url + 'production/diagnostics/run/list/';
    $.getJSON( url, function(data) {
        if (!data) { return; }
        $("td.Diagnostics").each(function() {
           var run = $(this).attr('runno');
           if (!data[run]) { $(this).html('N/A'); }
           else { 
               link = base_url + 'run/' + run + '#diagnostics';
               $(this).html('<a href="' + link + '">Diagnostics</a>'); 
           }
        });
    }); // .getJSON done
}
