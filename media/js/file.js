var this_url = window.location.href;
var index_of_run = this_url.indexOf('run');
var base_url = this_url.substring(0,index_of_run);
var remainder_url = this_url.substring(index_of_run+4);

var Run = new Object;
Run.runno = remainder_url.substring(0, remainder_url.indexOf('/'));

load_catalog(Run.runno);

function load_catalog(runno) {
    var url = base_url + 'run/' + runno + '/files/catalog/';
    $.getJSON( url, function(data) {
        if (data.catalog_base_dir) { 
            $('#catalog_base_dir').html('PDSF: ' + data.catalog_base_dir); 
        }
        else { $('#catalog_base_dir').html('N/A'); }
        
        $("td.filename").each(function() {
           var filename = $(this).html();
           var td = $(this).siblings(".catalog");
           if (data.files) {
               if (data.files[filename]) { td.html('Yes').addClass('great'); }
               else { td.html('N/A').addClass('warning'); }
           }
           else { 
               td.html('N/A').addClass('warning'); 
           }

        });
    }); // .getJSON done
};