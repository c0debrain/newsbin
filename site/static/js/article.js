var block=document.getElementById("js-localize-date");if(null!=block){var date=new Date(block.getAttribute("iso"));block.innerHTML=date.toLocaleDateString()+" "+date.toLocaleTimeString()}HTMLDocument.prototype.createElementWithAttr=function(t,e){var n=this.createElement(t);for(attr in e)n.setAttribute(attr,e[attr]);return n};var modal=function(t){var e={modal:document.getElementById("js-annotation-modal"),contents:document.createElementWithAttr("div",{class:"modal-container"}),part:{close:document.createElementWithAttr("div",{class:"modal-close",onClick:"modal.close()"}),title:document.createElementWithAttr("div",{class:"modal-title"}),image:document.createElementWithAttr("img",{class:"modal-image"}),card:document.createElementWithAttr("div",{class:"modal-data"}),content:document.createElementWithAttr("div",{class:"modal-content"}),link:document.createElementWithAttr("a",{class:"modal-link",target:"_blank"})}};e.modal.appendChild(e.contents);for(item in e.part)e.contents.appendChild(e.part[item]);return e.part.link.innerHTML="wikipedia",e.part.close.innerHTML="Close",{display:function(t){var n=new XMLHttpRequest,a="/annotations?name="+t;n.onload=function(){if(200==this.status){var t=JSON.parse(this.responseText);e.part.title.innerHTML=t.name,e.part.image.setAttribute("src",t.image),e.part.content.innerHTML=t.summary,e.part.link.setAttribute("href","https://en.wikipedia.org/wiki/"+t.name),e.modal.style.display="flex",console.log(t),null!=t.slug&&null!=t.truth_score?e.part.card.innerHTML='Truth rating: <span class="truth-rating" style="background-color:hsl('+t.truth_score+',100%,50%);" >'+t.truth_score+'%</span><br/><span class="truth-disclaimer" >(<a href="http://www.politifact.com/personalities/'+t.slug+'" target="_blank">based on last five statements</a>)</span>':e.part.card.innerHTML=""}},n.open("GET",a,!0),n.send()},close:function(){e.part.title.innerHTML="",e.part.image.setAttribute("src","#"),e.part.content.innerHTML="",e.part.link.setAttribute("href","#"),e.modal.style.display="none"}}}(),annotations=document.getElementsByClassName("annotation");if(annotations)for(var i=0;i<annotations.length;i++)annotations[i].addEventListener("click",function(t){modal.display(this.getAttribute("name"))});var content=document.getElementById("js-capture-selection");content&&content.addEventListener("mouseup",function(){var t=window.getSelection();if(!t.isCollapsed&&1==t.rangeCount){var e=t.getRangeAt(0),n=document.getElementById("js-add-selection");n&&e&&(n.value=e.toString())}}),menu_tab=document.getElementById("js-tab-menu"),article_tab=document.getElementById("js-tab-article"),menu_form=document.getElementById("js-sidebar-anno-menu"),menu_tab&&menu_tab.addEventListener("click",function(t){this.classList.toggle("current")?(article_tab.classList.remove("current"),menu_form.classList.add("open")):(article_tab.classList.add("current"),menu_form.classList.remove("open"))}),article_tab&&article_tab.addEventListener("click",function(t){this.classList.toggle("current")?(menu_tab.classList.remove("current"),menu_form.classList.remove("open")):(menu_tab.classList.add("current"),menu_form.classList.add("open"))});