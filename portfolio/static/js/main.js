$(function() {
    // delete loading
    "use strict";
    $("#deleteLoading").smoothState({ debug: true });

    // smooth
    $("a[href*='#']:not([href='#'])").click(function() {
        if(location.hostname == this.hostname && this.pathname.replace(/^\//,"") == location.pathname.replace(/^\//,"")){
            var anchor = $(this.hash);
            anchor = anchor.length ? anchor : $("[name=" + this.hash.slice(1) +"]");
            if(anchor.length){
                $("html, body").animate( { scrollTop: anchor.offset().top }, 1500);
            }
        }
    });

    // close notification success
    $("#closeNotif").click(function() {
        $("#notifSuccess").slideUp();
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