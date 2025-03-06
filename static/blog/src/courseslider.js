$(document).ready(function() {
  $('#sliderCourses').lightSlider({
      item:4,
      loop:false,
      slideMove:2,
      easing: 'cubic-bezier(0.25, 0, 0.25, 1)',
      speed:600,
      slideMargin:20,
      responsive : [
          {
              breakpoint:800,
              settings: {
                  item:3,
                  slideMove:1,
                  slideMargin:1,
                }
          },
          {
              breakpoint:600,
              settings: {
                  item:2,
                  slideMove:2,
                  slideMargin:5,
                }
          },
          {
              breakpoint:480,
              settings: {
                  item:1,
                  slideMove:1,
                  slideMargin:5,
                }
          },

          {
              breakpoint:420,
              settings: {
                  item:1,
                  slideMove:1
                }
          }
      ]
  });  
});