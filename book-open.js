// 책을 누르면 표지가 열리고 속지가 스르르 넘어간 뒤 상세 페이지로 들어가기.
// transform·opacity만 움직임. 움직임을 꺼 둔 사용자, 새 탭 열기(ctrl·cmd·가운데 클릭)는 그냥 이동.
(function(){
  if(!document.body.animate)return;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)');
  var busy=false,layer=null,hidden=null;

  function coverFor(a){
    return a.querySelector('.cover')||
      (a.closest('.entry')&&a.closest('.entry').querySelector('.cover'))||null;
  }
  function face(src){
    var cs=getComputedStyle(src),d=document.createElement('div');
    ['backgroundColor','backgroundImage','backgroundSize','backgroundPosition','backgroundRepeat'].forEach(function(k){d.style[k]=cs[k]});
    return d;
  }
  function el(cls,parent){var d=document.createElement('div');d.className=cls;parent.appendChild(d);return d}

  function open(a,cover){
    busy=true;
    var r=cover.getBoundingClientRect(),vw=innerWidth,vh=innerHeight;
    // 화면 가운데, 펼친 두 쪽이 다 들어오는 크기로
    var s=Math.min(vh*.62/r.height,vw*.44/r.width,3.2);

    layer=el('bo-layer',document.body);layer.setAttribute('aria-hidden','true');
    var dim=el('bo-dim',layer);
    var book=el('bo-book',layer);
    book.style.cssText='left:'+r.left+'px;top:'+r.top+'px;width:'+r.width+'px;height:'+r.height+'px';
    var block=el('bo-block',book);
    var sheets=[el('bo-sheet',book),el('bo-sheet',book),el('bo-sheet',book)];
    var front=el('bo-cover',book);
    var outside=face(cover);outside.className='bo-out';front.appendChild(outside);
    el('bo-in',front);
    var veil=el('bo-veil',layer);
    hidden=cover;cover.style.visibility='hidden';

    var ease='cubic-bezier(.645,.045,.355,1)';
    // 1) 책이 화면 가운데로 떠오름. 책등이 화면 가운데에 오게 해서 열린 두 쪽이 균형 있게
    var tx=vw/2-r.left, ty=vh/2-(r.top+r.height/2);
    book.animate([
      {transform:'translate(0,0) scale(1)'},
      {transform:'translate('+tx+'px,'+ty+'px) scale('+s+')'}
    ],{duration:520,easing:ease,fill:'forwards'});
    dim.animate([{opacity:0},{opacity:.88}],{duration:520,easing:'ease-out',fill:'forwards'});
    // 2) 표지가 열림
    front.animate([{transform:'rotateY(0deg)'},{transform:'rotateY(-168deg)'}],
      {duration:780,delay:380,easing:'cubic-bezier(.3,.1,.25,1)',fill:'forwards'});
    // 3) 속지가 한 장씩 스르르
    sheets.forEach(function(p,i){
      p.animate([{transform:'rotateY(0deg)'},{transform:'rotateY(-'+(162-i*4)+'deg)'}],
        {duration:620,delay:700+i*150,easing:'cubic-bezier(.35,.05,.3,1)',fill:'forwards'});
    });
    // 4) 흰 종이빛으로 덮이며 다음 페이지로
    var last=veil.animate([{opacity:0},{opacity:1}],{duration:380,delay:1200,easing:'ease-in',fill:'forwards'});
    last.onfinish=function(){
      try{sessionStorage.setItem('bookOpen','1')}catch(e){}
      location.href=a.href;
    };
  }

  function reset(){
    if(layer){layer.remove();layer=null}
    if(hidden){hidden.style.visibility='';hidden=null}
    busy=false;
  }
  // 뒤로 가기로 돌아왔을 때(페이지 캐시) 펼친 책 지우기
  addEventListener('pageshow',function(e){if(e.persisted)reset()});

  document.addEventListener('click',function(e){
    if(busy||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    if(reduce&&reduce.matches)return;
    var a=e.target.closest&&e.target.closest('a[href]');
    if(!a||!/(^|\/)book[\w-]*\.html(\?|#|$)/.test(a.getAttribute('href'))||a.target)return;
    var cover=coverFor(a);if(!cover)return;
    var r=cover.getBoundingClientRect();
    if(r.width<20||r.bottom<0||r.top>innerHeight)return; // 화면 밖이면 그냥 이동
    e.preventDefault();open(a,cover);
  });
})();
