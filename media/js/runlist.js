var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('run'));

init_searchform();


load_pqm_list();
load_diagnostics_list();

function init_searchform() {
    $("#id_date_from").datepicker({ defaultDate: +0 });
    $("#id_date_to").datepicker({ defaultDate: +0 });
    $('option[value="All"]').css('color', 'red');
}

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
