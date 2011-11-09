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

    load_model('Ad3Lidsensor');
    load_model('Ad3Adcovergas');
    load_model('LansIowTemp');
    load_model('LansRpcGas101');
    load_model('LansRpcGas102');
    // load_model('LansEnvPth');

}

function fetch_latest() {
    fetch_one('Ad3Lidsensor');
    fetch_one('Ad3Adcovergas');
    fetch_one('LansIowTemp');
    fetch_one('LansRpcGas101');
    fetch_one('LansRpcGas102');
    // fetch_one('LansEnvPth');
}

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        Ad3Lidsensor : {
            ultrasonic_gdls: ['AD3 GdLS Level: Ultrasonic [mm]', 65, 95, 70, 90],
            ultrasonic_ls: ['AD3 LS Level: Ultrasonic [mm]', 65, 95, 70, 90],
            capacitance_gdls: ['AD3 GdLS Level: Capacitance', 200, 450, 250, 350],
            capacitance_ls: ['AD3 LS Level: Capacitance', 200, 450, 300, 400],
            capacitance_mo: ['AD3 MO Level: Capacitance', 65, 95, 70, 90],
            temp_gdls: ['AD3 GdLS Temperature [C]', 20, 25, 21, 24],
            temp_ls: ['AD3 LS Temperature [C]', 20, 25, 21, 24],
            capacitance_temp_gdls: ['AD3 GdLS Temperature [C]: Capacitance', 23, 28, 24, 27],
            capacitance_temp_ls: ['AD3 LS Temperature [C]: Capacitance', 23, 28, 24, 27],
            capacitance_temp_mo: ['AD3 MO Temperature [C]: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD3 Tilt X : 1', -2, 2, -1.5, -0.5],
            tiltx_sensor2: ['AD3 Tilt X : 2', -2, 2, -1, 1],
            tiltx_sensor3: ['AD3 Tilt X : 3', -2, 2, -1, 1],
            tilty_sensor1: ['AD3 Tilt Y : 1', -2, 2, -1, 1],
            tilty_sensor2: ['AD3 Tilt Y : 2', -2, 2, -1, 1],
            tilty_sensor3: ['AD3 Tilt Y : 3', -2, 2, 0.5, 1.5]
        },
        Ad3Adcovergas : {
            supplypressure: ['AD3 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD3 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD3 Cover Gas Return [%]', 0.1, 15, 0.1, 10],
            humidity_electricaldrypipereturn: ['Humidity: AD3 Elec. Dry Pipe Return [%]', 0.1, 100, 0.1, 100],
            humidity_gasdrypipereturn: ['Humidity: AD3 Gas Dry Pipe Return [%]', 0.1, 15, 0.001, 10],
            humidity_pmtcablebellowreturn: ['Humidity: AD3 PMT Cable Bellow Return [%]', 0.1, 15, 0.1, 10]
        },
        LansIowTemp : {
            lans_iw_temp_pt1: ['Inner WP Temerature: 1', 20, 26, 22, 25],
            lans_iw_temp_pt2: ['Inner WP Temerature: 2', 20, 26, 22, 25],
            lans_iw_temp_pt3: ['Inner WP Temerature: 3', 20, 26, 22, 25],
            lans_iw_temp_pt4: ['Inner WP Temerature: 4', 20, 26, 22, 25],
            lans_ow_temp_pt1: ['Outer WP Temerature: 1', 20, 26, 22, 25],
            lans_ow_temp_pt2: ['Outer WP Temerature: 2', 20, 26, 22, 25],
            lans_ow_temp_pt3: ['Outer WP Temerature: 3', 20, 26, 22, 25],
            lans_ow_temp_pt4: ['Outer WP Temerature: 4', 20, 26, 22, 25]
        },
        LansRpcGas101 : {
            pressure_argon: ['RPC Argon Pressure [psi]', 18, 23, 19, 22],
            pressure_isobutane: ['RPC Isobutane Pressure [psi]', 18, 22, 19, 22],
            pressure_r134a: ['RPC R134A Pressure [psi]', 18, 22, 18.5, 22],
            pressure_sf6: ['RPC SF6 Pressure [psi]', 18, 22, 19, 22],
            flow_rate_argon: ['RPC Argon Flow Rate [cc/m]', 950, 1100, 1000, 1050],
            flow_rate_isobutane: ['RPC Isobutane Flow Rate [cc/m]', 60, 65, 61.5, 62],
            flow_rate_r134a: ['RPC R134A Flow Rate [cc/m]', 460, 475, 465, 468],
            flow_rate_sf6: ['RPC SF6 Flow Rate [cc/m]', 6, 7.7, 7.55, 7.65]     
        },
        LansRpcGas102 : {
            weight_isobutane: ['RPC Isobutane Weight [kg]', -10, 80, 2, 75],
            weight_r134a: ['RPC R134A Weight [kg]', -10, 80, 2, 75],
            weight_sf6: ['RPC SF6 Weight [kg]', -10, 80, 2, 75]     
        }
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

