enable_ajax_csrf();

var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('dcs'));

var single_chart = null;
Highcharts.setOptions({
    chart: { type: 'scatter', zoomType: 'xy', animation: false },
    credits: { enabled: false },
    // legend: { enabled: false },
    xAxis: { type: 'datetime' },       
    yAxis: { title: {text: ''}, tickPixelInterval: 36 },
    tooltip: { formatter: datetime_formatter },
    plotOptions: {
        scatter: { marker: {radius: 1.5} }
    }
});

init_searchform();

function init_searchform() {
    $("#id_date_from").datepicker({ defaultDate: +0 });
    $("#id_date_to").datepicker({ defaultDate: +0 });
    $('option[value="All"]').css('color', 'red');
}

$('#id_model').change(function(){
    var model = $(this).val();
    $.getJSON( base_url + 'dcs/model/' + model +'/fields/', function(data) {
        var html = '';
        var i;
        for ( i in data) {
            html += '<option value="' + data[i] + '">' + data[i] + '</option>';
        }
        $('#id_fields').html(html);
    }); // .getJSON done
});

$("#submit").click(function(){
    if (single_chart) { single_chart.destroy(); }  
    var jqxhr = $.post(base_url + 'dcs/', $("#form").serialize(),
        function(data) {
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