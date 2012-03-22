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
    load_model('Ad4Adcovergas');
    load_model('Ad5Adcovergas');
    load_model('Ad6Adcovergas');
    
    // load_model('LansIowTemp');
    // load_model('LansRpcGas101');
    load_model('FarsEnvPth');
    load_model('FarsWatersystem');

}

function fetch_latest() {
    fetch_one('Ad4Lidsensor');
    fetch_one('Ad5Lidsensor');
    fetch_one('Ad6Lidsensor');
    fetch_one('Ad4Adcovergas');
    fetch_one('Ad5Adcovergas');
    fetch_one('Ad6Adcovergas');
    
    // fetch_one('LansIowTemp');
    // fetch_one('LansRpcGas101');
    fetch_one('FarsEnvPth');
    fetch_one('FarsWatersystem');
    
}

function load_configs(){
    configs = {
        // renderTo, title, ymin, ymax, ysafemin, ysafemax
        Ad4Lidsensor : {
            ultrasonic_gdls:  ['AD4 GdLS Level: Ultrasonic [mm]',  101.25-15, 101.25+15, 101.25-4.5, 101.25+4.5],
            ultrasonic_ls:    ['AD4 LS Level: Ultrasonic [mm]',     95   -15,  95   +15,  95   -4.5,  95   +4.5],
            capacitance_gdls: ['AD4 GdLS Level: Capacitance [mm]', 101.25-15, 101.25+15, 101.25-4.5, 101.25+4.5],
            capacitance_ls:   ['AD4 LS Level: Capacitance [mm]',    95   -15,  95   +15,  95   -4.5,  95   +4.5],
            capacitance_mo:   ['AD4 MO Level: Capacitance [mm]',    93.8 -15,  93.8 +15,  93.8 -4.5,  93.8 +4.5],
            temp_gdls:        ['AD4 GdLS Temperature [C]', 21, 25, 22.4, 23],
            temp_ls:          ['AD4 LS Temperature [C]',   21, 25, 22.4, 23],
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
            ultrasonic_gdls:  ['AD5 GdLS Level: Ultrasonic [mm]',  87.71-15,  87.71+15,  87.71-4.5,  87.71+4.5],
            ultrasonic_ls:    ['AD5 LS Level: Ultrasonic [mm]',    87.6 -15,  87.6 +15,  87.6 -4.5,  87.6 +4.5],
            capacitance_gdls: ['AD5 GdLS Level: Capacitance [mm]', 87.71-15,  87.71+15,  87.71-4.5,  87.71+4.5],
            capacitance_ls:   ['AD5 LS Level: Capacitance [mm]',   87.6 -15,  87.6 +15,  87.6 -4.5,  87.6 +4.5],
            capacitance_mo:   ['AD5 MO Level: Capacitance [mm]',   93.4 -15,  93.4 +15,  93.4 -4.5,  93.4 +4.5],
            temp_gdls:        ['AD5 GdLS Temperature [C]', 21, 25, 22.4, 23],
            temp_ls:          ['AD5 LS Temperature [C]',   21, 25, 22.4, 23],
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
            ultrasonic_gdls:  ['AD6 GdLS Level: Ultrasonic [mm]',  99.5 -15,  99.5 +15,  99.5 -4.5,  99.5 +4.5],
            ultrasonic_ls:    ['AD6 LS Level: Ultrasonic [mm]',    97.2 -15,  97.2 +15,  97.2 -4.5,  97.2 +4.5],
            capacitance_gdls: ['AD6 GdLS Level: Capacitance [mm]', 99.5 -15,  99.5 +15,  99.5 -4.5,  99.5 +4.5],
            capacitance_ls:   ['AD6 LS Level: Capacitance [mm]',   97.2 -15,  97.2 +15,  97.2 -4.5,  97.2 +4.5],
            capacitance_mo:   ['AD6 MO Level: Capacitance [mm]',   95.2 -15,  95.2 +15,  95.2 -4.5,  95.2 +4.5],
            temp_gdls:        ['AD6 GdLS Temperature [C]', 21, 25, 22.4, 23],
            temp_ls:          ['AD6 LS Temperature [C]',   21, 25, 22.4, 23],
            //capacitance_temp_gdls: ['AD6 GdLS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_ls: ['AD6 LS Temperature: Capacitance', 23, 28, 24, 27],
            //capacitance_temp_mo: ['AD6 MO Temperature: Capacitance', 20, 26, 21, 25],
            tiltx_sensor1: ['AD6 Tilt X1 [deg]', -2, 2, -0.16, -0.12],
            tiltx_sensor2: ['AD6 Tilt X2 [deg]', -2, 2, -0.71, -0.67],
            tiltx_sensor3: ['AD6 Tilt X3 [deg]', -2, 2, -0.69, -0.65],
            tilty_sensor1: ['AD6 Tilt Y1 [deg]', -2, 2,  0.02,  0.06],
            tilty_sensor2: ['AD6 Tilt Y2 [deg]', -2, 2,  0.35,  0.39],
            tilty_sensor3: ['AD6 Tilt Y3 [deg]', -2, 2, -0.14, -0.10]
        },
        Ad4Adcovergas : {
            supplypressure: ['AD4 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD4 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD4 Cover Gas Return [%]', 0.1, 100, 0.1, 25],
            humidity_electricaldrypipereturn: ['Humidity: AD4 Elec. Dry Pipe Return [%]', 0.1, 100, 0.1, 31],
            humidity_gasdrypipereturn: ['Humidity: AD4 Gas Dry Pipe Return [%]', 0.1, 100, 0.1, 25],
            humidity_pmtcablebellowreturn: ['Humidity: AD4 PMT Cable Bellow Return [%]', 0.1, 100, 0.1, 25]
        },
        Ad5Adcovergas : {
            supplypressure: ['AD5 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD5 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD5 Cover Gas Return [%]', 0.1, 100, 0.1, 25],
            humidity_electricaldrypipereturn: ['Humidity: AD5 Elec. Dry Pipe Return [%]', 0.1, 100, 0.1, 31],
            humidity_gasdrypipereturn: ['Humidity: AD5 Gas Dry Pipe Return [%]', 0.1, 100, 0.1, 25],
            humidity_pmtcablebellowreturn: ['Humidity: AD5 PMT Cable Bellow Return [%]', 0.1, 100, 0.1, 25]
        },
        Ad6Adcovergas : {
            supplypressure: ['AD6 Cover Gas Pressure [psi]', 10, 30, 16, 25],
            oxygen: ['AD6 Cover Gas Oxygen Concentration [ppm]', 0.1, 550, 0.1, 500],
            humidity_covergasreturn: ['Humidity: AD6 Cover Gas Return [%]', 0.1, 100, 0.1, 25],
            humidity_electricaldrypipereturn: ['Humidity: AD6 Elec. Dry Pipe Return [%]', 0.1, 100, 0.1, 31],
            humidity_gasdrypipereturn: ['Humidity: AD6 Gas Dry Pipe Return [%]', 0.1, 100, 0.1, 25],
            humidity_pmtcablebellowreturn: ['Humidity: AD6 PMT Cable Bellow Return [%]', 0.1, 100, 0.1, 25]
        },
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
        FarsEnvPth : {
            fars_pth_t1: ['Temperature: E-Room [C]', 20, 29, 21, 29],        
            fars_pth_t2: ['Temperature: Near Gas-Room [C]', 20, 29, 21, 29],        
            fars_pth_h1: ['Humidity: E-Room [%]', 30, 80, 30, 70],        
            fars_pth_h2: ['Humidity: Near Gas-Room [%]', 30, 80, 30, 70],        
            fars_pth_p1: ['Pressure: E-Room [mbar]', 1000, 1050, 980, 1030],        
            fars_pth_p2: ['Pressure: Near Gas-Room [mbar]', 1000, 1050, 980, 1030]
        },
        FarsWatersystem : {
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
