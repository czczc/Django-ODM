

modal_by_click('.img_db');

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
