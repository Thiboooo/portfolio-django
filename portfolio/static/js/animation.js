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
$(function() {
  'use strict';
  $('#deleteLoading').smoothState({ debug: true });
});