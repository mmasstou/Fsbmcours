let close_message = document.querySelector("main .details_box_shiment .header__box .fa-xmark");
let messageBox = document.querySelector(".message__box");
let box__Views = document.querySelector(".details_box_shiment")
let mm =  document.querySelector('.Views_Shipment')
let kkkk = document.querySelector('.kkkk')
let darkModeBtn = document.querySelector('.dark_mode_incons')
let Body = document.querySelector(".body_container")
let profile_btn = document.querySelector(".user__avatar")
let notification_btn =  document.querySelector(".notification")
let profile_box =  document.querySelector(".profile_box")
let notification_box =  document.querySelector(".notification_box")
let menu_btn = document.getElementById("menu-btn")
let main__nav = document.querySelector(".main__nav")
// mm.addEventListener("click", function(){
//    box__Views.classList.add('active');
//    kkkk.classList.add('active');
// });
// close_message.addEventListener("click", function(){
//    box__Views.classList.remove('active');
//    kkkk.classList.remove('active');
// });
menu_btn.addEventListener("click", function(){
    console.log("menu_btn Clicked !")
    main__nav.classList.toggle("active")
 });
notification_btn.addEventListener("click", function(){
   console.log("notification Clicked !")
   notification_box.classList.toggle('notification_active')
});
  
profile_btn.addEventListener("click", function(){
    console.log("profile Clicked !")
    profile_box.classList.toggle('profile_active')
});
darkModeBtn.addEventListener("click", function(){
    console.log("dark mode btn clicked ")
  darkModeBtn.classList.toggle('fa-moon')
  darkModeBtn.classList.toggle('fa-sun')
  Body.classList.toggle('dark_active')
  // Body.classList.replace('dark_active', 'dark_deactive')
});

var myNav = document.getElementById("Header");
window.onscroll = function () { 
    if (document.body.scrollTop >= 100 || document.documentElement.scrollTop >= 100 ) {
        myNav.classList.add("nav-colored");
        myNav.classList.remove("nav-transparent");
    } 
    else {
        myNav.classList.add("nav-transparent");
        myNav.classList.remove("nav-colored");
    }
};


// slide

let prev_slid = document.getElementsByClassName("prev");
let next_slid = document.getElementsByClassName("next");
let product = document.getElementsByClassName("Products_card");
let product_page = Math.ceil(product.length/4);
let l = 0;
let movePre = 25.34;
let maxMove = 205;
let mobil_view = window.matchMedia("(max-width: 768px)");
if (mobil_view.matches){
    movePre = 50.36;
    maxMove = 504;
}
let right_move = ()=>{
    l = l + movePre;
}
// Portfolio slider
var numberOfSlides = document.querySelectorAll('.swiper-slide').length;
new Swiper('.swiper', {
    loop: false,
    allowSlidePrev: numberOfSlides !== 1,
    allowSlideNext: numberOfSlides !== 1,
    breakpoints: {
        0: {
            slidesPerView: 2,
            spaceBetween: 16,
        },
        769: {
            slidesPerView: 3,
            spaceBetween: 32,
        },
        1151: {
            slidesPerView: 4,
            spaceBetween: 26,
        },
    },
    navigation: {
        nextEl: '.slider-navigation .next',
        prevEl: '.slider-navigation .prev',
    },
});