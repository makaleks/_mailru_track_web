function set_menu_small() {
    // Move menu
    $('#id-menu-container').appendTo('#id-off-canvas');
    // Remove margin
    $('#id-menu-container').removeClass('medium-2 column');
    // In other case content width is 10/12, floating right
    $('#id-content').removeClass('medium-10 column'); 
}

function set_menu_large() {
    $('#id-menu-container').insertBefore('#id-content');
    $('#id-menu-container').addClass('medium-2 column');
    $('#id-content').addClass('medium-10 column');
    $('#id-off-canvas').foundation('close');
}

function size_breakpoint_callback_menu(event, newSize, oldSize) {
    // console.log("MYEVENT", event, newSize, oldSize);
    if(newSize != "small") {
        set_menu_large();
    }
    else {
        set_menu_small();
    }
}

$(function() { // Called after all DOM is loaded to jQuery
    $(document).foundation();
    size_breakpoint_callback_menu(
          null, Foundation.MediaQuery.current, null);
})

// Set callback on screen size change
$(window).on('changed.zf.mediaquery', size_breakpoint_callback_menu);
