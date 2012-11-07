var formulas = new Object();
load_formulas();

// for values, see http://dayabay.ihep.ac.cn/svn/dybaux/AD/ADSensors/LidSensors/DeliveryAndInstallation/master conversion table.ods
// David Webber Nov 10, 2011
// Temperature sensor offsets provided by R. Zhao on Feb 22, 2012

function load_formulas(){
    formulas = {
        Ad1Lidsensor : {
            ultrasonic_gdls:  function(x) { return (2720.6-x)/11.454+41; },
            ultrasonic_ls:    function(x) { return (2802.2-x)/11.384+23; },
            capacitance_mo:   function(x) { return 240-224.63+x*0.208044; },
            capacitance_gdls: function(x) { return 0.1507*x+0.5525+41; },
            capacitance_ls:   function(x) { return 0.15015*x+16.2473+23; },
            temp_gdls:        function(x) { return x+0.256; },
            temp_ls:          function(x) { return x+0.156; }
        },
        Ad2Lidsensor : {
            ultrasonic_gdls:  function(x) { return (2724.7-x)/11.416+41; },
            ultrasonic_ls:    function(x) { return (2786.9-x)/11.638+23; },
            capacitance_mo:   function(x) { return 240-224.24+x*0.208217; },
            capacitance_gdls: function(x) { return 0.15105*x-1.8593+41; },
            capacitance_ls:   function(x) { return 0.15175*x+14.1732+23; },
            temp_gdls:        function(x) { return x-0.026; },
            temp_ls:          function(x) { return x+0.13;  }
        },
        Ad3Lidsensor : { 
            ultrasonic_gdls:  function(x) { return (2703.6-x)/11.354+41; },
            ultrasonic_ls:    function(x) { return (2765.9-x)/11.382+23; },
            capacitance_mo:   function(x) { return 240-225.64+x*0.208335; },
            capacitance_gdls: function(x) { return 0.1517*x+0.6203+41; },
            capacitance_ls:   function(x) { return 0.14785*x-1.0478+23; },
            temp_gdls:        function(x) { return x+0.07; },
            temp_ls:          function(x) { return x+0.05; }
        },
        Ad4Lidsensor : {
            ultrasonic_gdls:  function(x) { return (2680-x)/11.369+41; },
            ultrasonic_ls:    function(x) { return (2737-x)/11.451+23; },
            capacitance_mo:   function(x) { return 240-225.4+x*0.208438; },
            capacitance_gdls: function(x) { return 0.14815*x-1.38+41; },
            capacitance_ls:   function(x) { return 0.14830*x+9.67+23; },
            temp_gdls:        function(x) { return x+0.24;  },
            temp_ls:          function(x) { return x+0.005; }
        },
        Ad5Lidsensor : {
            ultrasonic_gdls:  function(x) { return (2694.39-x)/11.334+41; },
            ultrasonic_ls:    function(x) { return (2764.12-x)/11.403+23; },
            capacitance_mo:   function(x) { return 240-226.2+x*0.205716; },
            capacitance_gdls: function(x) { return 0.1452*x+6.75+41; },
            capacitance_ls:   function(x) { return 0.14790*x+0.9+23; },
            temp_gdls:        function(x) { return 0.996*x+0.356; },
            temp_ls:          function(x) { return 0.992*x+0.451; }
        },
        Ad6Lidsensor : { // TODO: check GdLS, LS capacitance offsets
            ultrasonic_gdls:  function(x) { return (2708.48-x)/11.366+41; },
            ultrasonic_ls:    function(x) { return (2767.67-x)/11.378+23; },
            capacitance_mo:   function(x) { return 240-225.66+x*0.208487; },
            capacitance_gdls: function(x) { return 0.1471*x+0.6+41; },
            capacitance_ls:   function(x) { return 0.15125*x-1.21+23; },
            temp_gdls:        function(x) { return 0.997*x+0.283; },
            temp_ls:          function(x) { return 0.995*x-0.160+0.3; } // sensor reads lower than expected, so bumped it up by 0.3
        },
        Ad7Lidsensor : { // Checked on Sept 7, 2012
            ultrasonic_gdls:  function(x) { return (2725.4-x)/11.397+41; },
            ultrasonic_ls:    function(x) { return (2769.4-x)/11.357+23; },
            capacitance_mo:   function(x) { return 240-226.29+x*0.204427; },
            capacitance_gdls: function(x) { return 0.1485*x-1.0+41; },
            capacitance_ls:   function(x) { return 0.1488*x+1.2+23; },
            temp_gdls:        function(x) { return 0.992*x+0.391; }, 
            temp_ls:          function(x) { return 0.995*x+0.355; }  
        },
        Ad8Lidsensor : { // Checked on Sept 7, 2012
            ultrasonic_gdls:  function(x) { return (2710.2-x)/11.325+41; },
            ultrasonic_ls:    function(x) { return (2766.9-x)/11.368+23; },
            capacitance_mo:   function(x) { return 240-224.09+x*0.208103; },
            capacitance_gdls: function(x) { return 0.14805*x-2.6+41; },
            capacitance_ls:   function(x) { return 0.14795*x-2.6+23; },
            temp_gdls:        function(x) { return 0.992*x+0.262; }, 
            temp_ls:          function(x) { return 0.996*x+0.220; }  
        }
    };
}
