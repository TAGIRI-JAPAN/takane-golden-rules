"use strict";
(() => {
  const phrases=JSON.parse(document.querySelector("#phrase-data").textContent);
  const $=selector=>document.querySelector(selector);
  const audio=$("#phrase-audio");
  const rows=[...document.querySelectorAll(".phrase")];
  const sections=[...document.querySelectorAll(".section-label")];
  const tabs=[...document.querySelectorAll(".role-tab")];
  const playIcon='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 10 7-10 7z"/></svg><span>聞く</span>';
  const pauseIcon='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5v14M15 5v14"/></svg><span>停止</span>';
  let role="all",visible=phrases.map(p=>p.id),current=1,timer=null,sequence=0;
  let loaded=0;
  const phrase=id=>phrases[id-1];
  const number=id=>String(id).padStart(3,"0");
  function cancelGap(){if(timer!==null){clearTimeout(timer);timer=null;}}
  function status(text){$("#player-status").textContent=text;}
  function setActive(id){
    current=id;
    rows.forEach(row=>row.classList.toggle("is-current",Number(row.dataset.id)===id));
    const p=phrase(id);
    $("#now-number").textContent=number(id);
    $("#now-text").textContent=p.jp;
    $("#current-download").href=p.audio;
    $("#current-download").download=number(id)+".mp3";
    audio.setAttribute("aria-label",number(id)+"番 "+p.jp);
    $("#previous").disabled=visible.indexOf(current)<=0;
    $("#next").disabled=visible.indexOf(current)===visible.length-1 || !visible.includes(current);
    if(location.hash!=="#p"+number(id))history.replaceState(null,"","#p"+number(id));
  }
  function syncButtons(){
    rows.forEach(row=>{
      const playing=Number(row.dataset.id)===current&&!audio.paused;
      row.classList.toggle("is-playing",playing);
      const link=row.querySelector(".play-phrase");
      link.innerHTML=playing?pauseIcon:playIcon;
      link.setAttribute("aria-label",number(Number(row.dataset.id))+"番 "+phrase(Number(row.dataset.id)).jp+(playing?"を一時停止":"を再生"));
    });
  }
  async function play(id){
    cancelGap();
    const attempt=++sequence;
    status("");
    if(loaded!==id){audio.src=phrase(id).audio;loaded=id;}
    setActive(id);
    audio.playbackRate=Number($("#speed").value);
    try{await audio.play();}
    catch(error){if(attempt!==sequence)return;$("#continuous").checked=false;status(error.name==="NotAllowedError"?"下の再生ボタンを押すと、音声が始まります。":"音声を読み込めませんでした。もう一度「聞く」を押してください。");}
    syncButtons();
  }
  function stop(){sequence++;cancelGap();audio.pause();syncButtons();}
  function navigate(direction){
    const position=visible.indexOf(current);
    const next=position<0?visible[0]:visible[position+direction];
    if(next)play(next);
  }
  function filter(){
    const query=$("#search").value.trim().toLocaleLowerCase();
    const category=Number($("#category").value);
    visible=[];
    rows.forEach(row=>{
      const p=phrase(Number(row.dataset.id));
      const matchesRole=role==="all"||(role==="give"?p.id<=50:p.id>50);
      const matchesCategory=!category||p.group===category;
      const search=[p.jp,p.kana,p.en,String(p.id),number(p.id)].join(" ").toLocaleLowerCase();
      const show=matchesRole&&matchesCategory&&(!query||search.includes(query));
      row.hidden=!show;if(show)visible.push(p.id);
    });
    sections.forEach(heading=>{heading.hidden=!rows.some(row=>!row.hidden&&row.dataset.group===heading.dataset.group);});
    $("#result-count").textContent=visible.length+" / 100 文";
    $("#play-all-label").textContent=visible.length===100?"1番から、続けて聞く":"表示中の"+visible.length+"文を続けて聞く";
    $("#play-all").disabled=visible.length===0;
    $("#empty").hidden=visible.length!==0;
    if(!visible.includes(current)){stop();$("#continuous").checked=false;}
    $("#previous").disabled=visible.indexOf(current)<=0;
    $("#next").disabled=visible.indexOf(current)===visible.length-1||!visible.includes(current);
  }
  rows.forEach(row=>row.querySelector(".play-phrase").addEventListener("click",event=>{
    event.preventDefault();
    const id=Number(row.dataset.id);
    if(id===current&&!audio.paused){stop();return;}
    $("#continuous").checked=false;
    if(id===loaded&&audio.ended)audio.currentTime=0;
    play(id);
  }));
  tabs.forEach(tab=>tab.addEventListener("click",()=>{
    role=tab.dataset.role;tabs.forEach(item=>item.setAttribute("aria-pressed",String(item===tab)));
    $("#category").value="0";filter();
  }));
  $("#search").addEventListener("input",filter);
  $("#category").addEventListener("change",filter);
  $("#show-reading").addEventListener("change",event=>document.body.classList.toggle("hide-reading",!event.target.checked));
  $("#show-english").addEventListener("change",event=>document.body.classList.toggle("hide-english",!event.target.checked));
  $("#speed").addEventListener("change",event=>{audio.playbackRate=Number(event.target.value);});
  $("#previous").addEventListener("click",()=>navigate(-1));
  $("#next").addEventListener("click",()=>navigate(1));
  $("#play-all").addEventListener("click",()=>{
    if(!visible.length)return;
    $("#continuous").checked=true;$("#repeat").checked=false;
    if(loaded===visible[0])audio.currentTime=0;
    play(visible[0]);
  });
  $("#continuous").addEventListener("change",()=>{cancelGap();if($("#continuous").checked)$("#repeat").checked=false;});
  $("#repeat").addEventListener("change",()=>{cancelGap();if($("#repeat").checked)$("#continuous").checked=false;});
  audio.addEventListener("play",()=>{status("");syncButtons();});
  audio.addEventListener("pause",syncButtons);
  audio.addEventListener("error",()=>{stop();$("#continuous").checked=false;$("#repeat").checked=false;status("音声を読み込めませんでした。もう一度「聞く」を押してください。");});
  audio.addEventListener("ended",()=>{
    syncButtons();cancelGap();
    let next=null;
    if($("#repeat").checked)next=current;
    else if($("#continuous").checked){const index=visible.indexOf(current);if(index>=0)next=visible[index+1];}
    if(next){
      status($("#repeat").checked?"もう一度、同じ文を聞きます。":"次は "+number(next)+"番です。");
      timer=setTimeout(()=>{timer=null;if(next===current)audio.currentTime=0;play(next);},Number($("#gap").value)*1000);
    }else if($("#continuous").checked){$("#continuous").checked=false;status("表示中のフレーズを、最後まで再生しました。");}
  });
  document.addEventListener("keydown",event=>{if(event.key==="Escape"){stop();$("#continuous").checked=false;$("#repeat").checked=false;}});
  const hash=location.hash.match(/^#p(\d{3})$/);
  if(hash){const id=Number(hash[1]);if(id>=1&&id<=100){setActive(id);document.querySelector("#p"+number(id)).scrollIntoView({block:"center"});}}
  filter();
})();
