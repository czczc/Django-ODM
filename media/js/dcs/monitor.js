var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('dcs'));
Highcharts.setOptions({
    chart: { type: 'scatter', zoomType: 'xy', animation: false },
    credits: { enabled: false },
    legend: { enabled: false },
    xAxis: { type: 'datetime' },       
    yAxis: { title: {text: ''}, tickPixelInterval: 36 },
    tooltip: { formatter: datetime_formatter },
    plotOptions: {
        scatter: { marker: {radius: 1} }
    }
});

var DcsData = new Object;

load_model('Ad1Lidsensor');
load_model('DbnsEnvPth');

function load_model(model) {
    var url = base_url + 'dcs/data/' + model + '/';
    $.getJSON(url, function(data) {
        DcsData[model] = data;
        for (i=0; i<data.length; i++) {
            row = DcsData[model][i].fields;
            row.date_time = parse_datetime(row.date_time);
        }
        if (model == 'Ad1Lidsensor') {
            init_chart({
                renderTo: 'Ad1Lidsensor__ultrasonic_gdls',
                title: 'AD1 GdLS Level: Ultrasonic',
                ymin: 1900, ymax: 2600,
                ysafemin: 2100, ysafemax: 2400
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__ultrasonic_ls',
                title: 'AD1 LS Level: Ultrasonic',
                ymin: 1900, ymax: 2600,
                ysafemin: 2000, ysafemax: 2300
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__capacitance_gdls',
                title: 'AD1 GdLS Level: Capacitance',
                ymin: 150, ymax: 450,
                ysafemin: 250, ysafemax: 350
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__capacitance_ls',
                title: 'AD1 LS Level: Capacitance',
                ymin: 150, ymax: 450,
                ysafemin: 300, ysafemax: 400
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__capacitance_mo',
                title: 'AD1 MO Level: Capacitance',
                ymin: 150, ymax: 450,
                ysafemin: 250, ysafemax: 350
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__temp_gdls',
                title: 'AD1 GdLS Temperature',
                ymin: 21, ymax: 26,
                ysafemin: 22, ysafemax: 25
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__temp_ls',
                title: 'AD1 LS Temperature',
                ymin: 21, ymax: 26,
                ysafemin: 22, ysafemax: 25
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__capacitance_temp_gdls',
                title: 'AD1 GdLS Temperature: Capacitance',
                ymin: 23, ymax: 28,
                ysafemin: 24, ysafemax: 27
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__capacitance_temp_ls',
                title: 'AD1 LS Temperature: Capacitance',
                ymin: 23, ymax: 28,
                ysafemin: 24, ysafemax: 27
            });
            init_chart({
                renderTo: 'Ad1Lidsensor__capacitance_temp_mo',
                title: 'AD1 MO Temperature: Capacitance',
                ymin: 21, ymax: 26,
                ysafemin: 22, ysafemax: 25
            });
        }
        else if (model == 'DbnsEnvPth') {
            init_chart({
                renderTo: 'DbnsEnvPth__dbns_pth_t1',
                title: 'EH1 Temperature: 1',
                ymin: 22, ymax: 29,
                ysafemin: 25, ysafemax: 28
            });
            init_chart({
                renderTo: 'DbnsEnvPth__dbns_pth_t2',
                title: 'EH1 Temperature: 2',
                ymin: 22, ymax: 29,
                ysafemin: 24, ysafemax: 27
            });
            init_chart({
                renderTo: 'DbnsEnvPth__dbns_pth_h1',
                title: 'EH1 Humidity: 1',
                ymin: 48, ymax: 75,
                ysafemin: 40, ysafemax: 60
            });
            init_chart({
                renderTo: 'DbnsEnvPth__dbns_pth_h2',
                title: 'EH1 Humidity: 2',
                ymin: 48, ymax: 75,
                ysafemin: 40, ysafemax: 60
            });
            init_chart({
                renderTo: 'DbnsEnvPth__dbns_pth_p1',
                title: 'EH1 Pressure: 1'
            });
            init_chart({
                renderTo: 'DbnsEnvPth__dbns_pth_p2',
                title: 'EH1 Pressure: 2'
            });
        }
    }); // .getJSON done
}

function init_chart(options) {
    var model_field = options.renderTo.split('__');
    highchartsOptions = {
       chart: { renderTo: options.renderTo },
       title: { text: options.title },
       yAxis: { endOnTick: true },
       series: [{ animation: false,
             data: convert_data(DcsData[model_field[0]], model_field[1])
           }
       ]
    };
    if (options.ymin && options.ymax) {
        highchartsOptions.yAxis.min = options.ymin;
        highchartsOptions.yAxis.max = options.ymax;
    }
    if (options.ysafemin && options.ysafemax) {
        highchartsOptions.yAxis.plotBands = [{ // reference band
            from: options.ysafemin, to: options.ysafemax,
            color: 'rgba(144, 238, 144, 0.1)'
        }];
    }
    var chart = new Highcharts.Chart(highchartsOptions);
    // console.log(chart.series[0].data);
}


// utility functions
function datetime_formatter() {
    // return '<b>'+ this.series.name +'</b><br/>value: ' + this.y + '<br/>'+
    return 'Value: ' + this.y + '<br/>'+
    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x);
}

function convert_data(rawdata, field) {
    var data_xy = new Array();
    var i, row;
    for (i=0; i<rawdata.length; i++) {
        row = rawdata[i].fields;
        data_xy.push([row.date_time, parseFloat(row[field])]);
    }
    return data_xy;
}

function parse_datetime(datetime) {
    var first_second = datetime.split(' ');
    var date = first_second[0].split('-');
    var time = first_second[1].split(':');
    return Date.UTC(date[0], date[1]-1, date[2], time[0], time[1], time[2]);
}