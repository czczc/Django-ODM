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

    load_model('Ad1Lidsensor');
    load_model('Ad2Lidsensor');
    load_model('Ad1Adcovergas');
    load_model('Ad2Adcovergas');
    load_model('DbnsIowTemp');
    load_model('DbnsRpcGas101');
    load_model('DbnsRpcGas102');
    load_model('DbnsEnvPth');
    load_model('DbnsWatersystem');
}

function fetch_latest() {
    fetch_one('Ad1Lidsensor');
    fetch_one('Ad2Lidsensor');
    fetch_one('Ad1Adcovergas');
    fetch_one('Ad2Adcovergas');
    fetch_one('DbnsIowTemp');
    fetch_one('DbnsRpcGas101');
    fetch_one('DbnsRpcGas102');
    fetch_one('DbnsEnvPth');
    fetch_one('DbnsWatersystem');
    
}

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        Ad1Lidsensor : {
            // liquid levels change by 14 mm/C.  I set +/- 0.3C, +/-4.5 mm
            ultrasonic_gdls:  ['AD1 GdLS Level: Ultrasonic [mm]',  65, 95, 80.6-4.5, 80.6+4.5],
            capacitance_gdls: ['AD1 GdLS Level: Capacitance [mm]', 65, 95, 80.6-4.5, 80.6+4.5],    
            ultrasonic_ls:    ['AD1 LS Level: Ultrasonic [mm]',    65, 95, 85.6-4.5, 85.6+4.5], 
            capacitance_ls:   ['AD1 LS Level: Capacitance [mm]',   65, 95, 85.6-4.5, 85.6+4.5],
            capacitance_mo:   ['AD1 MO Level: Capacitance [mm]',   65, 95, 82.6-4.5, 82.6+4.5],
            temp_gdls:        ['AD1 GdLS Temperature [C]', 21, 25, 22.4, 23],
            temp_ls:          ['AD1 LS Temperature [C]',   21, 25, 22.4, 23],
            //capacitance_temp_gdls: ['AD1 GdLS Temperature: Capacitance [C]', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD1 LS Temperature: Capacitance [C]', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD1 MO Temperature: Capacitance [C]', 20, 26, 21, 25],
            tiltx_sensor1: ['AD1 Tilt X1 [deg]', -2, 2, -0.98, -0.94],
            tiltx_sensor2: ['AD1 Tilt X2 [deg]', -2, 2, -0.25, -0.21],
            tiltx_sensor3: ['AD1 Tilt X3 [deg]', -2, 2, -0.75, -0.71],
            tilty_sensor1: ['AD1 Tilt Y1 [deg]', -2, 2,  0.24,  0.28],
            tilty_sensor2: ['AD1 Tilt Y2 [deg]', -2, 2, -0.44, -0.40],
            tilty_sensor3: ['AD1 Tilt Y3 [deg]', -2, 2,  1.22,  1.26]
        },
        Ad2Lidsensor : {
            ultrasonic_gdls:  ['AD2 GdLS Level: Ultrasonic [mm]',  65, 95, 85.0-4.5, 85.0+4.5],
            capacitance_gdls: ['AD2 GdLS Level: Capacitance [mm]', 65, 95, 85.0-4.5, 85.0+4.5],    
            ultrasonic_ls:    ['AD2 LS Level: Ultrasonic [mm]',    65, 95, 87.7-4.5, 87.7+4.5], 
            capacitance_ls:   ['AD2 LS Level: Capacitance [mm]',   65, 95, 87.7-4.5, 87.7+4.5],
            capacitance_mo:   ['AD2 MO Level: Capacitance [mm]',   65, 95, 84.3-4.5, 84.3+4.5],
            temp_gdls:        ['AD2 GdLS Temperature [C]', 21, 25, 22.4, 23],
            temp_ls:          ['AD2 LS Temperature [C]',   21, 25, 22.4, 23],
            //capacitance_temp_gdls: ['AD2 GdLS Temperature: Capacitance [C]', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD2 LS Temperature: Capacitance [C]', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD2 MO Temperature: Capacitance [C]', 20, 26, 21, 25],
            tiltx_sensor1: ['AD2 Tilt X1 [deg]', -2, 2,  0.78,  0.82],
            tiltx_sensor2: ['AD2 Tilt X2 [deg]', -2, 2,  0.18,  0.22],
            tiltx_sensor3: ['AD2 Tilt X3 [deg]', -2, 2,  0.14,  0.18],
            tilty_sensor1: ['AD2 Tilt Y1 [deg]', -2, 2, -0.23, -0.19],
            tilty_sensor2: ['AD2 Tilt Y2 [deg]', -2, 2, -0.80, -0.76],
            tilty_sensor3: ['AD2 Tilt Y3 [deg]', -2, 2, -0.73, -0.69]
        },
        Ad1Adcovergas : {
            supplypressure: ['AD1 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD1 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD1 Cover Gas Return [%]', 0.1, 100, -0.9, 5],
            humidity_electricaldrypipereturn: ['Humidity: AD1 Elec. Dry Pipe Return [%]', 0.1, 100, -0.9, 31],
            humidity_gasdrypipereturn: ['Humidity: AD1 Gas Dry Pipe Return [%]', 0.1, 100, -0.9, 10],
            humidity_pmtcablebellowreturn: ['Humidity: AD1 PMT Cable Bellow Return [%]', 0.1, 100, -0.9, 10]
        },
        Ad2Adcovergas : {
            supplypressure: ['AD2 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD2 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD2 Cover Gas Return [%]', 0.1, 100, -0.9, 5],
            humidity_electricaldrypipereturn: ['Humidity: AD2 Elec. Dry Pipe Return [%]', 0.1, 100, -0.9, 31],
            humidity_gasdrypipereturn: ['Humidity: AD2 Gas Dry Pipe Return [%]', 0.1, 100, -0.9, 10],
            humidity_pmtcablebellowreturn: ['Humidity: AD2 PMT Cable Bellow Return [%]', 0.1, 100, -0.9, 10]
        },
        DbnsIowTemp : {
            dbns_iw_temp_pt1: ['Inner WP Temerature [C]: 1', 21, 26, 22, 25],
            dbns_iw_temp_pt2: ['Inner WP Temerature [C]: 2', 21, 26, 22, 25],
            dbns_iw_temp_pt3: ['Inner WP Temerature [C]: 3', 21, 26, 22, 25],
            dbns_iw_temp_pt4: ['Inner WP Temerature [C]: 4', 21, 26, 22, 25],
            dbns_ow_temp_pt1: ['Outer WP Temerature [C]: 1', 21, 26, 22, 25],
            dbns_ow_temp_pt2: ['Outer WP Temerature [C]: 2', 21, 26, 22, 25],
            dbns_ow_temp_pt3: ['Outer WP Temerature [C]: 3', 21, 26, 22, 25],
            dbns_ow_temp_pt4: ['Outer WP Temerature [C]: 4', 21, 26, 22, 25]
        },
        DbnsRpcGas101 : {
            pressure_argon: ['RPC Argon Pressure [psi]', 18, 23, 19, 22],
            pressure_isobutane: ['RPC Isobutane Pressure [psi]', 18, 22, 19, 22],
            pressure_r134a: ['RPC R134A Pressure [psi]', 18, 22, 18.5, 22],
            pressure_sf6: ['RPC SF6 Pressure [psi]', 18, 22, 19, 22],
            flow_rate_argon: ['RPC Argon Flow Rate [cc/m]', 950, 1100, 1000, 1050],
            flow_rate_isobutane: ['RPC Isobutane Flow Rate [cc/m]', 60, 63, 61.5, 62],
            flow_rate_r134a: ['RPC R134A Flow Rate [cc/m]', 460, 475, 465, 468],
            flow_rate_sf6: ['RPC SF6 Flow Rate [cc/m]', 7.4, 7.7, 7.55, 7.65]     
        },
        DbnsRpcGas102 : {
            weight_isobutane: ['RPC Isobutane Weight [kg]', -10, 80, 2, 75],
            weight_r134a: ['RPC R134A Weight [kg]', -10, 80, 2, 75],
            weight_sf6: ['RPC SF6 Weight [kg]', -10, 80, 2, 75]     
        },
        DbnsEnvPth : {
            dbns_pth_t1: ['Temperature: E-Room [C]', 20, 29, 21, 29],        
            dbns_pth_t2: ['Temperature: Near Gas-Room [C]', 20, 29, 21, 29],        
            dbns_pth_h1: ['Humidity: E-Room [%]', 30, 80, 30, 70],        
            dbns_pth_h2: ['Humidity: Near Gas-Room [%]', 30, 80, 30, 70],        
            dbns_pth_p1: ['Pressure: E-Room [mbar]', 1000, 1050, 980, 1030],        
            dbns_pth_p2: ['Pressure: Near Gas-Room [mbar]', 1000, 1050, 980, 1030]
        },
        DbnsWatersystem : {
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

