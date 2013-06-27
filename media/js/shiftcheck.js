modal_by_click('.img_db');


var Ref = new Object;
set_ref(parseInt($('#ref_runno').html(), 10));
function set_ref(runno) {
    Ref.runno = runno;
    // console.log(runno);
    Ref.diagnostics_seg = sprintf('runs_%07d/runs_%07d/run_%07d', 
        Math.floor(Ref.runno/1000)*1000, Math.floor(Ref.runno/100)*100, Ref.runno);
    Ref.diagnostics_base_index = 60; // nersc
    Ref.diagnostics_shown = true; // is currently displaying Ref?
}
// console.log(Ref);

var this_url = window.location.href;
var index_of_run = this_url.indexOf('run');
var base_url = this_url.substring(0,index_of_run);
var remainder_url = this_url.substring(index_of_run+4);
var Run = new Object;
Run.runno = remainder_url.substring(0, remainder_url.indexOf('/'));
Run.diagnostics_seg = sprintf('runs_%07d/runs_%07d/run_%07d', 
    Math.floor(Run.runno/1000)*1000, Math.floor(Run.runno/100)*100, Run.runno);

// console.log(Run);

enable_toggle_img_ref();

$('.img_db').each(function(){
    var this_link = $(this).attr('src');
    var ref_link = this_link.replace(Run.diagnostics_seg, Ref.diagnostics_seg);
    $(this).parent().append('<img class="img_ref" src="' + ref_link + '" width=200 height=150/>'); 
    modal_by_click($(this).siblings('.img_ref'));
    // $(".ref_runno").html('Reference Run: ' + Ref.runno);
});

function enable_toggle_img_ref() {
    $(document).unbind('keypress');
    $(document).bind('keypress', toggle_img_ref);
}

function toggle_img_ref(e) {
    if (Ref['diagnostics_shown']) {
      $('.img_ref').remove();
      Ref['diagnostics_shown'] = false;  
    }
    else {
        $('.img_db').each(function(){
            var this_link = $(this).attr('src');
            var ref_link = this_link.replace(Run.diagnostics_seg, Ref.diagnostics_seg);
            $(this).parent().append('<img class="img_ref" src="' + ref_link + '" width=200 height=150/>'); 
            modal_by_click($(this).siblings('.img_ref'));
            Ref['diagnostics_shown'] = true;
        });
    }
}



// display image modal window by single click
function modal_by_click(selector) {
    // change cursor shape
    $(selector).hover(function() {
        $(this).css('cursor','pointer');
    }, function() {
        $(this).css('cursor','auto');
    });
    // single click
    $(selector).click(function() {
        $.modal('<div><img src="' 
            + $(this).attr("src")
            + '" /></div>',
            {
                'overlayClose' : true
            }
        );
        return false;
    });
}