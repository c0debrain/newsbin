NodeList.prototype.forEach||(NodeList.prototype.forEach=function(e,t){for(var n=0,s=this.length;n<s;++n)e.call(t,this[n],n,this)});var options=function(e){for(var t=null,n=[],s=0;s<e.length;s++){var o=e[s];"all_label"==o.id?t=o:n.push(o),o.box=o.getElementsByTagName("input")[0],o.box.id in sessionStorage&&(o.box.checked="false"!=sessionStorage.getItem(o.box.id)),o.classList.toggle("mark",o.box.checked),o.addEventListener("change",function(e){this.id in i?i[this.id](this):i.default(this)})}var i={all_label:function(e){n.forEach(function(t){t.box.checked=e.box.checked}),this.update()},default:function(e){t.box.checked=n.every(function(e){return e.box.checked}),this.update()},update:function(){for(var t=0;t<e.length;t++){var n=e[t];n.classList.toggle("mark",n.box.checked),window.sessionStorage.setItem(n.box.id,n.box.checked)}}}}(document.getElementsByClassName("option-item"));!function(e){for(var t=0;t<e.length;t++){var n=e[t];n.id in sessionStorage?n.value=sessionStorage.getItem(n.id):sessionStorage.setItem(n.id,n.value),n.addEventListener("change",function(e){this.id&&sessionStorage.setItem(this.id,this.value)})}}(document.querySelectorAll('input[type="text"], input[type="number"], select')),function(e){e&&(e.innerHTML=(new Date).getFullYear())}(document.getElementById("js-year")),function(e,t){var n=[];[].push.apply(n,e.getElementsByTagName("div"));var s={open_menu:function(){t.classList.add("open")},close_menu:function(){t.classList.remove("open")}};n.forEach(function(e){e.addEventListener("click",function(e){this.classList.contains("current")||(n.forEach(function(e){e.classList.remove("current")}),this.classList.add("current"),s[this.getAttribute("run")]())})})}(document.getElementById("js-mobile-menu"),document.getElementById("js-menu"));