$(document).ready(function() {
  $('#sliderBooks').lightSlider({
      item:3,
      loop:false,
      slideMove:3,
      easing: 'cubic-bezier(0.25, 0, 0.25, 1)',
      speed:600,
      slideMargin:20,
      responsive : [
          {
              breakpoint:800,
              settings: {
                  item:2,
                  slideMove:1,
                  slideMargin:1,
                }
          },
          {
              breakpoint:600,
              settings: {
                  item:1,
                  slideMove:1
                }
          }
      ]
  });  
});