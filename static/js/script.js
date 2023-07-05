// Owlcarousel
$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
      loop:true,
    margin:10,
    nav:true,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true,
    center: true,
    navText: [
        "<i class='fa fa-angle-left'></i>",
        "<i class='fa fa-angle-right'></i>"
    ],
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:3
        }
    }
  });
});


const mobileNavShow = document.querySelector('.mobile-nav-show');
const mobileNavHide = document.querySelector('.mobile-nav-hide');

document.querySelectorAll('.mobile-nav-toggle').forEach(el => {
  el.addEventListener('click', function(event) {
    event.preventDefault();
    mobileNavToogle();
  })
});

function mobileNavToogle() {
  document.querySelector('head').classList.toggle('mobile-nav-active');
  mobileNavShow.classList.toggle('d-none');
  mobileNavHide.classList.toggle('d-none');
}


  $(document).ready(function(){
    $('.carousel').slick({
      // Options de configuration de Slick Carousel (si nécessaire)
      dots: true, // Afficher les indicateurs de pagination
      infinite: true, // Faire défiler en boucle le carousel
      slidesToShow: 3, // Nombre de diapositives à afficher à la fois
      slidesToScroll: 1, // Nombre de diapositives à faire défiler à la fois
      // Autres options personnalisées peuvent être ajoutées ici
    });
  });

