chart = null;

var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('run'));

$('button').button();
$(".draggable").draggable({ cursor: 'move', opacity: 0.35 });

var chart_div = $('#chart_daqstats');
var data_xy = [];
var title, xtitle, ytitle, legend, xtype;
var Runs = new Object;
var clock;

$.getJSON( base_url + 'run/json/list/', function(data) {
    for (run in data) {
        Runs[run] = {};
        Runs[run].timestart = data[run].timestart;
    }
}); // .getJSON done


$('#buttons_daqstats button').click(function(){
    chart_div.empty().html('<h3 align="center">Loading ...</h3>');
    var mode = $(this).attr('mode');
    var url = base_url + mode;
    $.getJSON( url, function(data) {
        chart_div.empty();
        data_xy = new Array();
        title = data.title;
        ytitle = data.ytitle;
        legend = data.legend;
        var xpoints = data.xpoints;
        var ypoints = data.ypoints;
        var i, runno;
        if (mode == 'run/stats/partition/' || mode == 'run/stats/runtype/') {
            for (i=0; i<xpoints.length; i++) {
                data_xy.push( [xpoints[i], ypoints[i]] );
            }
            charting_pie();
        }
        else if (data.xformat == 'year-month') {
            xtype = 'datetime';
            xtitle = '';
            for (i=0; i<xpoints.length; i++) {
                year_month = xpoints[i].split('-');
                year = parseInt(year_month[0], 10);
                month = parseInt(year_month[1], 10);
                data_xy[i] = [Date.UTC(year, month, 1), ypoints[i]];
            }
            charting();
        }
        else {
            clock = setInterval(function(){
                // wait until Runs are collected
                if (! Runs[6]) { 
                    // console.log('not available');
                    return; 
                }
                // Now it's ready
                clearInterval(clock);
                xtype = 'datetime';
                for (i=0; i<xpoints.length; i++) {
                    runno = xpoints[i];
                    if (Runs[runno]) {
                        date = Runs[runno].timestart.split(' ')[0];
                        // console.log(date);
                        data_xy.push( [Date.parse(date), ypoints[i]] );
                    }
                }
                charting();
            }, 500);
        }
        
    }); // .getJSON done
});



function charting() {
   chart = new Highcharts.Chart({
      chart: { renderTo: 'chart_daqstats', type: 'spline', zoomType: 'xy' },
      credits: { enabled: false },
      // legend: { align: 'right', verticalAlign: 'top', floating: true },
      plotOptions: {
          spline: {
              marker: {
                   enabled: false, states: { hover: { enabled: true } }   
                }
          } 
      },
      title: { text: title },
      xAxis: { type: xtype, title: {text: xtitle} },
      yAxis: { title: {text: ytitle}, min: 0 },
      series: [{
         // animation: false,
         name: legend,
         data: data_xy
      }]
   });
}   

function charting_pie() {
   chart = new Highcharts.Chart({
      chart: { 
          renderTo: 'chart_daqstats', plotBackgroundColor: null,
          plotBorderWidth: null, plotShadow: false 
      },
      credits: { enabled: false },
      plotOptions: {
          pie: {
             allowPointSelect: true,
             cursor: 'pointer',
             dataLabels: {
                enabled: true,
                color: Highcharts.theme.textColor || '#000000',
                connectorColor: Highcharts.theme.textColor || '#000000',
                formatter: function() {
                   return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
                }
             }
          }
      },
      title: { text: title },
      series: [{
         // animation: false,
         type: 'pie',
         name: legend,
         data: data_xy
      }]
   });
}
