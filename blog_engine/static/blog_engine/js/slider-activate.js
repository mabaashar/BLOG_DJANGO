$(document).ready(function() {
  //SLIDER 1
  var owl = $('#owl-1');
  owl.owlCarousel({
    items: 4,
    loop: true,
    margin: 4,
    autoplay: true,
    autoplayTimeout: 1000,
    autoplayHoverPause: true,
    center: true
  });

  //SLIDER 2
  var owl2 = $('#owl-2');
  owl2.owlCarousel({
    items: 3,
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 2000,
    autoplayHoverPause: true,
    center: true
  });


});

