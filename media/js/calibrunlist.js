var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('run'));

printrawinfo();

function printrawinfo() {
    $('.raw a').click(function(){
        var runno = $(this).parent().siblings('.runno').find('a').text();
        var url = base_url + 'run/calibration/' + runno + '/';
        $.getJSON( url, function(data) {
            var html = '<div id="content"><table>';
            var descr = ''
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