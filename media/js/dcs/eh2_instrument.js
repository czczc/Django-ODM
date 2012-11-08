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
    load_model('Ad8Lidsensor');
    load_model('Ad3Adcovergas');
    load_model('Ad8Adcovergas');
    load_model('LansIowTemp');
    load_model('LansRpcGas101');
    load_model('LansRpcGas102');
    load_model('LansEnvPth');
    load_model('LansWatersystem');

}

function fetch_latest() {
    fetch_one('Ad3Lidsensor');
    fetch_one('Ad8Lidsensor');
    fetch_one('Ad3Adcovergas');
    fetch_one('Ad8Adcovergas');
    fetch_one('LansIowTemp');
    fetch_one('LansRpcGas101');
    fetch_one('LansRpcGas102');
    fetch_one('LansEnvPth');
    fetch_one('LansWatersystem');
}

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        Ad3Lidsensor : {
            // liquid levels change by 14 mm/C.  I set +/- 0.4C, +/-5.6 mm
            ultrasonic_gdls:  ['AD3 GdLS Level: Ultrasonic [mm]',  92.3-15, 92.3+15, 92.3-5.6,     92.3+5.6],     // DMW
            capacitance_gdls: ['AD3 GdLS Level: Capacitance [mm]', 92.3-15, 92.3+15, 92.3-5.6-3.0, 92.3+5.6+3.0], // DMW 
            ultrasonic_ls:    ['AD3 LS Level: Ultrasonic [mm]',    80.4-15, 80.4+15, 80.4-5.6,     80.4+5.6],     // DMW
            capacitance_ls:   ['AD3 LS Level: Capacitance [mm]',   80.4-15, 80.4+15, 80.4-5.6-3.0, 80.4+5.6+3.0], // DMW
            capacitance_mo:   ['AD3 MO Level: Capacitance [mm]',   86.7-15, 86.7+15, 86.7-5.6,     86.7+5.6],     // DMW
            temp_gdls:        ['AD3 GdLS Temperature [C]', 21, 25, 22.7-0.4, 22.7+0.4],                           // DMW
            temp_ls:          ['AD3 LS Temperature [C]',   21, 25, 22.7-0.4, 22.7+0.4],                           // DMW
            //capacitance_temp_gdls: ['AD3 GdLS Temperature [C]: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD3 LS Temperature [C]: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD3 MO Temperature [C]: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD3 Tilt X1 [deg]', -2, 2,  0.38,  0.42],
            tiltx_sensor2: ['AD3 Tilt X2 [deg]', -2, 2, -0.22, -0.18],
            tiltx_sensor3: ['AD3 Tilt X3 [deg]', -2, 2, -0.37, -0.33],
            tilty_sensor1: ['AD3 Tilt Y1 [deg]', -2, 2,  0.78,  0.82],
            tilty_sensor2: ['AD3 Tilt Y2 [deg]', -2, 2,  1.40,  1.44],
            tilty_sensor3: ['AD3 Tilt Y3 [deg]', -2, 2, -0.19, -0.15]
        },
        Ad8Lidsensor : {
            // liquid levels change by 14 mm/C.  I set +/- 0.4C, +/-5.6 mm
            ultrasonic_gdls:  ['AD8 GdLS Level: Ultrasonic [mm]',  104.2-15, 104.2+15, 104.2-5.6,     104.2+5.6],     // DMW
            capacitance_gdls: ['AD8 GdLS Level: Capacitance [mm]', 104.2-15, 104.2+15, 104.2-5.6-3.0, 104.2+5.6+3.0], // DMW
            ultrasonic_ls:    ['AD8 LS Level: Ultrasonic [mm]',    106.1-15, 106.1+15, 106.1-5.6,     106.1+5.6],     // DMW
            capacitance_ls:   ['AD8 LS Level: Capacitance [mm]',   106.1-15, 106.1+15, 106.1-5.6-3.0, 106.1+5.6+3.0], // DMW
            capacitance_mo:   ['AD8 MO Level: Capacitance [mm]',   107.1-15, 107.1+15, 107.1-5.6,     107.1+5.6],     // DMW
            temp_gdls:        ['AD8 GdLS Temperature [C]', 21, 25, 22.7-0.4, 22.7+0.4],                               // DMW
            temp_ls:          ['AD8 LS Temperature [C]',   21, 25, 22.7-0.4, 22.7+0.4],                               // DMW
            //capacitance_temp_gdls: ['AD8 GdLS Temperature [C]: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD8 LS Temperature [C]: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD8 MO Temperature [C]: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD8 Tilt X1 [deg]', -2, 2,  0.38,  0.42],
            tiltx_sensor2: ['AD8 Tilt X2 [deg]', -2, 2, -0.22, -0.18],
            tiltx_sensor3: ['AD8 Tilt X3 [deg]', -2, 2, -0.37, -0.33],
            tilty_sensor1: ['AD8 Tilt Y1 [deg]', -2, 2,  0.78,  0.82],
            tilty_sensor2: ['AD8 Tilt Y2 [deg]', -2, 2,  1.40,  1.44],
            tilty_sensor3: ['AD8 Tilt Y3 [deg]', -2, 2, -0.19, -0.15]
        },
        Ad3Adcovergas : {
            supplypressure: ['AD3 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD3 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD3 Cover Gas Return [%]', 0.1, 100, -0.9, 5],
            humidity_electricaldrypipereturn: ['Humidity: AD3 Elec. Dry Pipe Return [%]', 0.1, 100, -0.9, 110],
            humidity_gasdrypipereturn: ['Humidity: AD3 Gas Dry Pipe Return [%]', 0.1, 100, -0.9, 10],
            humidity_pmtcablebellowreturn: ['Humidity: AD3 PMT Cable Bellow Return [%]', 0.1, 100, -0.9, 10]
        },
        Ad8Adcovergas : {
            supplypressure: ['AD8 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD8 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD8 Cover Gas Return [%]', 0.1, 100, -0.9, 5],
            humidity_electricaldrypipereturn: ['Humidity: AD8 Elec. Dry Pipe Return [%]', 0.1, 100, -0.9, 110],
            humidity_gasdrypipereturn: ['Humidity: AD8 Gas Dry Pipe Return [%]', 0.1, 100, -0.9, 10],
            humidity_pmtcablebellowreturn: ['Humidity: AD8 PMT Cable Bellow Return [%]', 0.1, 100, -0.9, 10]
        },
        LansIowTemp : {
            lans_iw_temp_pt1: ['Inner WP Temerature: 1 [C]', 20, 26, 22, 25],
            lans_iw_temp_pt2: ['Inner WP Temerature: 2 [C]', 20, 26, 22, 25],
            lans_iw_temp_pt3: ['Inner WP Temerature: 3 [C]', 20, 26, 22, 25],
            lans_iw_temp_pt4: ['Inner WP Temerature: 4 [C]', 20, 26, 22, 25],
            lans_ow_temp_pt1: ['Outer WP Temerature: 1 [C]', 20, 26, 22, 25],
            lans_ow_temp_pt2: ['Outer WP Temerature: 2 [C]', 20, 26, 22, 25],
            lans_ow_temp_pt3: ['Outer WP Temerature: 3 [C]', 20, 26, 22, 25],
            lans_ow_temp_pt4: ['Outer WP Temerature: 4 [C]', 20, 26, 22, 25]
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
        },
        LansEnvPth : {
            lans_pth_t1: ['Temperature: E-Room [C]', 20, 29, 21, 29],        
            lans_pth_t2: ['Temperature: Near Gas-Room [C]', 20, 29, 21, 29],        
            lans_pth_h1: ['Humidity: E-Room [%]', 30, 80, 30, 70],        
            lans_pth_h2: ['Humidity: Near Gas-Room [%]', 30, 80, 30, 70],        
            lans_pth_p1: ['Pressure: E-Room [mbar]', 1000, 1050, 980, 1030],        
            lans_pth_p2: ['Pressure: Near Gas-Room [mbar]', 1000, 1050, 980, 1030]
        },
        LansWatersystem : {
            waterlevel: ['Water Level: [m]', 7, 12, 8, 11],        
            poolwaterresistivity: ['Resistivity: Pool Water [M.Ohm]', 0, 18, 0.1, 16],        
            productresistivity: ['Resistivity: Product Water [M.Ohm]', 0, 20, 0.1, 18],        
            iwateroxygencontent: ['Oxygen: In Flow [ppm]', 0, 400, 10, 350],        
            owateroxygencontent: ['Oxygen: Out Flow [ppm]', 0, 400, 10, 350],        
            heatertemperature: ['Temperature: Heater [C]', 15, 35, 20, 30],
            heatexchangetemperature: ['Temperature: Heater Exchange [C]', 15, 35, 20, 30]
        }
    };
}


