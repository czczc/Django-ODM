var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('dcs'));
$('button').button();
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
var latest_days = 30;
var configs = new Object;
load_config();
var charts = [];
var DcsData = new Object;

load_all_models();
fetch_latest();
var timer = setInterval('fetch_latest()', 120000);


$('#select_days a').click(function(){
    latest_days = $(this).attr('days');
    load_all_models();
    return false;
});

function load_all_models() {
    var i;
    for (i=0; i<charts.length; i++) {
        charts[i].destroy();
    }
    // console.log(charts.length + ' charts destroyed.');
    charts.length = 0;
    load_model('Ad1Lidsensor');
    load_model('Ad2Lidsensor');
    load_model('DbnsIowTemp');
    load_model('DbnsRpcGas101');
    load_model('DbnsEnvPth');
}

function fetch_latest() {
    fetch_one('Ad1Lidsensor');
    fetch_one('Ad2Lidsensor');
    fetch_one('DbnsIowTemp');
    fetch_one('DbnsRpcGas101');
    fetch_one('DbnsEnvPth');
}

function fetch_one(model) {
    var url = base_url + 'dcs/record/' + model + '/last/';
    var heading = $('#th_'+model);
    var title = heading.attr('title');
    heading.html(title + ' [ updating ... ]');
    $.getJSON(url, function(data) {
        var record = data[0].fields;
        var td_field;
        for (field in record) {
            td_field = $('#td_'+model+'__'+field);
            td_field.html(record[field]);
            if (!is_safe(model, field, record[field])) {
                td_field.css('color', 'red');
            }
            else {
                td_field.css('color', 'black');
            }
        }
        heading.html(title + '&nbsp;&nbsp; [ ' + record.date_time + ' ]');
        // console.log(parse_datetime(record.date_time));
        // now = new Date();
        // console.log(now.getTime());
    });
}

function load_model(model) {
    var url = base_url + 'dcs/data/' + model + '/latest/days/' + latest_days + '/';
    $.getJSON(url, function(data) {
        DcsData[model] = data;
        var i;
        for (i=0; i<data.length; i++) {
            row = DcsData[model][i].fields;
            row.date_time = parse_datetime(row.date_time);
        }
        if (configs[model]) {
            for (field in configs[model]) {
                init_chart(model, field, configs[model][field]);
            }
        }
    }); // .getJSON done
}

function init_chart(model, field, options) {
    highchartsOptions = {
       chart: { renderTo: model + '__' + field },
       title: { text: options[0] },
       yAxis: { endOnTick: true },
       series: [{ animation: false,
             data: convert_data(DcsData[model],field)
           }
       ]
    };
    if (options[1] && options[2]) {
        highchartsOptions.yAxis.min = options[1];
        highchartsOptions.yAxis.max = options[2];
    }
    if (options[3] && options[4]) {
        highchartsOptions.yAxis.plotBands = [{ // reference band
            from: options[3], to: options[4],
            color: 'rgba(144, 238, 144, 0.1)'
        }];
    }
    charts.push(new Highcharts.Chart(highchartsOptions));
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

function is_safe(model, field, value) {
    if (configs[model][field]) {
        return (configs[model][field][3] <= value) && (configs[model][field][4] >= value);
    }
    else {
        return true;
    }
}

function load_config(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        Ad1Lidsensor : {
            ultrasonic_gdls: ['AD1 GdLS Level: Ultrasonic', 2000, 2400, 2100, 2300],
            ultrasonic_ls: ['AD1 LS Level: Ultrasonic', 1900, 2300, 2000, 2200],
            capacitance_gdls: ['AD1 GdLS Level: Capacitance', 200, 450, 250, 350],
            capacitance_ls: ['AD1 LS Level: Capacitance', 200, 450, 300, 400],
            capacitance_mo: ['AD1 MO Level: Capacitance', 200, 380, 330, 370],
            temp_gdls: ['AD1 GdLS Temperature', 20, 25, 21, 24],
            temp_ls: ['AD1 LS Temperature', 20, 25, 21, 24],
            capacitance_temp_gdls: ['AD1 GdLS Temperature: Capacitance', 23, 28, 24, 27],
            capacitance_temp_ls: ['AD1 LS Temperature: Capacitance', 23, 28, 24, 27],
            capacitance_temp_mo: ['AD1 MO Temperature: Capacitance', 20, 26, 21, 25]
        },
        Ad2Lidsensor : {
            ultrasonic_gdls: ['AD2 GdLS Level: Ultrasonic', 2000, 2400, 2100, 2300],
            ultrasonic_ls: ['AD2 LS Level: Ultrasonic', 1900, 2300, 2000, 2200],
            capacitance_gdls: ['AD2 GdLS Level: Capacitance', 200, 450, 250, 350],
            capacitance_ls: ['AD2 LS Level: Capacitance', 200, 450, 300, 400],
            capacitance_mo: ['AD2 MO Level: Capacitance', 200, 380, 330, 370],
            temp_gdls: ['AD2 GdLS Temperature', 20, 25, 21, 24],
            temp_ls: ['AD2 LS Temperature', 20, 25, 21, 24],
            capacitance_temp_gdls: ['AD2 GdLS Temperature: Capacitance', 23, 28, 24, 27],
            capacitance_temp_ls: ['AD2 LS Temperature: Capacitance', 23, 28, 24, 27],
            capacitance_temp_mo: ['AD2 MO Temperature: Capacitance', 20, 26, 21, 25]
        },
        DbnsIowTemp : {
            dbns_iw_temp_pt1: ['Inner WP Temerature: 1', 21, 26, 22, 25],
            dbns_iw_temp_pt2: ['Inner WP Temerature: 2', 21, 26, 22, 25],
            dbns_iw_temp_pt3: ['Inner WP Temerature: 3', 21, 26, 22, 25],
            dbns_iw_temp_pt4: ['Inner WP Temerature: 4', 21, 26, 22, 25],
            dbns_ow_temp_pt1: ['Outer WP Temerature: 1', 21, 26, 22, 25],
            dbns_ow_temp_pt2: ['Outer WP Temerature: 2', 21, 26, 22, 25],
            dbns_ow_temp_pt3: ['Outer WP Temerature: 3', 21, 26, 22, 25],
            dbns_ow_temp_pt4: ['Outer WP Temerature: 4', 21, 26, 22, 25]
        },
        DbnsRpcGas101 : {
            pressure_argon: ['RPC Argon Pressure', 18, 22, 19, 21],
            pressure_isobutane: ['RPC Isobutane Pressure', 18, 22, 19, 21],
            pressure_r134a: ['RPC R134A Pressure', 18, 22, 19, 21],
            pressure_sf6: ['RPC SF6 Pressure', 18, 22, 19, 21]     
        },
        DbnsEnvPth : {
            dbns_pth_t1: ['EH1 Temperature: 1', 22, 29, 24, 29],        
            dbns_pth_t2: ['EH1 Temperature: 2', 22, 29, 24, 29],        
            dbns_pth_h1: ['EH1 Humidity: 1', 50, 75, 40, 70],        
            dbns_pth_h2: ['EH1 Humidity: 2', 50, 75, 40, 70],        
            dbns_pth_p1: ['EH1 Pressure: 1', false, false, 980, 1030],        
            dbns_pth_p2: ['EH1 Pressure: 2', false, false, 980, 1030]
        }
    };
}
