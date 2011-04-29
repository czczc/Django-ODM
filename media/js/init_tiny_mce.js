tinyMCE.init({
        mode : "textareas",
        theme : "advanced",
        skin : "o2k7",
        plugins : "emotions,spellchecker,advhr,insertdatetime,table", 
        height : "480",
        
        // Theme options - button# indicated the row# only
        theme_advanced_buttons1 : "newdocument,cut,copy,paste,|,undo,redo,|,bullist,numlist,|,outdent,indent,|,justifyleft,justifycenter,justifyright,|,tablecontrols",
        theme_advanced_buttons2 : "code,|,fontselect,fontsizeselect,formatselect,forecolor,|,bold,italic,underline,strikethrough,|,link,unlink,|,insertdate,inserttime,advhr,removeformat,spellchecker,|,sub,sup,|,charmap,emotions",      
        theme_advanced_buttons3 : "",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_statusbar_location : "bottom"
        // theme_advanced_resizing : true
});
