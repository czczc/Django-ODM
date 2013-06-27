

modal_by_click('.img_db');
// $('.img_db').each(function(){
//     src = $(this).attr("src");
//     $(this).removeAttr("src").attr("src", src);
//     // console.log($(this));
// });

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
