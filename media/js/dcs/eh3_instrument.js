load_configs();
load_tooltips();
fetch_latest();
load_all_models();
var timer = setInterval('fetch_latest()', 300000);

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

    load_model('Ad4Lidsensor');
    // load_model('LansIowTemp');
    // load_model('LansRpcGas101');
    // load_model('LansEnvPth');

}

function fetch_latest() {
    fetch_one('Ad4Lidsensor');
    // fetch_one('LansIowTemp');
    // fetch_one('LansRpcGas101');
    // fetch_one('LansEnvPth');
}

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        Ad4Lidsensor : {
            ultrasonic_gdls: ['AD4 GdLS Level: Ultrasonic', 65, 95, 70, 90],
            ultrasonic_ls: ['AD4 LS Level: Ultrasonic', 65, 95, 70, 90],
            capacitance_gdls: ['AD4 GdLS Level: Capacitance', 200, 450, 250, 350],
            capacitance_ls: ['AD4 LS Level: Capacitance', 200, 450, 300, 400],
            capacitance_mo: ['AD4 MO Level: Capacitance', 65, 95, 70, 90],
            temp_gdls: ['AD4 GdLS Temperature', 20, 25, 21, 24],
            temp_ls: ['AD4 LS Temperature', 20, 25, 21, 24],
            capacitance_temp_gdls: ['AD4 GdLS Temperature: Capacitance', 23, 28, 24, 27],
            capacitance_temp_ls: ['AD4 LS Temperature: Capacitance', 23, 28, 24, 27],
            capacitance_temp_mo: ['AD4 MO Temperature: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD4 Tilt X : 1', -2, 2, -1.5, -0.5],
            tiltx_sensor2: ['AD4 Tilt X : 2', -2, 2, -1, 1],
            tiltx_sensor3: ['AD4 Tilt X : 3', -2, 2, -1, 1],
            tilty_sensor1: ['AD4 Tilt Y : 1', -2, 2, -1, 1],
            tilty_sensor2: ['AD4 Tilt Y : 2', -2, 2, -1, 1],
            tilty_sensor3: ['AD4 Tilt Y : 3', -2, 2, 0.5, 1.5]
        }
        // LansIowTemp : {
        //     lans_iw_temp_pt1: ['Inner WP Temerature: 1', 20, 26, 22, 25],
        //     lans_iw_temp_pt2: ['Inner WP Temerature: 2', 20, 26, 22, 25],
        //     lans_iw_temp_pt3: ['Inner WP Temerature: 3', 20, 26, 22, 25],
        //     lans_iw_temp_pt4: ['Inner WP Temerature: 4', 20, 26, 22, 25],
        //     lans_ow_temp_pt1: ['Outer WP Temerature: 1', 20, 26, 22, 25],
        //     lans_ow_temp_pt2: ['Outer WP Temerature: 2', 20, 26, 22, 25],
        //     lans_ow_temp_pt3: ['Outer WP Temerature: 3', 20, 26, 22, 25],
        //     lans_ow_temp_pt4: ['Outer WP Temerature: 4', 20, 26, 22, 25]
        // }
        // LansRpcGas101 : {
        //     pressure_argon: ['RPC Argon Pressure', 18, 23, 19, 22],
        //     pressure_isobutane: ['RPC Isobutane Pressure', 18, 22, 19, 22],
        //     pressure_r134a: ['RPC R134A Pressure', 18, 22, 19, 22],
        //     pressure_sf6: ['RPC SF6 Pressure', 18, 22, 19, 22]     
        // },
        // LansEnvPth : {
        //     lans_pth_t1: ['EH2 Temperature: 1', 22, 29, 24, 29],        
        //     lans_pth_t2: ['EH2 Temperature: 2', 22, 29, 24, 29],        
        //     lans_pth_h1: ['EH2 Humidity: 1', 50, 75, 40, 70],        
        //     lans_pth_h2: ['EH2 Humidity: 2', 50, 75, 40, 70],        
        //     lans_pth_p1: ['EH2 Pressure: 1', false, false, 980, 1030],        
        //     lans_pth_p2: ['EH2 Pressure: 2', false, false, 980, 1030]
        // }
    };
}
