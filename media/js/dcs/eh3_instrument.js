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
    load_model('Ad5Lidsensor');
    load_model('Ad6Lidsensor');
    // load_model('LansIowTemp');
    // load_model('LansRpcGas101');
    // load_model('LansEnvPth');

}

function fetch_latest() {
    fetch_one('Ad4Lidsensor');
    fetch_one('Ad5Lidsensor');
    fetch_one('Ad6Lidsensor');
    // fetch_one('LansIowTemp');
    // fetch_one('LansRpcGas101');
    // fetch_one('LansEnvPth');
}

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        Ad4Lidsensor : {
            //ultrasonic_gdls:  ['AD4 GdLS Level: Ultrasonic',  65, 95, 70, 90],
            ultrasonic_gdls:  ['AD4 GdLS Level: Ultrasonic',  43, 95, 70, 90],
            ultrasonic_ls:    ['AD4 LS Level: Ultrasonic',    43, 95, 70, 90],
            capacitance_gdls: ['AD4 GdLS Level: Capacitance', 43, 95, 70, 90],
            capacitance_ls:   ['AD4 LS Level: Capacitance',   43, 95, 70, 90],
            capacitance_mo:   ['AD4 MO Level: Capacitance',   43, 95, 70, 90],
            temp_gdls:        ['AD4 GdLS Temperature', 21, 25, 22.4, 23],
            temp_ls:          ['AD4 LS Temperature',   21, 25, 22.4, 23],
            //capacitance_temp_gdls: ['AD4 GdLS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD4 LS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD4 MO Temperature: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD4 Tilt X1 [deg]', -2, 2, -0.24, -0.20],
            tiltx_sensor2: ['AD4 Tilt X2 [deg]', -2, 2, -0.17, -0.13],
            tiltx_sensor3: ['AD4 Tilt X3 [deg]', -2, 2, -0.55, -0.51],
            tilty_sensor1: ['AD4 Tilt Y1 [deg]', -2, 2, -0.32, -0.28],
            tilty_sensor2: ['AD4 Tilt Y2 [deg]', -2, 2,  0.95,  0.99],
            tilty_sensor3: ['AD4 Tilt Y3 [deg]', -2, 2,  0.78,  0.82]
        },
        Ad5Lidsensor : {
            ultrasonic_gdls:  ['AD5 GdLS Level: Ultrasonic',  43, 95, 70, 90],
            ultrasonic_ls:    ['AD5 LS Level: Ultrasonic',    43, 95, 70, 90],
            capacitance_gdls: ['AD5 GdLS Level: Capacitance', 43, 95, 70, 90],
            capacitance_ls:   ['AD5 LS Level: Capacitance',   43, 95, 70, 90],
            capacitance_mo:   ['AD5 MO Level: Capacitance',   43, 95, 70, 90],
            temp_gdls:        ['AD5 GdLS Temperature', 21, 25, 22.4, 23],
            temp_ls:          ['AD5 LS Temperature',   21, 25, 22.4, 23],
            //capacitance_temp_gdls: ['AD5 GdLS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD5 LS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD5 MO Temperature: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD5 Tilt X1 [deg]', -2, 2, -1.15, -1.11],
            tiltx_sensor2: ['AD5 Tilt X2 [deg]', -2, 2, -0.18, -0.14],
            tiltx_sensor3: ['AD5 Tilt X3 [deg]', -2, 2, -0.89, -0.85],
            tilty_sensor1: ['AD5 Tilt Y1 [deg]', -2, 2,  0.01,  0.05],
            tilty_sensor2: ['AD5 Tilt Y2 [deg]', -2, 2,  0.83,  0.87],
            tilty_sensor3: ['AD5 Tilt Y3 [deg]', -2, 2,  0.70,  0.74]
        },
        Ad6Lidsensor : {
            ultrasonic_gdls:  ['AD6 GdLS Level: Ultrasonic',  43, 95, 70, 90],
            ultrasonic_ls:    ['AD6 LS Level: Ultrasonic',    43, 95, 70, 90],
            capacitance_gdls: ['AD6 GdLS Level: Capacitance', 43, 95, 70, 90],
            capacitance_ls:   ['AD6 LS Level: Capacitance',   43, 95, 70, 90],
            capacitance_mo:   ['AD6 MO Level: Capacitance',   43, 95, 70, 90],
            temp_gdls:        ['AD6 GdLS Temperature', 21, 25, 22.4, 23],
            temp_ls:          ['AD6 LS Temperature',   21, 25, 22.4, 23],
            //capacitance_temp_gdls: ['AD6 GdLS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD6 LS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD6 MO Temperature: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD6 Tilt X1 [deg]', -2, 2, -0.16, -0.12],
            tiltx_sensor2: ['AD6 Tilt X2 [deg]', -2, 2, -0.71, -0.67],
            tiltx_sensor3: ['AD6 Tilt X3 [deg]', -2, 2, -0.69, -0.65],
            tilty_sensor1: ['AD6 Tilt Y1 [deg]', -2, 2,  0.02,  0.06],
            tilty_sensor2: ['AD6 Tilt Y2 [deg]', -2, 2,  0.35,  0.39],
            tilty_sensor3: ['AD6 Tilt Y3 [deg]', -2, 2, -0.14, -0.10]
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
