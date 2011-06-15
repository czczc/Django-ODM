chart = null;

var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('run'));
var url = base_url + 'run/stats/';
$.getJSON( url, function(data) {
    var months = data.months;
    var runs = data.runs;
    var data_xy = [];
    var i;
    for (i=0; i<months.length; i++) {
        year_month = months[i].split('-');
        year = parseInt(year_month[0], 10);
        month = parseInt(year_month[1], 10);
        data_xy[i] = [Date.UTC(year, month, 1), runs[i]];
    }
    chart_runcount(data_xy);
}); // .getJSON done


function chart_runcount(data_xy) {
   chart = new Highcharts.Chart({
      chart: { renderTo: 'chart_runstats', type: 'spline' },
      credits: { enabled: false },
      // legend: { align: 'right', verticalAlign: 'top', floating: true },
      title: { text: 'Integrated Number of Runs' },
      xAxis: { type: 'datetime' },
      yAxis: { title: {text: '# Runs'}, min: 0 },
      series: [{
         name: 'All Runs',
         data: data_xy
      }]
   });
}   
