let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick=()=> {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

window.onscroll=()=>{
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
}

const typed = new Typed('.multiple-text', {
    strings: ['Data Analyst', 'Business Analyst'],
    typeSpeed: 80,
    backSpeed: 80,
    backDelay: 1200,
    loop: true,
  });

// Sliding Cards Feature
(function () {
    const slider = document.querySelector('.slider');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
  
    let currentIndex = 0;
  
    prevButton.addEventListener('click', () => {
      currentIndex = Math.max(currentIndex - 1, 0);
      slider.style.transform = `translateX(-${currentIndex * 300}px)`;
    });
  
    nextButton.addEventListener('click', () => {
      currentIndex = Math.min(currentIndex + 1, slider.children.length - 1);
      slider.style.transform = `translateX(-${currentIndex * 300}px)`;
    });
  })();
  