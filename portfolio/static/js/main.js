$(function($) {

    // close notification success
    $("#closeNotif").click(function() {
        if(typeof $('#notifsuccess') != 'undefined') {$("#notifsuccess").slideUp();}
        if(typeof $('#notiferror') != 'undefined'){$("#notiferror").slideUp();}
    });

    // smooth scroll
    $("a[href*='#']:not([href='#'])").click(function() {
        var page = $(this).attr('href');
        var speed = 750;
        $('html, body').animate( { scrollTop: $(page).offset().top }, speed );
        return false;
  });

});

/*;(function ($) {
    'use strict';
    var $body    = $('html, body'), // Define jQuery collection 
        content  = $('header').smoothState({
          onStart : {
            duration: 250,
            render: function () {
              content.toggleAnimationClass('is-exiting');
              
              // Scroll user to the top
              $body.animate({ 'scrollTop': 0 });
  
            }
          }
        }).data('smoothState');
  })(jQuery);*/