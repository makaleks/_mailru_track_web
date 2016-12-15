
function set_menu_large() {
    $(document).foundation();
    var elem = new Foundation.Sticky($('#id-menu'), {
        //dataAnchor: content_id
        marginTop: 0
    });
    //$('.sticky').foundation('_calc', true);
    //$('.sticky').foundation('_setSticky');

    //$('.sticky').foundation('_events', true);
    //Foundation.reInit('sticky');
    //Foundation.reInit('sticky');
    //$(document).foundation();
    //$(document).foundation('reflow');
}

function set_menu_canvas() {
    $('.sticky').foundation('_removeSticky');

    var elem = new Foundation.OffCanvas($('#id-offcanvas'), {
        //dataAnchor: content_id
        marginTop: 0
    });
    //$('.sticky').foundation('_calc', true);
    //$('.sticky').foundation('_setSticky');
    
    //$('.sticky').foundation('_events', true);
    //Foundation.reInit('sticky');
    //Foundation.reInit('sticky');
    //$(document).foundation();
    //$(document).foundation('reflow');
}

function size_breakpoint_callback_menu(event, newSize, oldSize) {
    console.log("MYEVENT", event, newSize, oldSize);
    if(newSize != "small") {
        set_menu_large();
    }
    else {
        //set_menu_canvas();
    }
}

$(function() {
    $(document).foundation();

    size_breakpoint_callback_menu(
            null, Foundation.MediaQuery.current, null);
    //set_menu_large();
})

$(window).on('changed.zf.mediaquery', size_breakpoint_callback_menu);
