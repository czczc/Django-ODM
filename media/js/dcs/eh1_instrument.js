load_configs();
load_tooltips();
load_all_models();
fetch_latest();
// var timer = setInterval('fetch_latest()', 300000);
// console.log(configs);

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
    // load_model('DbnsIowTemp');
    load_model('DbnsRpcGas101');
    load_model('DbnsEnvPth');

}

function fetch_latest() {
    fetch_one('Ad1Lidsensor');
    fetch_one('Ad2Lidsensor');
    // fetch_one('DbnsIowTemp');
    fetch_one('DbnsRpcGas101');
    fetch_one('DbnsEnvPth');
}

function load_configs(){
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
