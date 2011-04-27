$('#pdsf_logout').click(function(){
    $.newt_ajax({
        url: '/logout',       
        type: 'GET',
        success: function(data) {
            show_success("You've logged out PDSF.");
        }
    });
});

function run_command(cmd) {
    $.newt_ajax({
        url: '/command/pdsf',    
        type: 'POST',
        data: {"executable": cmd}, 
        success: function(data) {
            $.noticeRemove($('.notice-item-wrapper'), 400);
            $.modal('<div><pre class="prettyprint">' + data.output + '</pre></div>',
                {
                    'overlayClose' : true,
                    'maxWidth' : 900,
                    'maxHeight' : 600
                }
            );
            prettyPrint();
        },
        error: function() {
            show_error('ERROR: operation failed.');
        }
    });
}

function show_modal_pre(output) {
    $.modal('<div><pre class="prettyprint">' + output + '</pre></div>',
        {
            'overlayClose' : true,
            'maxWidth' : 900,
            'maxHeight' : 600
        }
    );
    prettyPrint();
}

function show_notice(text) {
    $.noticeAdd({ text : text, stay: true});
}

function show_error(text) {
    $.noticeAdd({ text : text, type: 'error', stay: true});
}

function show_success(text) {
    $.noticeAdd({ text : text, type: 'success'});
}

function remove_notice() {
    $.noticeRemove($('.notice-item-wrapper'), 400);
}