var this_url = window.location.href;
var index_of_run = this_url.indexOf('run');
var base_url = this_url.substring(0,index_of_run);
var remainder_url = this_url.substring(index_of_run+4);

var Run = new Object;
Run.runno = remainder_url.substring(0, remainder_url.indexOf('/'));
Run.files = {
    'RAW' : {},
    'D2R' : {},
    'KUP' : {},
    'P11A' : {}
};

load_catalog(Run.runno);
load_catalog(Run.runno, 'D2R');
load_catalog(Run.runno, 'KUP');
load_catalog(Run.runno, 'P11A');
load_ODM(Run.runno);

function load_files() {
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
}

function load_catalog(runno, appl) {
    // var url = "http://dayabay.lbl.gov/production/catalog/service/report/run/" + runno;
    // if (appl) { url += '/?application=' + appl + '-P'; }
    var url = base_url + 'files/catalog/run/' + runno + '/';
    if (appl) { url += 'appl/' + appl + '/'; }
    else { appl = 'RAW'; }
    $.get(url, function(xml){
        dir = '';
        html = '';
        $(xml).find('Entry').each(function(){
            // var identity = $(this).find('identity').text();
            var location = $(this).find('location').text();
            var this_dir = dirname(location);
            var fileno = parse_fileno(basename(location));
            Run.files[appl][fileno] = 1;
            if (!(dir == this_dir)) {
                dir = this_dir;
                html += location + '<br />';
                // console.log(location);
            }
        });
        // console.log(Run.files);
        
        html = html.replace(/<br \/>$/, '');
        if (!html) { html = 'N/A'; }
        $('#'+appl).html(html);
        
        $("td.filename").each(function() {
            var fileno = parse_fileno($(this).html());
            var td = $(this).siblings("."+appl);
            if (Run.files[appl][fileno]) {
                td.html('Y').addClass('great');
            }
            else {
                td.html('N').addClass('warning');
            }
        });
        
    }, "xml")
    .error(function(){
        // console.log('error loading');
    });
}

function basename(path) { return path.replace(/\\/g,'/').replace( /.*\//, '' ); } 
function dirname(path) { return path.replace(/\\/g,'/').replace(/\/[^\/]*$/, ''); }
function parse_fileno(filename) { 
    var found = filename.match(/_\d+/);
    var fileno = 0;
    if (found) {
        fileno = parseInt(found[0].replace('_', ''), 10);
    }
    return fileno;
}

function load_ODM(runno) {
    var url = base_url + 'run/' + runno + '/files/diagnostics/';
    $.getJSON( url, function(data) {
        if (data.diagnostics_base_dir) { 
            $('#ODM').html(data.diagnostics_base_dir + '/'); 
        }
        else { $('#diagnostics_base_dir').html('N/A'); }
    
        $("td.filename").each(function() {
           var filename = $(this).html();
           var td = $(this).siblings(".ODM");
           if (data.files) {
               seq = filename.split('.')[6].substring(1);
               if (data.files[seq]) {
                   // var i; 
                   // var html = data.files[seq][len-1]; 
                   // for (i=1; i<data.files[seq].length; i++) {
                   //     html += ' ' + data.files[seq][i];
                   // }
                   td.html('Y').addClass('great'); 
               }
               else { td.html('N').addClass('warning'); }
           }
           else { 
               td.html('N').addClass('warning'); 
           }
        });
    }); // .getJSON done
}

// function load_catalog(runno) {
//     var url = base_url + 'run/' + runno + '/files/catalog/';
//     $.getJSON( url, function(data) {
//         if (data.catalog_base_dir) { 
//             $('#catalog_base_dir').html('PDSF: ' + data.catalog_base_dir); 
//         }
//         else { $('#catalog_base_dir').html('N/A'); }
//         
//         $("td.filename").each(function() {
//            var filename = $(this).html();
//            var td = $(this).siblings(".catalog");
//            if (data.files) {
//                if (data.files[filename]) { td.html('Yes').addClass('great'); }
//                else { td.html('N/A').addClass('warning'); }
//            }
//            else { 
//                td.html('N/A').addClass('warning'); 
//            }
//         });
//     }); // .getJSON done
// };
// 
// function load_diagnostics(runno) {
//     var url = base_url + 'run/' + runno + '/files/diagnostics/';
//     $.getJSON( url, function(data) {
//         if (data.diagnostics_base_dir) { 
//             $('#diagnostics_base_dir').html('PDSF: ' + data.diagnostics_base_dir); 
//         }
//         else { $('#diagnostics_base_dir').html('N/A'); }
//         
//         $("td.filename").each(function() {
//            var filename = $(this).html();
//            var td = $(this).siblings(".diagnostics");
//            if (data.files) {
//                seq = filename.split('.')[6].substring(1);
//                if (data.files[seq]) {
//                    var i; 
//                    var html = data.files[seq][0]; 
//                    for (i=1; i<data.files[seq].length; i++) {
//                        html += ' ' + data.files[seq][i];
//                    }
//                    td.html(html).addClass('great'); 
//                }
//                else { td.html('N/A').addClass('warning'); }
//            }
//            else { 
//                td.html('N/A').addClass('warning'); 
//            }
//         });
//     }); // .getJSON done
// };

$('.more').click(function(){
   var filename = $(this).parent().siblings('.filename').html();
   var url = base_url + 'files/proxy/' + filename + '/';
   $.get(url, function(xml){
       var html = '<div id="content"><table style="width: 600px;">';
       html += '<tr><td class="descr">File Name' 
             + '</td><td class="value">' + filename + '</td></tr>';        
       $(xml).find('endorsement').each(function(){           
            var role = $(this).find('role').text();            
            var whenSigned = $(this).find('whenSigned').text();
            html += '<tr><td class="descr">' + role 
                  + '</td><td class="value">' + covert_time(whenSigned) + '</td></tr>';
            // console.log(role + ' : ' + whenSigned);
        });
        html += '</table></div>';        
        $.modal(html,
            {
                'overlayClose' : true
            }
        );
   }, "xml")
   .error(function(){
       $.modal('Failed',
           {
               'overlayClose' : true
           }
       );
   });
   return false;
});

function covert_time(str) {
    var date_time = str.split('T');
    return date_time[0] + ' ' + date_time[1].split('-')[0];
}
