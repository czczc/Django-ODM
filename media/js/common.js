$("#show_nav").click(function() {
		$("#nav").toggle("blind", "", "fast");
	}
);

$("#quick_search_field").css("color", "#aaa").val(' Run No.');
$("#quick_search_field").click(function() {
    $(this).val('').css("color", "#333");
});

$("#zone-bar li a").click(function() {
    var submenu = $(this).parents("li").children("ul");
    var hidden = submenu.is(":hidden");

    $("#zone-bar>ul>li>ul").hide();       
    $("#zone-bar>ul>li>a").removeClass();

    if (hidden) {
        submenu.toggle()
        .parents("li").children("a").addClass("zoneCur");
    } 
});
// 
$("#content").click(function() {
    $("#zone-bar>ul>li>ul").hide();       
    $("#zone-bar>ul>li>a").removeClass();
});
// 
// $(".top_menu").click(function() {
//    return false; 
// });
