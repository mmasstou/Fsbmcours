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