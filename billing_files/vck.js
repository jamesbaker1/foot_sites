if(typeof asset_host!="string"||asset_host=='https://d2j3qa5nc37287.cloudfront.net/')window.asset_host="https://cdn.us8.co/";if(window.asset_host.substring(0,2)=="//")window.asset_host="https:"+window.asset_host;if(window.asset_host.substring(window.asset_host.length-1)!="/")window.asset_host=window.asset_host+"/";window.ju_host=window.asset_host.split('.')[1]+'.'+window.asset_host.split('.')[2].replace('/','');window.ju_domain='https://my.'+window.ju_host;function ju_loadversionscript(v,vr){if(window.ju_alreadyloaded)return
(function(){var s=document.createElement("script");s.type="text/javascript";s.async=true;s.src=asset_host+"mwgt_"+v+".js?v="+vr;var x=document.getElementsByTagName("script")[0];x.parentNode.insertBefore(s,x);})();}
function jju_setCookie(name,value,days,path){var today=new Date();today.setTime(today.getTime()+days*24*60*60*1000);document.cookie=name+"="+escape(value)+";expires="+(days==-1?"Thu, 01 Jan 1970 00:00:01 GMT":today.toGMTString())+(path?";path="+path:"");}
function jju_getCookie(c_name){var i,x,y,ARRcookies=document.cookie.split(";");for(i=0;i<ARRcookies.length;i++){x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);x=x.replace(/^\s+|\s+$/g,"");if(x==c_name){return unescape(y);}}
return "";}
function isNumeric(n){return!isNaN(parseFloat(n))&&isFinite(n);}
var $jujsonp=(function(){var that={};that.send=function(src,options){var callback_name=options.callbackName||"callback",on_success=options.onSuccess||function(){},on_timeout=options.onTimeout||function(){},timeout=options.timeout||10;var timeout_trigger=window.setTimeout(function(){window[callback_name]=function(){};on_timeout();},timeout*1000);window[callback_name]=function(data){window.clearTimeout(timeout_trigger);on_success(data);};var script=document.createElement("script");script.type="text/javascript";script.async=true;script.src=src;document.getElementsByTagName("head")[0].appendChild(script);};return that;})();var ju_v=jju_getCookie("_ju_v");var ju_vr="";if(ju_v&&ju_v.indexOf("_")!=-1){var ju_v_arr=ju_v.split("_");ju_v=ju_v_arr[0];ju_vr=ju_v_arr[1];ju_loadversionscript(ju_v,ju_vr);}else{if(ju_num.match(/^[{]?[0-9a-fA-F]{8}[-]?([0-9a-fA-F]{4}[-]?){3}[0-9a-fA-F]{12}[}]?$/)){$jujsonp.send(ju_domain+"/ajax/account_version_check.html?id="+ju_num,{callbackName:"ju_vcheck",onSuccess:function(json){ju_v=json.v;ju_vr=json.vr;jju_setCookie("_ju_v",ju_v+"_"+ju_vr,0.0208,"/");ju_loadversionscript(ju_v,ju_vr);}});}}