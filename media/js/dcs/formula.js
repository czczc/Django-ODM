var formulas = new Object();
load_formulas();

// for values, see http://dayabay.ihep.ac.cn/svn/dybaux/AD/ADSensors/LidSensors/DeliveryAndInstallation/master conversion table.ods
// David Webber Nov 10, 2011

function load_formulas(){
    formulas = {
        Ad1Lidsensor : {
            ultrasonic_gdls:  function(x) { return (2720.6-x)/11.454+41; },
            ultrasonic_ls:    function(x) { return (2802.2-x)/11.384+23; },
            capacitance_mo:   function(x) { return 240-224.63+x*0.208044; },
            capacitance_gdls: function(x) { return 0.1507*x+0.5525+41; },
            capacitance_ls:   function(x) { return 0.15015*x+14.2473+23; }
        },
        Ad2Lidsensor : {
            ultrasonic_gdls:  function(x) { return (2724.7-x)/11.416+41; },
            ultrasonic_ls:    function(x) { return (2786.9-x)/11.638+23; },
            capacitance_mo:   function(x) { return 240-224.24+x*0.208217; },
            capacitance_gdls: function(x) { return 0.15105*x-1.8593+41; },
            capacitance_ls:   function(x) { return 0.15175*x+15.0732+23; }
        },
        Ad3Lidsensor : { // TODO: check GdLS, LS capacitance offsets
            ultrasonic_gdls:  function(x) { return (2703.6-x)/11.354+41; },
            ultrasonic_ls:    function(x) { return (2765.9-x)/11.382+23; },
            capacitance_mo:   function(x) { return 240-225.64+x*0.208335; },
            capacitance_gdls: function(x) { return 0.1517*x-4.5397+41; },
            capacitance_ls:   function(x) { return 0.14785*x-4.2578+23; }
        },
        Ad4Lidsensor : { // TODO: check GdLS, LS capacitance offsets
            ultrasonic_gdls:  function(x) { return (2680-x)/11.369+41; },
            ultrasonic_ls:    function(x) { return (2737-x)/11.451+23; },
            capacitance_mo:   function(x) { return 240-225.4+x*0.208438; },
            capacitance_gdls: function(x) { return 0.14815*x-7.6+41; },
            capacitance_ls:   function(x) { return 0.14830*x-3.77+23; }
        },
        Ad5Lidsensor : { // TODO: check GdLS, LS capacitance offsets
            ultrasonic_gdls:  function(x) { return (2694.39-x)/11.334+41; },
            ultrasonic_ls:    function(x) { return (2764.12-x)/11.403+23; },
            capacitance_mo:   function(x) { return 240-226.2+x*0.205716; },
            capacitance_gdls: function(x) { return 0.1452*x+5.0587+41; },
            capacitance_ls:   function(x) { return 0.14790*x-0.3816+23; }
        },
        Ad6Lidsensor : { // TODO: check GdLS, LS capacitance offsets
            ultrasonic_gdls:  function(x) { return (2708.48-x)/11.366+41; },
            ultrasonic_ls:    function(x) { return (2767.67-x)/11.378+23; },
            capacitance_mo:   function(x) { return 240-225.66+x*0.208487; },
            capacitance_gdls: function(x) { return 0.1471*x+0.0000+41; },
            capacitance_ls:   function(x) { return 0.15125*x+0.00+23; }
        },
        Ad7Lidsensor : { // placeholders only
            ultrasonic_gdls:  function(x) { return -(2720.6-x)/11.454+41; },
            ultrasonic_ls:    function(x) { return -(2802.2-x)/11.384+23; },
            capacitance_mo:   function(x) { return -240-224.63+x*0.208044; },
            capacitance_gdls: function(x) { return -0.1507*x+0.5525+41; },
            capacitance_ls:   function(x) { return -0.14790*x-0.3816+23; }
        },
        Ad8Lidsensor : { // placeholders only
            ultrasonic_gdls:  function(x) { return -(2720.6-x)/11.454+41; },
            ultrasonic_ls:    function(x) { return -(2802.2-x)/11.384+23; },
            capacitance_mo:   function(x) { return -240-224.63+x*0.208044; },
            capacitance_gdls: function(x) { return -0.1507*x+0.5525+41; },
            capacitance_ls:   function(x) { return -0.15015*x+14.2473+23; }
        }
    };
}
