var formulas = new Object();
load_formulas();

function load_formulas(){
    formulas = {
        Ad1Lidsensor : {
            ultrasonic_gdls: function(x) { return (2720.6-x)/11.454+41; },
            ultrasonic_ls:   function(x) { return (2802.2-x)/11.384+23; },
            capacitance_mo:  function(x) { return 240-224.63+x*0.208044; }
        },
        Ad2Lidsensor : {
            ultrasonic_gdls: function(x) { return (2724.7-x)/11.416+41; },
            ultrasonic_ls:   function(x) { return (2786.9-x)/11.638+23; },
            capacitance_mo:  function(x) { return 240-224.24+x*0.208217; }
        },
        Ad3Lidsensor : {
            ultrasonic_gdls: function(x) { return (2703.6-x)/11.354+41; },
            ultrasonic_ls:   function(x) { return (2765.9-x)/11.382+23; },
            capacitance_mo:  function(x) { return 240-225.64+x*0.208335; }
        },
        Ad4Lidsensor : {
            ultrasonic_gdls: function(x) { return (2680-x)/11.369+41; },
            ultrasonic_ls:   function(x) { return (2737-x)/11.451+23; },
            capacitance_mo:  function(x) { return 240-225.4+x*0.208438; }
        }
    };
}
