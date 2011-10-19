enable_ajax_csrf();

var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('dcs'));
var site = $("#site_label").html();

var single_chart = null;
Highcharts.setOptions({
    chart: { type: 'scatter', zoomType: 'xy', animation: false },
    credits: { enabled: false },
    // legend: { layout: 'vertical', align: 'right', verticalAlign: 'top',
    //    x: -10, y: 100, borderWidth: 0
    // },    
    xAxis: { type: 'datetime' },       
    yAxis: { title: {text: ''}, tickPixelInterval: 36 },
    tooltip: { formatter: datetime_formatter },
    plotOptions: {
        scatter: { marker: {radius: 1.5} },
        line: { marker: {radius: 1.5} }
    }

});

init_searchform();
reload_form('#id_model', '#id_fields');

function init_searchform() {
    $("#id_date_from").datepicker({ defaultDate: +0 });
    $("#id_date_to").datepicker({ defaultDate: +0 });
    $('option[value="All"]').css('color', 'red');
}

function reload_form(selector_model, selector_fields) {
    var model = $(selector_model).val();
    $.getJSON( base_url + 'dcs/model/' + model +'/fields/', function(data) {
        var html = '';
        var i;
        for (i in data) {
            html += '<option value="' + data[i] + '">' + data[i] + '</option>';
        }
        $(selector_fields).html(html);
    }); // .getJSON done
}

$('#id_model').change(function(){
    reload_form('#id_model', '#id_fields');
});

$("#submit").click(function(){
    if (single_chart) { single_chart.destroy(); }
    $('#single_chart').html('<h3 align="center">Retrieving Data ...</h3>');
    $('#form_errors').empty();    
    var jqxhr = $.post(base_url + 'dcs/search/' + site + '/', $("#form").serialize(),
        function(data) {
            if (data.errors) { 
                // server form validation failed
                str_error = '';
                for (attr in data.errors) {
                    for (i in data.errors[attr]) { 
                        str_error += '<li>' + attr + ': ' + data.errors[attr][i] + '</li>'; 
                    }
                    $('#form_errors').html(str_error);
                }
                $('#single_chart').html('<h3 align="center">Form Error!</h3>');
                return;
            }
            var i;
            for (i=0; i<data.length; i++) {
                row = data[i].fields;
                row.date_time = parse_datetime(row.date_time);
            }
            var highchartsOptions = {
               chart: { renderTo: 'single_chart' },
               title: { text: '' },
               yAxis: { endOnTick: false },
               series: convert_series(data)
            };
            var y_min = $('#id_y_min').val();
            var y_max = $('#id_y_max').val();
            if (y_min) { highchartsOptions.yAxis.min = parseFloat(y_min); }
            if (y_max) { highchartsOptions.yAxis.max = parseFloat(y_max); }
            var plot_type = $('#id_plot_type').val();
            if (plot_type) { highchartsOptions.chart.type = plot_type; }
            
            single_chart = new Highcharts.Chart(highchartsOptions);
        }, "json"); // post done.
    jqxhr.error(function() { 
        ;
    });
    return false;
});




// utility functions
function datetime_formatter() {
    return '<b>'+ this.series.name +'</b> : ' + this.y + '<br/>'+
    // return 'Value: ' + this.y + '<br/>'+
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

function convert_series(data) {
    var series = [];
    if (data[0]) {
        for (attr in data[0].fields) {
            if (attr == 'date_time') { continue; }
            series.push({
                name: attr,
                animation: false,
                data: convert_data(data, attr)
            });
        }    
    }
    return series;
}

function parse_datetime(datetime) {
    // dcs is beijing time
    var first_second = datetime.split(' ');
    var date = first_second[0].split('-');
    var time = first_second[1].split(':');
    return Date.UTC(date[0], date[1]-1, date[2], time[0], time[1], time[2]);
}