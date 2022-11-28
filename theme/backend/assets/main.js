let close_message = document.querySelector("main .details_box_shiment .header__box .fa-xmark");
let messageBox = document.querySelector(".message__box");
let box__Views = document.querySelector(".details_box_shiment")
let mm =  document.querySelector('.Views_Shipment')
let kkkk = document.querySelector('.kkkk')
let product_pub = document.querySelector('.published_btn')
let pub_icon = document.querySelector('.pub_icon')

pub_icon.addEventListener("click", function(){
   console.log("product_pub clicked ")
   product_pub.classList.toggle('active');

   pub_icon.classList.toggle('fa-eye');
   pub_icon.classList.toggle('fa-eye-slash');
});
mm.addEventListener("click", function(){
   box__Views.classList.add('active');
   kkkk.classList.add('active');
});
close_message.addEventListener("click", function(){
   box__Views.classList.remove('active');
   kkkk.classList.remove('active');
});


