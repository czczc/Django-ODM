load_configs();
load_tooltips();
fetch_latest();
load_all_models();
var timer = setInterval('fetch_latest()', 300000);

$('a.HV').click(function(){
    var group = $(this).attr('id');
    $('#table_'+group).toggle("blind");
    $(this).parent('td').toggleClass('on_display'); 
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
    HV_fetch_one('DbnsMuonPmtHvVmon');
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
        var td_field, group;
        for (field in record) {
            td_field = $('#td_'+model+'__'+field);
            td_field.html(record[field]);
            if (!is_safe(model, field, record[field])) {
                group = $('#'+model+'__'+td_field.attr('group')); //$('#'+model+'__'+field.substring(0,2));
                if (!group.hasClass('down')) {
                    group.removeClass('live').addClass('down');
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

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        DbnsAd1Hv : {},
        DbnsAd2Hv : {},
        DbnsMuonPmtHvVmon : {},
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
    
    configs.DbnsMuonPmtHvVmon['dciu3g'] = ['dciu3g', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu3f'] = ['dciu3f', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu3e'] = ['dciu3e', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu3d'] = ['dciu3d', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu3c'] = ['dciu3c', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu3b'] = ['dciu3b', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu3a'] = ['dciu3a', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu39'] = ['dciu39', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu38'] = ['dciu38', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu37'] = ['dciu37', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu36'] = ['dciu36', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu35'] = ['dciu35', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu34'] = ['dciu34', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu33'] = ['dciu33', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu32'] = ['dciu32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu31'] = ['dciu31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu24'] = ['dciu24', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu23'] = ['dciu23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu22'] = ['dciu22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu21'] = ['dciu21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dciu11'] = ['dciu11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih42'] = ['dcih42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih41'] = ['dcih41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih32'] = ['dcih32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih31'] = ['dcih31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih22'] = ['dcih22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih21'] = ['dcih21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih12'] = ['dcih12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcih11'] = ['dcih11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig72'] = ['dcig72', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig63'] = ['dcig63', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig61'] = ['dcig61', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig52'] = ['dcig52', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig43'] = ['dcig43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig41'] = ['dcig41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig32'] = ['dcig32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig23'] = ['dcig23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig21'] = ['dcig21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcig12'] = ['dcig12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif42'] = ['dcif42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif41'] = ['dcif41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif32'] = ['dcif32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif31'] = ['dcif31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif22'] = ['dcif22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif21'] = ['dcif21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif12'] = ['dcif12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcif11'] = ['dcif11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie76'] = ['dcie76', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie74'] = ['dcie74', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie72'] = ['dcie72', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie67'] = ['dcie67', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie65'] = ['dcie65', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie63'] = ['dcie63', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie61'] = ['dcie61', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie56'] = ['dcie56', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie54'] = ['dcie54', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie52'] = ['dcie52', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie47'] = ['dcie47', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie45'] = ['dcie45', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie43'] = ['dcie43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie41'] = ['dcie41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie36'] = ['dcie36', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie34'] = ['dcie34', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie32'] = ['dcie32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie27'] = ['dcie27', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie25'] = ['dcie25', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie23'] = ['dcie23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie21'] = ['dcie21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie16'] = ['dcie16', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie14'] = ['dcie14', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcie12'] = ['dcie12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid42'] = ['dcid42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid41'] = ['dcid41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid32'] = ['dcid32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid31'] = ['dcid31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid22'] = ['dcid22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid21'] = ['dcid21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid12'] = ['dcid12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcid11'] = ['dcid11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic72'] = ['dcic72', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic63'] = ['dcic63', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic61'] = ['dcic61', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic52'] = ['dcic52', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic43'] = ['dcic43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic41'] = ['dcic41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic32'] = ['dcic32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic23'] = ['dcic23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic21'] = ['dcic21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcic12'] = ['dcic12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib42'] = ['dcib42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib41'] = ['dcib41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib32'] = ['dcib32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib31'] = ['dcib31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib22'] = ['dcib22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib21'] = ['dcib21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib12'] = ['dcib12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcib11'] = ['dcib11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia76'] = ['dcia76', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia74'] = ['dcia74', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia72'] = ['dcia72', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia67'] = ['dcia67', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia65'] = ['dcia65', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia63'] = ['dcia63', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia61'] = ['dcia61', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia56'] = ['dcia56', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia54'] = ['dcia54', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia52'] = ['dcia52', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia47'] = ['dcia47', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia45'] = ['dcia45', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia43'] = ['dcia43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia41'] = ['dcia41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia36'] = ['dcia36', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia34'] = ['dcia34', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia32'] = ['dcia32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia27'] = ['dcia27', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia25'] = ['dcia25', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia23'] = ['dcia23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia21'] = ['dcia21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia16'] = ['dcia16', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia14'] = ['dcia14', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dcia12'] = ['dcia12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dviu26'] = ['dviu26', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dviu35'] = ['dviu35', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dviu24'] = ['dviu24', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dviu23'] = ['dviu23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dviu22'] = ['dviu22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dviu21'] = ['dviu21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dviu11'] = ['dviu11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvohf3'] = ['dvohf3', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvohf1'] = ['dvohf1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvogf1'] = ['dvogf1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoff3'] = ['dvoff3', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoff1'] = ['dvoff1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoef3'] = ['dvoef3', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoef2'] = ['dvoef2', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoef1'] = ['dvoef1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvodf3'] = ['dvodf3', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvodf1'] = ['dvodf1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvocf1'] = ['dvocf1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvobf3'] = ['dvobf3', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvobf1'] = ['dvobf1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoaf3'] = ['dvoaf3', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoaf2'] = ['dvoaf2', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoaf1'] = ['dvoaf1', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh42'] = ['dvoh42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh41'] = ['dvoh41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh32'] = ['dvoh32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh31'] = ['dvoh31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh22'] = ['dvoh22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh21'] = ['dvoh21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh12'] = ['dvoh12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoh11'] = ['dvoh11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih42'] = ['dvih42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih41'] = ['dvih41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih32'] = ['dvih32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih31'] = ['dvih31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih22'] = ['dvih22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih21'] = ['dvih21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih12'] = ['dvih12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvih11'] = ['dvih11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvog41'] = ['dvog41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvog31'] = ['dvog31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvog21'] = ['dvog21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvog11'] = ['dvog11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig42'] = ['dvig42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig41'] = ['dvig41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig32'] = ['dvig32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig31'] = ['dvig31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig22'] = ['dvig22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig21'] = ['dvig21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig12'] = ['dvig12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvig11'] = ['dvig11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof42'] = ['dvof42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof41'] = ['dvof41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof32'] = ['dvof32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof31'] = ['dvof31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof22'] = ['dvof22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof21'] = ['dvof21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof12'] = ['dvof12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvof11'] = ['dvof11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif42'] = ['dvif42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif41'] = ['dvif41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif32'] = ['dvif32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif31'] = ['dvif31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif22'] = ['dvif22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif21'] = ['dvif21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif12'] = ['dvif12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvif11'] = ['dvif11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe43'] = ['dvoe43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe42'] = ['dvoe42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe41'] = ['dvoe41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe33'] = ['dvoe33', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe32'] = ['dvoe32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe31'] = ['dvoe31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe23'] = ['dvoe23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe22'] = ['dvoe22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe21'] = ['dvoe21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe13'] = ['dvoe13', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe12'] = ['dvoe12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoe11'] = ['dvoe11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie44'] = ['dvie44', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie43'] = ['dvie43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie42'] = ['dvie42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie41'] = ['dvie41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie34'] = ['dvie34', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie33'] = ['dvie33', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie32'] = ['dvie32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie31'] = ['dvie31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie24'] = ['dvie24', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie23'] = ['dvie23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie22'] = ['dvie22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie21'] = ['dvie21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie14'] = ['dvie14', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie13'] = ['dvie13', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie12'] = ['dvie12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvie11'] = ['dvie11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod42'] = ['dvod42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod41'] = ['dvod41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod32'] = ['dvod32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod31'] = ['dvod31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod22'] = ['dvod22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod21'] = ['dvod21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod12'] = ['dvod12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvod11'] = ['dvod11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid42'] = ['dvid42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid41'] = ['dvid41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid32'] = ['dvid32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid31'] = ['dvid31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid22'] = ['dvid22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid21'] = ['dvid21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid12'] = ['dvid12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvid11'] = ['dvid11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoc41'] = ['dvoc41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoc31'] = ['dvoc31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoc21'] = ['dvoc21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoc11'] = ['dvoc11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic42'] = ['dvic42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic41'] = ['dvic41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic32'] = ['dvic32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic31'] = ['dvic31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic22'] = ['dvic22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic21'] = ['dvic21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic12'] = ['dvic12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvic11'] = ['dvic11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob42'] = ['dvob42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob41'] = ['dvob41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob32'] = ['dvob32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob31'] = ['dvob31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob22'] = ['dvob22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob21'] = ['dvob21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob12'] = ['dvob12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvob11'] = ['dvob11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib42'] = ['dvib42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib41'] = ['dvib41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib32'] = ['dvib32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib31'] = ['dvib31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib22'] = ['dvib22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib21'] = ['dvib21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib12'] = ['dvib12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvib11'] = ['dvib11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa43'] = ['dvoa43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa42'] = ['dvoa42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa41'] = ['dvoa41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa33'] = ['dvoa33', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa32'] = ['dvoa32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa31'] = ['dvoa31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa23'] = ['dvoa23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa22'] = ['dvoa22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa21'] = ['dvoa21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa13'] = ['dvoa13', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa12'] = ['dvoa12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvoa11'] = ['dvoa11', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia44'] = ['dvia44', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia43'] = ['dvia43', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia42'] = ['dvia42', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia41'] = ['dvia41', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia34'] = ['dvia34', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia33'] = ['dvia33', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia32'] = ['dvia32', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia31'] = ['dvia31', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia24'] = ['dvia24', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia23'] = ['dvia23', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia22'] = ['dvia22', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia21'] = ['dvia21', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia14'] = ['dvia14', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia13'] = ['dvia13', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia12'] = ['dvia12', 1100, 2000, 1200, 1900];
    configs.DbnsMuonPmtHvVmon['dvia11'] = ['dvia11', 1100, 2000, 1200, 1900];
}

