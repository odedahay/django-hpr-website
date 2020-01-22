// document.addEventListener("DOMContentLoaded", function(){
    
//     const navigation = document.querySelector(".main-navigation");
//     const siteHeader = document.querySelector('.site-header');
//     const mobileIcon = document.querySelector('.mobile-menu i');

//     mobileIcon.addEventListener('click', function(){
//        if(navigation.classList.contains('mobile-active')){
//            navigation.classList.remove('d-flex', 'mobile-active');
//            return;
//        }else{
//          navigation.classList.add('d-flex', 'mobile-active', 'fixed-top');
//        }

       
//     })

//     // Fixed navigation on top

//     const fixedNavigation = () => {
//         if (window.innerWidth > 768) {
//             window.onscroll = () => {
//                 if (window.scrollY > 0) {
//                     navigation.classList.add('fixed-top');
//                     navigation.classList.add("logo-small");
                    
//                 } else {
//                     navigation.classList.remove("fixed-top");
//                     navigation.classList.remove("logo-small");
                 
//                 }
//             }   
//         } else {
//             navigation.classList.remove('fixed-top');
//         }
//     }

//     fixedNavigation();

//     window.addEventListener('resize', function () {
//         fixedNavigation();
//     })

// });