enable_ajax_csrf();
$('#jumper button').click(function() {
    window.location = $(this).attr('href');
});

var this_url = window.location.href;
var base_url = this_url.substring(0,this_url.indexOf('dbi'));
var model = $('#model').attr('model');

var single_chart = null;
Highcharts.setOptions({
    chart: { type: 'line', zoomType: 'xy', animation: false },
    credits: { enabled: false },
    // legend: { layout: 'vertical', align: 'right', verticalAlign: 'top',
    //    x: -10, y: 100, borderWidth: 0
    // },    
    xAxis: { type: 'datetime' },       
    yAxis: { title: {text: ''} }, // tickPixelInterval: 36
    tooltip: { backgroundColor: '#FCFFC5', formatter: dbi_formatter },
    plotOptions: {
        line: { marker: {
            radius: 3, 
            fillColor: '#FFFFFF', 
            lineWidth: 2,
            lineColor: null } // inherit from series
        }
    }
});

var configs = new Object;
load_configs();

$('#id_detector').change(function(){
    if (model == 'CalibPMTSpec' || model == 'CableMap') {
        var detector = $(this).val();
        if (detector.indexOf('AD') > -1) {
            $('#id_ring').prev('h6').html('Ring');
            $('#id_column').prev('h6').html('Column');
            $('#id_in_out').hide();           
        }
        else {
            $('#id_ring').prev('h6').html('Wall');
            $('#id_column').prev('h6').html('Spot');
            if (detector == 'OWS') {
                $('#id_in_out').show();
            }
        }
    }
});

$("#submit").click(function(){
    if (single_chart) { single_chart.destroy(); }
    $('#single_chart').html('<h3 align="center">Retrieving Data ...</h3>');
    $('#form_errors').empty();  
    var jqxhr = $.post(base_url + 'dbi/trend/'+model+'/', $("#form").serialize(),
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
            // console.log(data);
            var highchartsOptions = {
               chart: { renderTo: 'single_chart' },
               title: { text: '' },
               series: convert_series(data)
            };            
            single_chart = new Highcharts.Chart(highchartsOptions);
        }, "json"); // post done.
    jqxhr.error(function() { 
        ;
    });
    return false;
});

function convert_data(data, field) {
    var data_xy = new Array();
    var i, row, value;
    var length = data.length;
    for (i=0; i<length; i++) {
        row = data[i];
        value = row[field];
        data_xy.push({
            x: parse_datetime(row.start),
            y: value,
            name: format_name(row, field)
        });
        if (i < length-1) {
            data_xy.push({
                x: parse_datetime(row.end)-1,
                y: value,
                name: format_name(row, field),
                marker: {radius: 0}
            });
        }
        else {
            data_xy.push({
                x: parse_datetime(row.start)+86400000*15,
                y: value,
                name: format_name(row, field),
                marker: {radius: 0}
            });
        }
    }
    // console.log(data_xy);
    return data_xy;
}

function convert_series(data) {
    var series = [];
    
    var fields = [];
    fields.push($('#id_field').val()); // one field for now
    // console.log(fields);
    var i, field;
    for (i=0; i<fields.length; i++) {
        field = fields[i];
        series.push({
            name: configs[model][field]['title'],
            animation: false,
            data: convert_data(data, field)
        });
    }    
    return series;
}

// utility functions
function format_name(row, field) {
    str = '';
    if (model == 'EnergyRecon') {
        str += '[PE to Evis(MeV)] <b>' + row.peevis + ' +/- ' + row.peevisunc + '</b><br/>';
    }
    else if (model == 'CalibPMTSpec') {
        str += '[High Gain SPE] <b>' + row.pmtspehigh + '</b> ADC<br/>'
             + '[Low Gain SPE] <b>' + row.pmtspelow + '</b> ADC<br/>'
             + '[Time Offset] <b>' + row.pmttoffset + '</b> TDC<br/>';
    }
    else if (model == 'CableMap') {
        str += '[Board-Connector] <b>' + row.board + '-' + row.connector + '</b><br/>';
    }
    return str
        + '[From] <b>' + row.start + '</b><br/>'
        + '[To] <b>' + row.end + '</b><br/>'
        + '[seqno] <b>' + row.seqno + '</b>';
}

function dbi_formatter() {
    return this.point.name;
}

function parse_datetime(datetime) {
    // dcs is beijing time
    var first_second = datetime.split(' ');
    var date = first_second[0].split('-');
    var time = first_second[1].split(':');
    return Date.UTC(date[0], date[1]-1, date[2], time[0], time[1], time[2]);
}

function load_configs() {
    configs = {
        'EnergyRecon' : {
          'peevis' : {'title' : 'PE to Visible Energy(MeV)'}
        },
        'CalibPMTSpec' : {
          'pmtspehigh' : {'title' : 'High Gain SPE [ADC]'},
          'pmtspelow'  : {'title' : 'Low Gain SPE [ADC]'},
          'pmttoffset' : {'title' : 'Time Offset [TDC]'}
        },
        'CableMap' : {
          'board' : {'title' : 'Board'},
          'connector'  : {'title' : 'Connector'}
        }
    };
}     