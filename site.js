// Apparition en douceur des blocs au défilement (coupée si l'appareil demande moins de mouvement).
(function(){
  if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  document.documentElement.classList.add('js');
  var els=document.querySelectorAll('section .wrap>*, .services>div, .reviews>figure, .faq-liste>details, .contact .wrap>*');
  els.forEach(function(el){el.classList.add('reveal');var k=Array.prototype.indexOf.call(el.parentElement.children,el);el.style.transitionDelay=(Math.min(k,7)*70)+'ms';});
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var t=e.target;t.classList.add('vu');io.unobserve(t);setTimeout(function(){t.style.transitionDelay='';},1200);}});},{rootMargin:'0px 0px -8% 0px'});
  els.forEach(function(el){io.observe(el);});
})();

// Carrousel des réalisations : flèches, points et glisser au doigt (défilement natif).
(function(){
  document.querySelectorAll('.carrousel').forEach(function(c){
    var piste=c.querySelector('.piste'),slides=piste.children,points=c.querySelectorAll('.points button');
    var sec=c.closest('section'),prec=sec&&sec.querySelector('.fleche.prec'),suiv=sec&&sec.querySelector('.fleche.suiv');
    function pas(){return slides.length>1?slides[1].offsetLeft-slides[0].offsetLeft:piste.clientWidth;}
    function aller(i){i=Math.max(0,Math.min(slides.length-1,i));piste.scrollTo({left:slides[i].offsetLeft-slides[0].offsetLeft});}
    function actuel(){return Math.round(piste.scrollLeft/pas());}
    function maj(){
      var i=actuel(),fin=piste.scrollLeft+piste.clientWidth>=piste.scrollWidth-4;
      if(fin)i=slides.length-1;
      points.forEach(function(p,k){if(k===i)p.setAttribute('aria-current','true');else p.removeAttribute('aria-current');});
      if(prec)prec.disabled=piste.scrollLeft<4;
      if(suiv)suiv.disabled=fin;
    }
    points.forEach(function(p,k){p.addEventListener('click',function(){aller(k);});});
    if(prec)prec.addEventListener('click',function(){aller(actuel()-1);});
    if(suiv)suiv.addEventListener('click',function(){aller(actuel()+1);});
    piste.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){e.preventDefault();aller(actuel()+1);}if(e.key==='ArrowLeft'){e.preventDefault();aller(actuel()-1);}});
    var t;piste.addEventListener('scroll',function(){clearTimeout(t);t=setTimeout(maj,60);},{passive:true});
    window.addEventListener('resize',maj);maj();
  });
})();
