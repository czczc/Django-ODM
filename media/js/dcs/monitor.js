chart = null;

var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('dcs'));

var DcsData = new Object;

load_model('Ad1Lidsensor');

function load_model(model) {
    var url = base_url + 'dcs/model/' + model + '/';
    $.getJSON(url, function(data) {
        DcsData[model] = data;
        for (i=0; i<data.length; i++) {
            row = DcsData[model][i].fields;
            row.date_time = parse_datetime(row.date_time);
        }
        if (model == 'Ad1Lidsensor') {
            init_chart_Ad1Lidsensor__ultrasonic_gdls();
            init_chart_Ad1Lidsensor__ultrasonic_ls();
            init_chart_Ad1Lidsensor__capacitance_gdls();
        }
        
    }); // .getJSON done
}

function init_chart_Ad1Lidsensor__ultrasonic_gdls() {
    chart = new Highcharts.Chart({
       chart: { renderTo: 'Ad1Lidsensor__ultrasonic_gdls', type: 'scatter', zoomType: 'xy' },
       credits: { enabled: false },
       legend: { enabled: false },
       title: { text: 'AD1 GdLS Level: Ultrasonic' },
       xAxis: { type: 'datetime' },
       yAxis: { title: {text: ''} },
       tooltip: { formatter: datetime_formatter },
       plotOptions: {
           scatter: { marker: {radius: 2} }
       },
       series: [
           { animation: false,
             name: 'GdLS',
             data: convert_data(DcsData.Ad1Lidsensor, 'ultrasonic_gdls')
           }
       ]
    });
}

function init_chart_Ad1Lidsensor__ultrasonic_ls() {
    chart = new Highcharts.Chart({
       chart: { renderTo: 'Ad1Lidsensor__ultrasonic_ls', type: 'scatter', zoomType: 'xy' },
       credits: { enabled: false },
       legend: { enabled: false },
       title: { text: 'AD1 LS Level: Ultrasonic' },
       xAxis: { type: 'datetime' },
       yAxis: { title: {text: ''} },
       tooltip: { formatter: datetime_formatter },
       plotOptions: {
           scatter: { marker: {radius: 2} }
       },
       series: [
           { animation: false,
             name: 'LS',
             data: convert_data(DcsData.Ad1Lidsensor, 'ultrasonic_ls')
           }
       ]
    });
}

function init_chart_Ad1Lidsensor__capacitance_gdls() {
    chart = new Highcharts.Chart({
       chart: { renderTo: 'Ad1Lidsensor__capacitance_gdls', type: 'scatter', zoomType: 'xy' },
       credits: { enabled: false },
       legend: { enabled: false },
       title: { text: 'AD1 GdLS Level: Capacitance' },
       xAxis: { type: 'datetime' },       
       yAxis: { title: {text: ''} },
       tooltip: { formatter: datetime_formatter },
       plotOptions: {
           scatter: { marker: {radius: 2} }
       },
       series: [
           { animation: false,
             name: 'GdLS',
             data: convert_data(DcsData.Ad1Lidsensor, 'capacitance_gdls')
           }// ,
           //            { animation: false,
           //              name: 'LS',
           //              data: convert_data(DcsData.Ad1Lidsensor, 'capacitance_ls')
           //            },
           //            { animation: false,
           //              name: 'MO',
           //              data: convert_data(DcsData.Ad1Lidsensor, 'capacitance_mo')
           //            }
       ]
    });
}

// utility functions
function datetime_formatter() {
    return '<b>'+ this.series.name +'</b><br/>value: ' + this.y + '<br/>'+
    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x);
}

function convert_data(rawdata, field) {
    var data_xy = new Array();
    var i, row;
    for (i=0; i<rawdata.length; i++) {
        row = rawdata[i].fields;
        data_xy.push([row.date_time, row[field]]);
    }
    return data_xy;
}

function parse_datetime(datetime) {
    var first_second = datetime.split(' ');
    var date = first_second[0].split('-');
    var time = first_second[1].split(':');
    return Date.UTC(date[0], date[1]-1, date[2], time[0], time[1], time[2]);
}