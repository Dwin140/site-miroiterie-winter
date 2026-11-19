// Apparition en douceur des blocs au défilement (coupée si l'appareil demande moins de mouvement).
(function(){
  if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  document.documentElement.classList.add('js');
  var els=document.querySelectorAll('section .wrap>*, .services>div, .reviews>figure, .faq-liste>details, .contact .wrap>*');
  els.forEach(function(el){el.classList.add('reveal');var k=Array.prototype.indexOf.call(el.parentElement.children,el);el.style.transitionDelay=(Math.min(k,7)*70)+'ms';});
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var t=e.target;t.classList.add('vu');io.unobserve(t);setTimeout(function(){t.style.transitionDelay='';},1200);}});},{rootMargin:'0px 0px -8% 0px'});
  els.forEach(function(el){io.observe(el);});
})();
