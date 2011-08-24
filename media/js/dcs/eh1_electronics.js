load_configs();
load_tooltips();
fetch_latest();
load_all_models();
var timer = setInterval('fetch_latest()', 300000);

$('a.HV').click(function(){
    var ladder = $(this).attr('id');
    $('#table_'+ladder).toggle("blind").addClass('current'); 
    return false; 
});

function load_all_models() {
    var i;
    for (i=0; i<charts.length; i++) {
        charts[i].destroy();
    }
    charts.length = 0;
}

function fetch_latest() {
    HV_fetch_one('DbnsAd1Hv');
    HV_fetch_one('DbnsAd2Hv');
    fetch_one('DbnsRpcHvVmon');
    fetch_one('DbnsAd1Vme');
    fetch_one('DbnsAd2Vme');
    fetch_one('DbnsIWVme');
    fetch_one('DbnsOWVme');
    fetch_one('DbnsRPCVme');
}

function HV_fetch_one(model) {
    var url = base_url + 'dcs/record/' + model + '/last/';
    var th_last_update = $('#th_'+model).next('.th_last_update');
    th_last_update.html('updating ...');
    $.getJSON(url, function(data) {
        $('#table_'+model+' .HV').removeClass('down').addClass('live');
        var record = data[0].fields;
        var td_field;
        for (field in record) {
            td_field = $('#td_'+model+'__'+field);
            td_field.html(record[field]);
            if (!is_safe(model, field, record[field])) {
                a_ladder = $('#'+model+'__'+field.substring(0,2));
                if (!a_ladder.hasClass('down')) {
                    a_ladder.removeClass('live').addClass('down');
                }
                td_field.addClass('warning');
            }
            else {
                td_field.removeClass('warning');                
            }
        }
        th_last_update.html(record.date_time);
        var now = new Date();
        var now_time_ms = now.getTime();
        var dt_min = (now_time_ms - parse_datetime(record.date_time))/360000;
        if (dt_min>15) { 
            th_last_update.removeClass('good').addClass('warning');
        }
        else { 
            th_last_update.removeClass('warning').addClass('good'); 
        }
    })
    .error(function(){
        th_last_update.html('updating failed (tunnel down)');
    });
}

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        DbnsAd1Hv : {},
        DbnsAd2Hv : {},
        DbnsRpcHvVmon : {},
        DbnsAd1Vme : {},
        DbnsAd2Vme : {},
        DbnsIWVme : {},
        DbnsOWVme : {},
        DbnsRPCVme : {}
    };
    var ladder, row, column, field;
    for (ladder=1; ladder<=8; ladder++) {
        for (row=1; row<=8; row++) {
            for (column=1; column<=3; column++) {
                field = 'l'+ladder+'c'+column+'r'+row;
                configs.DbnsAd1Hv[field] = [field, 1100, 2000, 1200, 1900];
                configs.DbnsAd2Hv[field] = [field, 1100, 2000, 1200, 1900];
            }
        }
    }
    var channel;
    for (channel=0; channel<=23; channel++) {
        field = sprintf('dbns_fo%02dn', channel);
        configs.DbnsRpcHvVmon[field] = [field, 3000, 4000, 3500, 3900];
    }
    var tp;
    for (tp=1; tp<=8; tp++) {
        field = 'temperature' + tp;
        configs.DbnsAd1Vme[field] = [field, 15, 40, 20, 30];
        configs.DbnsAd2Vme[field] = [field, 15, 40, 20, 30];
        configs.DbnsIWVme[field]  = [field, 15, 40, 20, 30];
        configs.DbnsOWVme[field]  = [field, 15, 40, 20, 30];
        configs.DbnsRPCVme[field] = [field, 15, 40, 20, 30];
    }
}

