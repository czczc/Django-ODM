var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('dcs'));
$('button').button();
$('.th_last_update').qtip({
    content: 'auto-updates every 5 min',
    position: {corner: {target: 'topMiddle', tooltip: 'bottomLeft'}},
    style: {
        width: 200,
        name: 'cream'
    }
});

Highcharts.setOptions({
    chart: { type: 'scatter', zoomType: 'xy', animation: false, alignTicks: false },
    credits: { enabled: false },
    legend: { enabled: false },
    xAxis: { type: 'datetime' },       
    yAxis: { title: {text: ''}, tickPixelInterval: 24, endOnTick: false },
    tooltip: { formatter: datetime_formatter },
    plotOptions: {
        scatter: { marker: {radius: 1} }
    }
});
var latest_days = 30;
var charts = [];
var DcsData = new Object;
var single_chart = null;

// sc == show chart

$('.sc').hover(function() {
    $(this).css('cursor','pointer');
}, function() {
    $(this).css('cursor','auto');
}).click(function() {
    var str = $(this).attr('id').substring(3);
    var model_field = str.split('__');
    var model = model_field[0];
    var field = model_field[1];
    var url = base_url + 'dcs/data/' + model + '/latest/days/7/';
    $.modal('<div style="height:200px; width: 640px;" id="single_chart"><h1 style="color: white;">Retrieving Data ... (may take a few seconds)</h1></div>',
        {
            'overlayClose' : true
        }
    );
    $.getJSON(url, function(data) {
        var i;
        for (i=0; i<data.length; i++) {
            row = data[i].fields;
            row.date_time = parse_datetime(row.date_time);
        }
        options = configs[model][field];
        var highchartsOptions = {
           chart: { renderTo: 'single_chart' },
           title: { text: options[0] },
           yAxis: { endOnTick: true },
           series: [{ animation: false,
                 data: convert_data(data, model, field)
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
        if (single_chart) { single_chart.destroy(); }
        single_chart = new Highcharts.Chart(highchartsOptions);
    })
    .error(function(){
        $('#single_chart').html('<h1 style="color: white;">Error retrieving data ...</h1>');
    }); // .getJSON done
});



function fetch_one(model) {
    var url = base_url + 'dcs/record/' + model + '/last/';
    var th_last_update = $('#th_'+model).next('.th_last_update');
    // var title = heading.attr('title');
    th_last_update.html('updating ...');
    var value;
    $.getJSON(url, function(data) {
        var record = data[0].fields;
        var td_field;
        for (field in record) {
            td_field = $('#td_'+model+'__'+field);
            value = apply_formular(record[field], model, field);
            td_field.html(sprintf("%.2f", value));
            if (!is_safe(model, field, value)) {
                td_field.addClass('warning');
            }
            else {
                td_field.removeClass('warning');                
            }
        }
        th_last_update.html(record.date_time);
        var now = new Date();
        var now_time_ms = now.getTime();
        // confused, why the extra 4 hours?
        var dt_min = (now_time_ms - parse_datetime(record.date_time))/60000 + 240 + now.getTimezoneOffset();
        if (dt_min>15) { 
            th_last_update.removeClass('good').addClass('warning');
        }
        else { 
            th_last_update.removeClass('warning').addClass('good'); 
        }
    })
    .error(function(){
        th_last_update.html('updating failed');
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
                if ($('#' + model + '__' + field).length>0) {
                    init_chart(model, field, configs[model][field]);
                }
            }
        }
    }); // .getJSON done
}

function init_chart(model, field, options) {
    var highchartsOptions = {
       chart: { renderTo: model + '__' + field },
       title: { text: options[0] },
       yAxis: { endOnTick: true },
       series: [{ animation: false,
             data: convert_data(DcsData[model], model, field)
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

function convert_data(rawdata, model, field) {
    var data_xy = new Array();
    var i, row, value, f;
    for (i=0; i<rawdata.length; i++) {
        row = rawdata[i].fields;
        value = apply_formular(parseFloat(row[field]), model, field);
        data_xy.push([row.date_time, value]);
    }
    return data_xy;
}

function apply_formular(value, model, field) {
    var f;
    if (formulas[model]) {
        f = formulas[model][field];
        if (f) {
            value = f(value);
        }
    }
    return value;
}

function parse_datetime(datetime) {
    // dcs is beijing time
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

// execute this after loading all configs. 
function load_tooltips() {
    $('.sc').each(function() {
        var str = $(this).attr('id').substring(3);
        var model_field = str.split('__');
        var model = model_field[0];
        var field = model_field[1];
        var safemin = '-'; 
        if (configs[model][field]) { safemin = configs[model][field][3]; };
        var safemax = '-';
        if (configs[model][field]) { safemax = configs[model][field][4]; };
        $(this).qtip({
            content:  '<h4 align="center">' + field + '</h4><br />'
                + 'Ref. Values: <span style="color:green; font-weight: bold;"> ' 
                + safemin + ' - ' + safemax + '</span><br />Click to show last week',
            position: {corner: {target: 'topMiddle', tooltip: 'bottomLeft'}},
            style: {
                width: 200,
                name: 'light',
                tooltip: 'bottomLeft'
            }
        });
    });
}
