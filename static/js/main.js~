
		ip = "10.3.8.158";
		port = "8010";
		conn = "https";
		whatisopened = 0
		Academics = {};
                Sports = {};
                Events = {};
                Cultural = {};
                Urgent = {};
                LostFound = {};
                General = {};
                other = {};
                BigTable = {};
		globallist = ["Academics","Sports","Events","Cultural","Urgent","LostFound","General","SentMails"];
		var flag = "Academics";

		var activeelement = document.getElementById("tabs").children[0];
		var sa = document.getElementById("inboxme");
		var draftlist = {};
		var draftsubject = "";
		var draftmessage = "";
		var draftreceivers = {};
		var deletedraftlist = [];
		var deletesentlist = [];
		var completelist;
                var cuckoo;
		
		
function clickmailicons(e){
	//console.log(e.name);
	if(e.name=="reply")
		replymail();
	else if(e.name=="forward")
		forwardmail();
	else if(e.name=="delete")
		deletemail();
	else if(e.name=="important")
		markimportant();
	else if(e.name=="read")
		markread();
	else if(e.name=="unread")
		markunread();
	gettagcount();
}

function replymail(){
	
	$("#composer").show();
	$("#sender").show();
        $("#close").show();
	
	sa.className = "down";
        e = document.getElementById("composeme");
 	e.className = "sideactive";
        sa = e;
	
	document.getElementById("inboxer").style.display = "none";
        document.getElementById("maildetails").style.display = "none";	

	comp=document.getElementById("composer");
	if(comp.children[2].children[3].childElementCount==1){
		comp.children[2].children[3].removeChild(comp.children[2].children[3].children[0]);
		newdom=document.createElement("ul");
		newdom.id="receivers";
		comp.children[2].children[3].appendChild(newdom);
	}
	uldiv=comp.children[2].children[3].children[0];
	
	newli=document.createElement("li");
	var text=document.createTextNode(activejson.send_id);
	newli.appendChild(text);
	newli.className="rev";
	uldiv.appendChild(newli);

	comp.children[2].children[7].value="RE: " + activejson.sub;
}

function forwardmail(){
	$("#composer").show();
	$("#sender").show();
        $("#close").show();
	
	sa.className = "down";
        e = document.getElementById("composeme");
 	e.className = "sideactive";
        sa = e;
	
	document.getElementById("inboxer").style.display = "none";
        document.getElementById("maildetails").style.display = "none";

	comp=document.getElementById("composer");
	comp.children[2].children[7].value=activejson.sub;

	comp.children[2].children[9].value=activejson.msg;
		
}
function deletemail(){
	if(whatisopened==0)
	{	
		inboxDelete();
		refreshs("Mails Deleted!");	
	}
	else
	{
		$("#maildetails").hide(function(){
			$("#inboxer").fadeIn();
			whatisopened = 0;
		});
		count="";
		count+=activejson.id+">";
		
		//console.log(activejson.id)
		var xml = new XMLHttpRequest();
				xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/deleteInbox?count="+count, true);
				xml.send();
				xml.onreadystatechange = function(){
					if(xml.readyState == 4 && xml.status == 200){
						
					}
				}
	}
	
}

function markimportant(){
	if(whatisopened)
	{
	xml=new XMLHttpRequest;
	xml.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/setimportant?myjson="+JSON.stringify(activejson)+"&id="+activejson.id,true)
	xml.send();
	xml.onreadystatechange=function(){
		if(xml.readyState==4 && xml.status==200)
		{
			animatemsg("Marked important");
		}
	}
	}
	else
	{
		markimpmails();
		refreshs("Marked Important!");
	}
}

function markread(){
	if(whatisopened)
	{
		xml=new XMLHttpRequest;
	xml.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/setread?myjson="+JSON.stringify(activejson)+"&id="+activejson.id,true)
	xml.send();
	xml.onreadystatechange=function(){
		if(xml.readyState==4 && xml.status==200)
		{
			animatemsg("Marked unread");
		}
	}
		animatemsg("Already marked read");	
	}
	else
	{
		markreadmails();
		refreshs("Marked Read!");	
	}
	
}

function markunread(){
	if(whatisopened)
	{
	xml=new XMLHttpRequest;
	xml.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/setunread?myjson="+JSON.stringify(activejson)+"&id="+activejson.id,true)
	xml.send();
	xml.onreadystatechange=function(){
		if(xml.readyState==4 && xml.status==200)
		{
			animatemsg("Marked Unread!");
		}
	}
	}
	else
	{
		markunreadmails();
		refreshs("Marked Unread!");
	}
}
		function refreshs(txt)
		{
				animatemsg(txt);
				openinbox(activeelement);
		}
		function attach(){
			var xml = new XMLHttpRequest();
			xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/attach", true);
			xml.send();
			xml.onreadystatechange = function(){
				if(xml.readyState == 4 && xml.status == 200){
					var re = xml.responseText;
				}
			}
		}	

	function opensearchdetails(e)
	{
	  		        $("#inboxer").hide();
					$("#imgreply").fadeIn();
					$("#imgforward").fadeIn();
					$("#searchbox").hide();
					$("#searchdiv").hide();
					gettagcount();
					document.getElementById("mailicons").style.visibility="visible";
	
					tmp=e.id.slice(6);
		newobj=searchjson[tmp];
		activejson=newobj;
		thisjson=activejson;
		var xml1= new XMLHttpRequest;
	xml1.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/setread?myjson="+JSON.stringify(activejson)+"&id="+activejson.id,true);
	xml1.send();
	xml1.onreadystatechange = function()
	{
		if( xml1.readyState == 4 && xml1.status == 200 )
		{
			gettagcount();		//alert(xml.responseText)
			console.log("readdetailssent");	
		}
	}
	var div=document.getElementById("maildetails");
	div.style.display="block";

			var xml;
			xml = new XMLHttpRequest();
			xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/attachment2?id="+thisjson.id, true);
			xml.send();
       
        		div.innerHTML="<div id=\"topdiv\"><div id=\"subjectdetails\"><h2>"+thisjson.sub+"</h2></div><div id=\"fromdetails\"><p>From:"+thisjson.send_id+"</p><p>Time:"+thisjson.sent_time+"</p><p>Date:"+thisjson.sent_date+"</p></div></div><div id=\"mailcontent\">"+thisjson.msg+"</div><div id=\"Sentdivider2\"></div><div id=\"mailattachments\" style=\"position:absolute;top:40%;left:80%\">Your Attachments</div><div id=\"attachINBOX\" style=\"position:absolute;left:81%;top:60%\"></div>";
			var attack = document.getElementById("attachINBOX")
			xml.onreadystatechange = function(){
				if(xml.readyState == 4 && xml.status == 200){
					attachments = xml.responseText;
					attachments = attachments.split(">");
					attack.innerHTML = attachments[0];
					br = document.createElement("br");
					attack.appendChild(br);
					if(attachments.length == 2){
						button = document.createElement("a");
						button2 = document.createElement("button")
						button2.innerHTML = "Download Attachment";
						button.href = conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/default/download/"+attachments[1];
						button.target = "_blank"
						button2.style = "position:absolute; top:200%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"
						button2.onmouseover= function(){button2.style = "position:absolute; top:200%; width:120px; background-color:#006699; transition: all 0.5 ease; border-radius: 133px;opacity:1;color:white;cursor:pointer"}
						button2.onmouseout = function(){button2.style = "position:absolute; top:200%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"}
						button.appendChild(button2)
						attack.appendChild(button);
					}
				}
			}
	}
                function opendetails(e){
      		        $("#inboxer").hide();
					$("#imgreply").fadeIn();
					$("#imgforward").fadeIn();
					$("#searchdiv").hide();
					whatisopened = 1

					gettagcount();
	document.getElementById("mailicons").style.visibility="visible";
	var tmp=e.id.slice(-4);
	//console.log(tmp);
	var tag=null;
	if(isNaN(tmp))
	{
		if(isNaN(tmp.slice(1)))
		{
			if(isNaN(tmp.slice(2)))
			{
				tag=e.id.slice(7,-1);
				tmp=e.id.slice(-1);
			}
			else
			{
				tag=e.id.slice(7,-2);
				tmp=e.id.slice(-2);
			}
		}
	}
	else
	{
		tag=e.id.slice(7,-3);
		tmp=e.id.slice(-3);
	}
	//console.log(tag);
	tagjson=eval(tag);
	thisjson=tagjson[tmp];
	
	thisjson.red=1;
	activejson=thisjson; 
	//console.log(activejson);
	receiver_id=document.getElementById("idofuser").innerHTML;
	//console.log(activejson.id)
       		       
	var xml1= new XMLHttpRequest;
	xml1.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/setread?myjson="+JSON.stringify(activejson)+"&id="+activejson.id,true);
	xml1.send();
	xml1.onreadystatechange = function()
	{
		if( xml1.readyState == 4 && xml1.status == 200 )
		{
			
		gettagcount();		//alert(xml.responseText)
			console.log("readdetailssent");	
		}
	}
	var div=document.getElementById("maildetails");
	div.style.display="block";

			var xml;
			xml = new XMLHttpRequest();
			xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/attachment2?id="+thisjson.id, true);
			xml.send();
       
        		div.innerHTML="<div id=\"topdiv\"><div id=\"subjectdetails\"><h2>"+thisjson.sub+"</h2></div><div id=\"fromdetails\"><p>From:"+thisjson.send_id+"</p><p>Time:"+thisjson.sent_time+"</p><p>Date:"+thisjson.sent_date+"</p></div></div><div id=\"mailcontent\">"+thisjson.msg+"</div><div id=\"mailattachments\">Attachments</div><div id=\"attachINBOX\" style=\"position:absolute;left:81%;top:60%\"></div>";
			var attack = document.getElementById("attachINBOX")
			xml.onreadystatechange = function(){
				if(xml.readyState == 4 && xml.status == 200){
					attachments = xml.responseText;
					attachments = attachments.split(">");
					attack.innerHTML = attachments[0];
					br = document.createElement("br");
					attack.appendChild(br);
					if(attachments.length == 2){
						button = document.createElement("a");
						button2 = document.createElement("button")
						button2.innerHTML = "Download Attachment";
						button.href = conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/default/download/"+attachments[1];
						button.target = "_blank"
						button2.style = "position:absolute; top:200%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"
						button2.onmouseover= function(){button2.style = "position:absolute; top:200%; width:120px; background-color:#006699; transition: all 0.5 ease; border-radius: 133px;opacity:1;color:white;cursor:pointer"}
						button2.onmouseout = function(){button2.style = "position:absolute; top:200%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"}
						button.appendChild(button2)
						attack.appendChild(button);
					}
				}
			}
                }

		function makeactive(e){
			 activeelement.className = "tags";
			 activeelement = e;
			 e.className = "activemy";
			 
		}
		function putinto(el,p)
		{
			if( p == 1 )
				end = "";
			else
				end = "D";

				 var id = el.innerHTML;
         
                                        var listitem = document.createElement("LI");
                                        listitem.className = "rev";
                                        listitem.onclick = function() { document.getElementById("receivers"+end).removeChild(this); }
                                        var text = document.createTextNode(id);
                                        listitem.appendChild(text);
                                        ulist = document.getElementById("receivers"+end);
                                        ulist.appendChild(listitem);
                                        document.getElementById("recvrinput"+end).value = "";
                           
	
		}
		function animatemsg(txt)
		{
			var divid = document.getElementById("layer");
			divid.id = "layeractive";
			msgdiv = document.getElementById("message").children[0];
			msgdiv.innerHTML = txt;
			$("#message").fadeIn("slow");
			setTimeout(function(){ $("#message").fadeOut("fast");document.getElementById("layeractive").id = "layer";},1200);
		}
		
		function gettagcount()
		{
			var xml = new XMLHttpRequest();
			var name = document.getElementById("idofuser").innerHTML;
			xml.onreadystatechange = function()
			{
				if(xml.readyState == 4 && xml.status == 200)
				{
					newobj = JSON.parse(xml.responseText);
					document.getElementById("c1").children[0].innerHTML = newobj["Academics"]	
					document.getElementById("c2").children[0].innerHTML = newobj["Sports"]
					document.getElementById("c3").children[0].innerHTML = newobj["Events"]
					document.getElementById("c4").children[0].innerHTML = newobj["Cultural"]
					document.getElementById("c5").children[0].innerHTML = newobj["Urgent"]
					document.getElementById("c6").children[0].innerHTML = newobj["Lost/Found"]
					document.getElementById("c7").children[0].innerHTML = newobj["General"]
				}
			}
			xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/count?name="+name,true);
			xml.send();
		}
		
		document.getElementById("search").onkeyup = function (){
						var xml = new XMLHttpRequest();
			text = document.getElementById("search").value;
			name = document.getElementById("idofuser").innerHTML;
			var parameters = "value="+text+"&name="+name;
			xml.onreadystatechange = function()
			{
				if(xml.readyState == 4 && xml.status == 200)
				{
					obj = JSON.parse(xml.responseText);
					var p = document.getElementById("table_search");
					for(i=p.rows.length - 1;i>0;--i)
					{
						p.deleteRow(i);
					}
					searchjson = {}
					tempcount=1
					if (obj != "None")
					{
						var rows = ""
						//console.log(obj);
						
						for (i in obj)
						{
						//$.each(obj, function(){
							//if(obj.red == 1)
							//console.log(obj.red)
							//console.log(obj[i])
							if(obj[i].important)
							{
							if(obj[i].red)
							rows += "<tr><td class=\"readmails\" class='one'><input type='checkbox' id='radio_search'></td><td class=\"readmails\" onclick=\"opensearchdetails(this)\" class='two' id=\"search"+tempcount+"\">"+obj[i].sub+"</td><td class=\"readmails\"><img id=\"searchimp\" src=\"../static/images/star_highlight.png\" /></td><td class=\"readmails\" class='six'>"+obj[i].tag+"</td><td class=\"readmails\" class='three'>"+obj[i].send_id+"</td><td class=\"readmails\" class='four'>"+obj[i].sent_date+"</td><td class=\"readmails\" class='five'><img src='../static/images/paperclip.png' style='height:14px;width:28px;'/></td></tr>";
							else

							rows += "<tr><td class=\"unreadmails\" class='one'><input type='checkbox' id='radio_search'></td><td class=\"unreadmails\" onclick=\"opensearchdetails(this)\" class='two' id=\"search"+tempcount+"\">"+obj[i].sub+"</td><td class=\"unreadmails\" ><img id=\"searchimp\" src=\"../static/images/star_highlight.png\" /></td><td class=\"unreadmails\" class='six'>"+obj[i].tag+"</td><td class=\"unreadmails\" class='three'>"+obj[i].send_id+"</td><td class=\"unreadmails\" class='four'>"+obj[i].sent_date+"</td><td class=\"unreadmails\" class='five'><img src='../static/images/paperclip.png' style='height:14px;width:28px;'/></td></tr>";
							}
							else
							{

							if(obj[i].red)
							rows += "<tr><td class=\"readmails\" class='one'><input type='checkbox' id='radio_search'></td><td class=\"readmails\" onclick=\"opensearchdetails(this)\" class='two' id=\"search"+tempcount+"\">"+obj[i].sub+"</td><td class=\"readmails\"></td><td class=\"readmails\" class='six'>"+obj[i].tag+"</td><td class=\"readmails\" class='three'>"+obj[i].send_id+"</td><td class=\"readmails\" class='four'>"+obj[i].sent_date+"</td><td class=\"readmails\" class='five'><img src='../static/images/paperclip.png' style='height:14px;width:28px;'/></td></tr>";
							else

							rows += "<tr><td class=\"unreadmails\" class='one'><input type='checkbox' id='radio_search'></td><td class=\"unreadmails\" onclick=\"opensearchdetails(this)\" class='two' id=\"search"+tempcount+"\">"+obj[i].sub+"</td><td class=\"unreadmails\" ></td><td class=\"unreadmails\" class='six'>"+obj[i].tag+"</td><td class=\"unreadmails\" class='three'>"+obj[i].send_id+"</td><td class=\"unreadmails\" class='four'>"+obj[i].sent_date+"</td><td class=\"unreadmails\" class='five'><img src='../static/images/paperclip.png' style='height:14px;width:28px;'/></td></tr>";	
							}
							
							searchjson[tempcount] = obj[i];
							
							tempcount+=1;
						}
						$(rows).appendTo("#table_search");
						$("#searchbox").show();
						$("#bigtable_"+flag).hide();
						divname =  sa.id.slice(0,-2);
						$("#"+divname+"er").hide();
					}
					else
					{
						$("#searchbox").hide();
						divname =  sa.id.slice(0,-2);
						if( divname == "inbox" )
						{
							$("#inboxer").show();
							whatisopened = 0;
							$("#bigtable_"+flag).show();
						}
						else
							$("#"+divname+"er").show();
						
					}
				}
			}
			xml.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/search?"+parameters, true);
			xml.send();
		}
		
		
		function getuser(){
                                var xhr = new XMLHttpRequest();
                                xhr.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/getuser",true);
                                xhr.send();
        
                                xhr.onreadystatechange = function(){
                                        if( xhr.readyState == 4 && xhr.status == 200 )
                                        {                
							var k = xhr.responseText;
							gettagcount();	
					}
                                
				}
                        
                        }
		function sendtodiv(e,p)
		{
			if( p == 1 )
				end = "";
			else
				end = "D";
			if ( e.keyCode == 13 )
			{	
				id = document.getElementById("suggestions"+end).children[0].innerHTML;
				if ( id != "" )
				{
					var listitem = document.createElement("LI");
					listitem.className = "rev";
					listitem.onclick = function() { document.getElementById("receivers"+end).removeChild(this); }
					var text = document.createTextNode(id);
					listitem.appendChild(text);
					ulist = document.getElementById("receivers"+end);
					ulist.appendChild(listitem);
					document.getElementById("recvrinput"+end).value = "";
				}
			}
		}
		function auto(e,p)
		{
				if( p == 1 )
					end = "";
				else
					end = "D";
				var xhr = new XMLHttpRequest();
				xhr.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/getid?id="+document.getElementById("recvrinput"+end).value,true);
				xhr.send()
				
				xhr.onreadystatechange = function()
				{
					if( xhr.readyState == 4 && xhr.status == 200 )
					{
						response = xhr.responseText;
						k = response.split(" ");
						div = document.getElementById("suggestions"+end);
						j = div.children.length;
						for( k = j-1 ; k>=0; k-- )
							div.removeChild(div.children[k]);
						
						if( document.getElementById("recvrinput"+end).value != "" )
						{
							if( response.length != 0 )
							{	
									k = response.split(" ");
									for(i=0;i<k.length;i++)
									{
										var sug = document.createElement("P");
										var txt = document.createTextNode(k[i]);
										sug.appendChild(txt);
										sug.onclick = function(){ putinto(this,p);  document.getElementById("suggestions"+end).style.visibility = "hidden"; };
										div.appendChild(sug);
										div.style.visibility="visible";
									}
							}
						}
						else
							div.style.visibility = "hidden";
							
					}
				}
		}
		function logout(){
                                window.location.href = conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/loginmy?logout=1"
                        }
		function showdraftmessage(e)
		{
				  k = e.id;
                               	  k = k.slice(3,k.length);
				  document.getElementById("draftdelete").style.display = "none";
	
					 document.getElementById("subD").value = ""; 
                                        document.getElementById("msgD").value = "";
                                        doko = document.getElementById("recvrD");
                                        doko.removeChild(doko.children[0]);
                                        koko = document.createElement("UL");
                                        koko.id = "receiversD";
                                        doko.appendChild(koko);
				  
				  for ( i=1 ; ; i++ )
                                  {
                                         if( typeof draftlist[i] != "undefined" )
                                         {
						if ( i == k )
						{
                                                        p = draftlist[i]["receivers"];
							p = p.split(" ");
							len = p.length - 1;	
						       for( toko= 1; toko <= len ; toko ++ )
						       {
									  var listitem = document.createElement("LI");
                                 				          listitem.className = "rev";
										id = p[toko];
                                       						 listitem.onclick = function() { document.getElementById("receiversD").removeChild(this); }
                                     						   var text = document.createTextNode(id);
                                 					       listitem.appendChild(text);
                                    					    ulist = document.getElementById("receiversD");
                                 					       ulist.appendChild(listitem);
                                   					     document.getElementById("recvrinputD").value = "";
							}
                                
                  			              var tagel = document.getElementsByTagName("select");
                            			    var tag = tagel[0].options[tagel[0].selectedIndex].innerHTML;
                                 
							document.getElementById("closeD").style.display = "block";
							document.getElementById("senderD").style.display = "block";
							draftsubject = draftlist[i]["subject"];
							draftmessage = draftlist[i]["mail_message"];
							draftreceivers = draftlist[i]["receivers"];
							document.getElementById("composerD").style.display = "block";
							document.getElementById("subD").value = draftlist[i]["subject"];
                                                        document.getElementById("msgD").value = draftlist[i]["mail_message"];

							document.getElementById("draftser").style.display = "none";   
						}
	
					}
					else
						break;
		      		}
		}
		function senddraftmail(){

				document.getElementById("draftdelete").style.display = "none";
				var xhr = new XMLHttpRequest();
                                var xp = new XMLHttpRequest();
                                reclist = "";
                                var el = document.getElementById("receiversD");
                                list = el.children;
                                for( k = 0 ; k < list.length ; k++ )
                                        reclist = reclist+" "+list[k].innerHTML;
                                
                                details = {}
                                details["receivers"] = reclist;
                                
                                var tagel = document.getElementsByTagName("select");
                                var tag = tagel[1].options[tagel[1].selectedIndex].innerHTML;
                                
                                details["tag"] = tag;
				var sub = document.getElementById("subD").value;
                                details["sub"] = sub;
                                var msg = document.getElementById("msgD").value;
                                details["msg"] = msg;
                                var send_id = document.getElementById("idofuser").innerHTML;
                                details["send_id"] = send_id;
                                var sender_name = document.getElementById("user").innerHTML;
                                details["sender_name"] = sender_name;
               			draftdetails = {};		
				draftdetails["send_id"] = send_id;
				draftdetails["sender_name"] = sender_name;
				draftdetails["sub"] = draftsubject;
				draftdetails["message"] = draftmessage;
				draftdetails["receivers"] = draftreceivers;

                                if( tag != "" )
                                {
	
                                        xhr.open("POST",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/send",true);
                                        xp.open("POST",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/checkdrafts",true);
                                        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                                        xp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                                        xhr.send(JSON.stringify(details));
                                        xp.send(JSON.stringify(draftdetails));

                                        xhr.onreadystatechange = function(){
                                                
                                                if( xhr.readyState == 4 && xhr.status == 200 )
                                                {
                                                        animatemsg(xhr.responseText);
                                                	document.getElementById("composerD").style.display = "none";
                                                        document.getElementById("draftser").style.display = "block";
							document.getElementById("draftdelete").style.display = "block";   
							refreshdraftmails();
							localStorage.clear();
							
						}
                                        }
                                        xp.onreadystatechange = function(){
                                                if ( xp.readyState == 4 && xp.status == 200 )
                                                        console.log(xp.responseText);
                                        }
                                }
                                else
                                {
                                        if( id == "" )
                                                animatemsg("Receivers ID field can not be left empty");
                                }
					
		}
		function closedraftmail()
		{
				  var xhr = new XMLHttpRequest();
                 		reclist = "";
                                var el = document.getElementById("receiversD");
                                list = el.children;
                                for( k = 0 ; k < list.length ; k++ )
                                        reclist = reclist+" "+list[k].innerHTML;
                                
                                details = {};
				t = reclist.split(" ");
                                if( t.length != 1 )
                                {
                                       details["receivers"] = reclist;
                                
                                       var tagel = document.getElementsByTagName("select");
                                       var tag = tagel[0].options[tagel[0].selectedIndex].innerHTML;
                                
                                        details["tag"] = tag;
                                        var sub = document.getElementById("subD").value;
                                        details["sub"] = sub;
                                        var msg = document.getElementById("msgD").value;
                                        details["msg"] = msg;
                                        if( sub != "" || msg != "" )
                                        {
                                                     var send_id = document.getElementById("idofuser").innerHTML;
                                                             details["send_id"] = send_id;
                                                     var sender_name = document.getElementById("user").innerHTML;
                                                     details["sender_name"] = sender_name;
       
                                                     xhr.open("POST",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/drafts",true);
                                                     xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                                           	     xhr.send(JSON.stringify(details));
                                              	//	console.log(details);
						       xhr.onreadystatechange = function(){
                                                
                                                                     if( xhr.readyState == 4 && xhr.status == 200 )
                                                                     {
										if ( xhr.responseText != "already" )
										{
											animatemsg("Mail saved to Drafts");
											refreshdraftmails();
                                                      				}
                                        			     }
                        				}
                                	}
				}
				document.getElementById("closeD").style.display = "none";
                                document.getElementById("senderD").style.display = "none";
				document.getElementById("composerD").style.display = "none";
                                document.getElementById("draftser").style.display = "block";   
				document.getElementById("draftdelete").style.display = "block";
		}
		function refreshdraftmails()
		{
					draftlist = {}; 
                                        var xp = new XMLHttpRequest();
                                
                                        xp.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/getdrafts?email="+document.getElementById("idofuser").innerHTML,true);
                                        xp.send();
                                
                                        l = document.getElementById("draftser");
                                        l.removeChild(l.children[0]);
                                        table = document.createElement("TABLE");
                                        table.id = "drafttable";
                                        table.className = "table";
                                        l.appendChild(table);
                                        
					 $("#drafttable").append("<tr><td class='one' id='i1'></td><td class='two' id='i2'>Subject</td><td class='three' id='i3'>Receivers</td><td class='four' id='i4'>Date</td></tr>");


                                        xp.onreadystatechange = function()
                                        {
                                                if( xp.readyState == 4 && xp.status == 200 )
                                                {
                                                        draftlist = JSON.parse(xp.responseText);
							console.log(draftlist);
                                                        for ( i=1 ; ; i++ )
                                                        {
                                                                if( typeof draftlist[i] != "undefined" )
                                                                {
                                                                        p = draftlist[i]["receivers"].split(" ");
    									k = p.length - 1;
									 
									$("#drafttable").append("<tr><td class='one'><input onclick='selectdelmails(this,2)' type='checkbox' name='radiog_lite' id='radio' class='css-checkbox'></td><td class='two' onclick='showdraftmessage(this)' id='msg"+i+"'><label class='css-label'>"+draftlist[i]['subject']+"</label></td><td class='three'>"+k+"</td><td class='four'>"+draftlist[i]['made_date']+"</td></tr>");
                                                                
       	                                                        }
                                                                else if( typeof draftlist[i] == "undefined" )
                                                                       break;

                                                        }
						}
					}
		}
		function refreshsentmails()
		{
				console.log(sa);
				var xhr = new XMLHttpRequest();
                                xhr.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/sentmails?email="+document.getElementById("idofuser").innerHTML,true);
                                xhr.send();
                        $("#searchdiv").hide();
                                l = document.getElementById("senter");
                                l.removeChild(l.children[0]);
                                table = document.createElement("TABLE");
                                table.id = "senttable";
                                table.className = "table";
                                l.appendChild(table);
                                        
                                $("#senttable").append("<tr><td class='one' id='i1'></td><td class='two' id='i2'>Subject</td><td class='three' id='i3'>Receivers</td><td class='four' id='i4'>Date</td><td class='five' id='i5'><img src='../static/images/attmain.png' height='14px' width='20px'/></td></tr>");

                                xhr.onreadystatechange = function(){
                                        
                                                if( xhr.readyState == 4 && xhr.status == 200 )
                                                {
                                                        completelist = JSON.parse(xhr.responseText);
							console.log(completelist);
                                                        for( i in completelist )
                                                        {
                                                                k = completelist[i]["receivers"].split(" ");
                                                                console.log(k);
								if ( completelist[i]["attachment"] )
                                                                	$("#senttable").append("<tr><td class='one'><input onclick='selectdelmails(this,1)' type='checkbox' name='radiog_lite' id='radio' class='css-checkbox'></td><td class='two' onclick='showsentmessage(this)' id='sent"+i+"'><label class='css-label'>"+completelist[i]["subject"]+"</label></td><td class='three'>"+(k.length-1)+"</td><td class='four'>"+completelist[i]["sent_date"]+"</td><td class='five'><img src='../static/images/paperclip.png' height='31px' width='31px'></img></tr>");
                                                        	else
									$("#senttable").append("<tr><td class='one'><input onclick='selectdelmails(this,1)' type='checkbox' name='radiog_lite' id='radio' class='css-checkbox'></td><td class='two' onclick='showsentmessage(this)' id='sent"+i+"'><label class='css-label'>"+completelist[i]["subject"]+"</label></td><td class='three'>"+(k.length-1)+"</td><td class='four'>"+completelist[i]["sent_date"]+"</td><td class='five'></td></tr>");

							}
                                                }       
				}
				gettagcount();
		}
		function deletethesemails()
		{
			deleter = {};
			divname =  sa.id.slice(0,-2);
			if( divname == "drafts" )
			{
				varname = deletedraftlist;
				whichlist = draftlist;
				slicewhat = 3;
			}
			else if( divname == "sent")
			{	
				varname = deletesentlist;
				whichlist = completelist;
				slicewhat = 4;
			}
			for(i=0 ; i< varname.length ; i++ )
			{
				idofmsg = varname[i].slice(slicewhat,varname[i].length);
				deleter[i] = {};
				for( j in whichlist[idofmsg] ){
					if(!( j == "attachment" || j == "id" || j == "unique_field"))
						deleter[i][j] = whichlist[idofmsg][j];
				}
			}
			var xhr = new XMLHttpRequest();
			xhr.open("POST",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/delete"+divname,true);
			xhr.setRequestHeader("Content-Type","application/json;charset=UTF-8");
			xhr.send(JSON.stringify(deleter));	
			xhr.onreadystatechange = function()
			{
				if( xhr.readyState == 4 && xhr.status == 200 )
				{
					animatemsg(xhr.responseText);
					if( divname == "sent" )
					{
						refreshsentmails();
						deletesentlist = [];
					}
					else if( divname == "drafts" )
					{	refreshdraftmails();
						deletedraftlist = [];
					}
				}
			}
		}
		function selectdelmails(e,pizza)
		{
			
			id = e.parentNode.parentNode.children[1].id;
			if ( e.checked == true )
			{
				e.parentNode.className="selected";
				if( pizza == 1 )
					deletesentlist.push(id);
				else if(pizza == 2 )
					deletedraftlist.push(id);			
			}
			else
			{
				k = [];
				if( pizza == 1 )
				{
					e.parentNode.className = "original";
					deletesentlist.filter(function(idd) { if( idd != id ) { k.push(idd) } });
					deletedraftlist = k;
				}
				else if(pizza == 2 )
				{
					e.parentNode.className = "original";
					deletedraftlist.filter(function(idd) { if( idd != id ) { k.push(idd) } });
					deletesentlist = k;
				}
			}
		}
		function showsentmessage(e)
		{

			popop = e.id.slice(4,e.id.length);
			
			document.getElementById("senter").style.display = "none";
			document.getElementById("Sentmaildetails").style.display = "block";
			mail = completelist[popop];
			var xml = XMLHttpRequest();
			xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/attachment?id="+mail["id"], true);
			xml.send();
			 doko = document.getElementById("Sentrecvr");
                         doko.removeChild(doko.children[0]);
                         koko = document.createElement("UL");
                         koko.id = "Sentrecvrlist";
                         doko.appendChild(koko);
			
			k = completelist[popop]["receivers"].split(" ");
			for(i=0;i<k.length;i++)
			{
				if( k[i] != "" )
				{
				var listitem = document.createElement("LI");
       		                 listitem.className = "rev";
                 	       var text = document.createTextNode(k[i]);
                	        listitem.appendChild(text);
               		         ulist = document.getElementById("Sentrecvrlist");
                        	ulist.appendChild(listitem);
				}
			}
			
			
			document.getElementById("Senttag").children[0].innerHTML = mail["tag"];
			document.getElementById("Sentsubjectdetails").children[0].innerHTML = mail["subject"];
                        document.getElementById("Sentmailcontent").innerHTML = mail["mail_message"];
			var attack = document.getElementById("attachA")
			xml.onreadystatechange = function(){
				if(xml.readyState == 4 && xml.status == 200){
					attachments = xml.responseText;
					attachments = attachments.split(">");
					attack.innerHTML = attachments[0];
					br = document.createElement("br");
					attack.appendChild(br);
					if(attachments.length == 2){
						button = document.createElement("a");
						button2 = document.createElement("button")
						button2.innerHTML = "Download Attachment";
						button.href = conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/default/download/"+attachments[1];
						button.target = "_blank"
						button2.style = "position:absolute; top:120%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"
						button2.onmouseover= function(){button2.style = "position:absolute; top:120%; width:120px; background-color:#006699; transition: all 0.5 ease; border-radius: 133px;opacity:1;color:white;cursor:pointer"}
						button2.onmouseout = function(){button2.style = "position:absolute; top:120%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"}
						button.appendChild(button2)
						attack.appendChild(button);
					}
				}
			}	
		}
		function closesentmail()
		{
			document.getElementById("senter").style.display = "block";
                        document.getElementById("sentview").style.display = "none";		
		}
		function showtrashmessage(e){
			
				l = e.id;
				idd = l.slice(5,l.length);
				
				xml = new XMLHttpRequest();
				xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/attachment2?id="+trashlist[idd]["id"], true);
				xml.send();
	
				document.getElementById("trasher").style.display = "none";
				maindiv = document.getElementById("trashdetails");
           	                maindiv.style.display = "block";
                        	document.getElementById("TrashTag").innerHTML = trashlist[idd]["tag"];
				t = document.getElementById("Trashfrom");
				maindiv.children[0].removeChild(t);
				divi = document.createElement("DIV");
				divi.id = "Trashfrom"; 				
				maindiv.appendChild(divi);
				console.log(maindiv.children);				
				p = document.createElement("P");
				txt = document.createTextNode("From:"+trashlist[idd]["send_id"]);
				p.appendChild(txt);
				divi = document.getElementById("Trashfrom");
				divi.appendChild(p);
				p = document.createElement("P");
                                txt = document.createTextNode("Time:"+trashlist[idd]["sent_time"]);
                                p.appendChild(txt);
				divi.appendChild(p);
				p = document.createElement("P");
                                txt = document.createTextNode("Date:"+trashlist[idd]["sent_date"]);
                                p.appendChild(txt);
				divi.appendChild(p);
				
                       		document.getElementById("Trashsubject").innerHTML = trashlist[idd]["sub"];
                       	        document.getElementById("trashmailcontent").innerHTML = trashlist[idd]["msg"];

				var attack = document.getElementById("attachT");
                                xml.onreadystatechange = function(){
                                if(xml.readyState == 4 && xml.status == 200){
                                        attachments = xml.responseText;
                                        attachments = attachments.split(">");
                                        attack.innerHTML = attachments[0];
                                        br = document.createElement("br");
                                        attack.appendChild(br);
                                        if(attachments.length == 2){
                                                button = document.createElement("a");
                                                button2 = document.createElement("button")
                                                button2.innerHTML = "Download Attachment";
                                                button.href = conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/default/download/"+attachments[1];
                                                button.target = "_blank"
                                                button2.style = "position:absolute; top:120%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"
                                                button2.onmouseover= function(){button2.style = "position:absolute; top:120%; width:120px; background-color:#006699; transition: all 0.5 ease; border-radius: 133px;opacity:1;color:white;cursor:pointer"}
                                                button2.onmouseout = function(){button2.style = "position:absolute; top:120%;color:white;background-color:#006699;width: 120px; opacity: 0.4; transition: all 0.5s ease; border-radius: 133px;"}
                                                button.appendChild(button2)
                                                attack.appendChild(button);
                                        }
                                }
                        }       

		
		
		}
		function refreshtrashmails(){
		
				var idofuser = document.getElementById("idofuser").innerHTML;
				var xhr = new XMLHttpRequest();
				xhr.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/showTrash?id="+idofuser,true);
				xhr.send();
				
				var div=document.getElementById("trasher");
                                l = document.getElementById("trashtable");
				div.removeChild(l);
                                var table=document.createElement("TABLE");
                                table.className = "table";
                                table.id = "trashtable";
                                div.appendChild(table);
                                $("#trashtable").append("<tr><td class=\"one\" id=\"i1\"></td><td class=\"two\" id=\"i2\">Subject</td><td class=\"three\" id=\"i3\">From</td><td class=\"four\" id=\"i4\">Date</td><td class=\"five\" id=\"i5\"><img src=\"../static/images/attmain.png\" style=\"height=14px;width:20px;\"/></td></tr>");
	
				xhr.onreadystatechange = function(){
						if( xhr.readyState == 4 && xhr.status == 200 )
						{
							          trashlist = JSON.parse(xhr.responseText);
								  console.log(trashlist)
								  for( i in trashlist )
								  {
									if( trashlist[i]["Link"] != "None" )
									{
									$("#trashtable").append("<tr><td class='one'></td><td class='two' onclick='showtrashmessage(this)' id='trash"+i+"'><label class='css-label'>"+trashlist[i]["sub"]+"</label></td><td class='three'>"+trashlist[i]["send_id"]+"</td><td class='four'>"+trashlist[i]["sent_date"]+"</td><td class='five'><img src='../static/images/paperclip.png' height='31px' width='31px'></img></tr>");
									 }
									 else
										$("#trashtable").append("<tr><td class='one'></td><td class='two' onclick='showtrashmessage(this)' id='trash"+i+"'><label class='css-label'>"+trashlist[i]["sub"]+"</label></td><td class='three'>"+trashlist[i]["send_id"]+"</td><td class='four'>"+trashlist[i]["sent_date"]+"</td><td class='five'></td></tr>");
								  }
						}
				}
		}
		function openinbox(e){
				
				$("#draftdelete").hide();	
				$("#dlt").hide();
				$("#mailicons").fadeIn("fast");			        
				sa.className = "down";
                                divname =  sa.id.slice(0,-2);
				eko = document.getElementById("inboxme");
				eko.className = "sideactive";
				if ( divname == "compose" )
                                {
                                         $("#close").fadeOut("fast");
                                                 $("#sender").fadeOut("fast"); 
                                                 $("#composer").fadeOut("fast");

                                }
                             	else if( divname == "sent" )
				{
                                      document.getElementById("senter").style.display = "none";     
					document.getElementById("Sentmaildetails").style.display = "none";
				}else if(divname == "inbox" )
				{	
				     document.getElementById("inboxer").style.display = "none";
				     document.getElementById("maildetails").style.display = "none";
				}	
				else if(divname == "trash" )
				{
						$("#trasher").hide();
						document.getElementById("trashdetails").style.display = "none"; 		
				}
				else if( divname == "drafts" )
                                {      $("#draftdelete").fadeOut("fast");
				      document.getElementById("draftser").style.display = "none";
						document.getElementById("composerD").style.display = "none";
				}
				sa = eko;
			$("#imgforward").hide();
			$("#imgreply").hide();
			$("#searchdiv").show();
			 $("#inboxer").show();
			 whatisopened = 0
			 document.getElementById("search").value = "";
                         details=document.getElementById("maildetails")
                         details.style.display="none";
                         activeelement.className = "tags";
                         activeelement = e;
                         e.className = "activemy";
                         taginboxname = e.id.slice(4,e.id.length);
			 flag = taginboxname;
		              			var div=document.getElementById("div"+taginboxname);
                                                div.removeChild(document.getElementById("bigtable_"+taginboxname));
                                                var table=document.createElement("TABLE");
						table.className = "table";
                                                table.id="bigtable_"+taginboxname;
                                                div.appendChild(table);
                                                appendfirstrow(taginboxname);
                                                reloadpage();
                                                for(i=0;i<globallist.length;i++)
                                                {
                                                        if( globallist[i] != taginboxname )
                                                                $("#bigtable_"+globallist[i]).hide();
                                                }
						$("#searchbox").hide();
                                                $("#bigtable_"+taginboxname).show();

                }
		function appendtotable(tag, tmpobj, count, flag, imp)
{
			
			addline = "";
			if( tmpobj.Link != "None" )
			{
				addline = "<img src='../static/images/paperclip.png' style='height=14px;width:22px'>";
			}
	if(imp)
	{
		
		if(flag)
{
			$("#bigtable_"+tag).append("<tr><td  class=\"readmails\" class=\"one\"><input type=\"checkbox\" id=\"radio"+tag+count+"\"/></td><td class=\"readmails\" class=\"two\" id=\"subject"+tag+count+"\" onclick=\"opendetails(this)\"><label>"+tmpobj.sub+"</label></td><td class=\"readmails\"  class=\"three\">"+tmpobj.send_id+"</td><td class=\"readmails\" class=\"four\"><img style=\"height=14px;width:20px;\" src=\"../static/images/star_highlight.png\"></td><td class=\"readmails\" class=\"five\">"+tmpobj.sent_date+"</td><td class=\"readmails\" class=\"six\">"+addline+"</td><td style='display:none'>"+tmpobj.id+"</td></tr>");
}else
{			$("#bigtable_"+tag).append("<tr><td class=\"unreadmails\" class=\"one\"><input type=\"checkbox\" id=\"radio"+tag+count+"\"/></td><td class=\"unreadmails\" class=\"two\" id=\"subject"+tag+count+"\"  onclick=\"opendetails(this)\"><label>"+tmpobj.sub+"</label></td><td class=\"unreadmails\" class=\"three\">"+tmpobj.send_id+"</td><td class=\"unreadmails\" class=\"four\"><img style=\"height=14px;width:20px;\" src=\"../static/images/star_highlight.png\"></td><td class=\"unreadmails\" class=\"five\">"+tmpobj.sent_date+"</td><td class=\"unreadmails\" class=\"six\">"+addline+"</td><td style='display:none'>"+tmpobj.id+"</td></tr>");
}	
}

	else
	{
		if(flag)
{			$("#bigtable_"+tag).append("<tr><td  class=\"readmails\" class=\"one\"><input type=\"checkbox\" id=\"radio"+tag+count+"\"/></td><td class=\"readmails\" class=\"two\" id=\"subject"+tag+count+"\" onclick=\"opendetails(this)\"><label>"+tmpobj.sub+"</label></td><td class=\"readmails\"  class=\"three\">"+tmpobj.send_id+"</td><td class=\"readmails\" class=\"four\"></td><td class=\"readmails\" class=\"five\">"+tmpobj.sent_date+"</td><td class=\"readmails\" class=\"six\">"+addline+"</td><td style='display:none'>"+tmpobj.id+"</td></tr>");
}
		else
{			$("#bigtable_"+tag).append("<tr><td class=\"unreadmails\" class=\"one\"><input type=\"checkbox\" id=\"radio"+tag+count+"\"/></td><td class=\"unreadmails\" class=\"two\" id=\"subject"+tag+count+"\"  onclick=\"opendetails(this)\"><label>"+tmpobj.sub+"</label></td><td class=\"unreadmails\" class=\"three\">"+tmpobj.send_id+"</td><td class=\"unreadmails\" class=\"four\"></td><td class=\"unreadmails\" class=\"five\">"+tmpobj.sent_date+"</td><td class=\"unreadmails\" class=\"six\">"+addline+"</td><td style='display:none'>"+tmpobj.id+"</td></tr>");
}
	}
}

function appendfirstrow(tag)
{
	$("#bigtable_"+tag).append("<tr><td class=\"one\" id=\"i1\"></td><td class=\"two\" id=\"i2\">Subject</td><td class=\"three\" id=\"i3\">From</td><td id=\"i4\" class=\"four\"><img src='../static/images/star_selected.png' style='height=14px;width:20px;'></td><td class=\"five\" id=\"i5\">Date</td><td class=\"six\" id=\"i6\"><img src=\"../static/images/attmain.png\" style=\"height=14px;width:20px;\"/></td></tr>");


}

			function reloadpage()
{
	gettagcount();
	$("#maildetails").hide();
	var xhr = new XMLHttpRequest();
	var l = document.getElementById("idofuser").innerHTML;
	xhr.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/show?id="+l,true);
	xhr.send();
	$("#inboxer").show();
	whatisopened = 0;
	xhr.onreadystatechange = function()
	{
		if( xhr.readyState == 4 && xhr.status == 200 )
		{       
			Academics_count=1;
			Sports_count=1;
			Events_count=1;
			Cultural_count=1;
			Urgent_count=1;
			LostFound_count=1;
			General_count=1;
			other_count=1;

			obj=JSON.parse(xhr.responseText);
			console.log(obj);
			jQuery.each(obj, function(keyi, valuei) {
					tmpobj = valuei;
					jQuery.each(tmpobj,function(keyj,valuej){
						if(keyj=="tag"&&valuej=="Academics")
						{
							Academics[Academics_count]=valuei;
							appendtotable("Academics", tmpobj,Academics_count, tmpobj.red, tmpobj.important);    
							Academics_count += 1;
						}
						else if(keyj=="tag"&&valuej=="Sports"){
							Sports[Sports_count]=valuei;
							appendtotable("Sports", tmpobj, Sports_count, tmpobj.red, tmpobj.important);
							Sports_count += 1;
						}
						else if(keyj=="tag"&&valuej=="Events"){
							Events[Events_count]=valuei;
							appendtotable("Events", tmpobj, Events_count, tmpobj.red, tmpobj.important);
							Events_count += 1;
						}

						else if(keyj=="tag"&&valuej=="Cultural"){
							Cultural[Cultural_count]=valuei;
							appendtotable("Cultural", tmpobj, Cultural_count, tmpobj.red, tmpobj.important);
							Cultural_count += 1;
						}
						else if (keyj=="tag"&&valuej=="Urgent"){
							Urgent[Urgent_count]=valuei;
							appendtotable("Urgent", tmpobj, Urgent_count, tmpobj.red, tmpobj.important);
							Urgent_count += 1;
						}
						else if(keyj=="tag"&&valuej=="Lost/Found"){
							LostFound[LostFound_count]=valuei;
							appendtotable("LostFound", tmpobj, LostFound_count, tmpobj.red, tmpobj.important);
							LostFound_count += 1;
						}
						else if(keyj=="tag"&&valuej=="General"){
							General[General_count]=valuei;
							appendtotable("General", tmpobj, General_count, tmpobj.red, tmpobj.important);
							General_count += 1;
						}


					});

			});
		}
	}

}

			
			function markimpmails(){
				var f;
				var tab = document.getElementById("tabs").children;
				for(f=0;f<tab.length;f++){
					if(tab[f].className == "activemy"){
						break;
					}
				}
				var count = "";
				var fields = document.getElementById("inboxer").children[f].children[0].children[0].children;
				for(f=1;f<fields.length;f++){
					if(fields[f].children[0].children[0].checked){
						count += (fields[f].children[6].innerHTML)+">";
					}	
				}
				console.log(count);
				var xml = new XMLHttpRequest();
				xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/importantInbox?count="+count, true);
				xml.send();
				xml.onreadystatechange = function(){
					if(xml.readyState == 4 && xml.status == 200){
						
					}
				}
	
			}
			function markunreadmails(){
				var f;
				var tab = document.getElementById("tabs").children;
				for(f=0;f<tab.length;f++){
					if(tab[f].className == "activemy"){
						break;
					}
				}
				var count = "";
				var fields = document.getElementById("inboxer").children[f].children[0].children[0].children;
				for(f=1;f<fields.length;f++){
					if(fields[f].children[0].children[0].checked){
						count += (fields[f].children[6].innerHTML)+">";
					}	
				}
				console.log(count);
				var xml = new XMLHttpRequest();
				xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/unreadInbox?count="+count, true);
				xml.send();
				xml.onreadystatechange = function(){
					if(xml.readyState == 4 && xml.status == 200){
						
					}
				}
	
			}
    
			function markreadmails(){
				var f;
				var tab = document.getElementById("tabs").children;
				for(f=0;f<tab.length;f++){
					if(tab[f].className == "activemy"){
						break;
					}
				}
				var count = "";
				var fields = document.getElementById("inboxer").children[f].children[0].children[0].children;
				for(f=1;f<fields.length;f++){
					if(fields[f].children[0].children[0].checked){
						count += (fields[f].children[6].innerHTML)+">";
					}	
				}
				console.log(count);
				var xml = new XMLHttpRequest();
				xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/readInbox?count="+count, true);
				xml.send();
				xml.onreadystatechange = function(){
					if(xml.readyState == 4 && xml.status == 200){
						
					}
				}
	
			}
                 
			function inboxDelete(){
				var f;
				var tab = document.getElementById("tabs").children;
				for(f=0;f<tab.length;f++){
					if(tab[f].className == "activemy"){
						break;
					}
				}
				var count = "";
				var fields = document.getElementById("inboxer").children[f].children[0].children[0].children;
				for(f=1;f<fields.length;f++){
					if(fields[f].children[0].children[0].checked){
						count += (fields[f].children[6].innerHTML)+">";
					}	
				}
				console.log(count);
				var xml = new XMLHttpRequest();
				xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/deleteInbox?count="+count, true);
				xml.send();
				xml.onreadystatechange = function(){
					if(xml.readyState == 4 && xml.status == 200){
						
					}
				}
	
			}
		$(document).ready(function()
		{
			sa = document.getElementById("inboxme");	
			$("#searchbox").hide();
			$("#imgreply").hide();
			$("#imgforward").hide();
			$("#bigtable_Academics").show();
                        $("#bigtable_Sports").hide();
                        $("#bigtable_Events").hide();
                        $("#bigtable_Cultural").hide();
                        $("#bigtable_Urgent").hide();
                        $("#bigtable_LostFound").hide();
                        $("#bigtable_General").hide();
                        $("#bigtable_SentMails").hide();
                        $("#maildetails").hide();
                        reloadpage();
	 		showinbox();
			attach();	
			function savetodrafts(){
	
				var xhr = new XMLHttpRequest();
                                var el = document.getElementById("receivers");
                                list = el.children;
				reclist = "";
                                for( k = 0 ; k < list.length ; k++ )
                                        reclist = reclist+" "+list[k].innerHTML;
                                
                         	details = {};
				list = reclist.split(" ");
				if( list.length != 1 )
				{
                         	       details["receivers"] = reclist;
                                
                       	               var tagel = document.getElementsByTagName("select");
                       	               var tag = tagel[0].options[tagel[0].selectedIndex].innerHTML;
                                
                        	        details["tag"] = tag;
                                	var sub = document.getElementById("sub").value;
                 	                details["sub"] = sub;
                       		        var msg = document.getElementById("msg").value;
                 	                details["msg"] = msg;
					if( sub != "" || msg != "" )
					{
           	        	                     var send_id = document.getElementById("idofuser").innerHTML;
                	    	        	             details["send_id"] = send_id;
                                    		     var sender_name = document.getElementById("user").innerHTML;
                     	         	             details["sender_name"] = sender_name;
						     	
						     xhr.open("POST",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/drafts",true);
                              		             xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                               		      	     xhr.send(JSON.stringify(details));
              		                             xhr.onreadystatechange = function(){
                                                
                           			                     if( xhr.readyState == 4 && xhr.status == 200 )
                                            			     	       animatemsg(xhr.responseText);
                                                      }
                                        }
			
				}
			}
				
			$("#composeme").click(function(){
				$("#searchdiv").hide();
				$("#mailicons").fadeOut("fast");
				$("#dlt").hide();
				 localStorage.clear();	
				 document.getElementById("sub").value = ""; 
                                        document.getElementById("msg").value = "";
                                        d = document.getElementById("recvr");
                                        d.removeChild(d.children[0]);
                                        k = document.createElement("UL");
                                        k.id = "receivers";
                                        d.appendChild(k);

				sa.className = "down";
                                e = document.getElementById("composeme");
                                divname =  sa.id.slice(0,-2);
				if ( divname == "compose" )
                                {
					 $("#close").fadeOut("fast");
                                                 $("#sender").fadeOut("fast"); 
                                                 $("#composer").fadeOut("fast");
	
                                }
                        	else if( divname == "drafts" )
                                {      $("#draftdelete").fadeOut("fast");
				      document.getElementById("draftser").style.display = "none";
						document.getElementById("composerD").style.display = "none";
				}
      				else if( divname == "sent" )
				{
					$("#draftdelete").fadeOut("fast");
				      document.getElementById("senter").style.display = "none";     
					document.getElementById("Sentmaildetails").style.display = "none";
				}else if(divname == "inbox")
				 {
					document.getElementById("maildetails").style.display = "none";     
					document.getElementById("inboxer").style.display = "none";
				}
 				else if( divname == "trash" )
				{
				document.getElementById("trashdetails").style.display = "none"; 
				$("#trasher").hide();
				}
				
				$("#"+divname+"er").fadeOut("fast");		
                                e.className = "sideactive";
				sa = e;
				 $("#close").fadeIn("slow");
                                 $("#sender").fadeIn("slow"); 
                                 $("#composer").fadeIn("slow");



				});
			$("#close").click(function(){
				
					savetodrafts();
					sa.className = "down";
                                        e = document.getElementById("inboxme");
                                        $("#close").fadeOut("fast");
                                        $("#sender").fadeOut("fast"); 
                                        $("#composer").fadeOut("fast");
                                        e.className = "sideactive";
                                        $("#inboxer").fadeIn("slow");
                                        whatisopened = 0;
                                        sa = e;	
					$("#composer").fadeOut("fast");
			});
			$("#sender").click(function(){
                                var xhr = new XMLHttpRequest();
				$("#dlt").hide();
                            	var xp = new XMLHttpRequest();
				var el = document.getElementById("receivers");
				list = el.children;
				reclist = "";
				
				if( list.length != 0 )
				{
				for( k = 0 ; k < list.length ; k++ )
					reclist = reclist+" "+list[k].innerHTML;
				
				details = {}
				details["receivers"] = reclist;
				
				var tagel = document.getElementsByTagName("select");
				var tag = tagel[0].options[tagel[0].selectedIndex].innerHTML;
				
				details["tag"] = tag;
				var sub = document.getElementById("sub").value;
				details["sub"] = sub;
                                var msg = document.getElementById("msg").value;
				details["msg"] = msg;
                                var send_id = document.getElementById("idofuser").innerHTML;
				details["send_id"] = send_id;
                                var sender_name = document.getElementById("user").innerHTML;
        			details["sender_name"] = sender_name;
                                if( tag != "" )
                                {
                                        xhr.open("POST",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/send",true);
					xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                                        xhr.send(JSON.stringify(details));
                                        xhr.onreadystatechange = function(){
                                                if( xhr.readyState == 4 && xhr.status == 200 )
                                                {
							animatemsg("Message Sent!");    
							$("#composer").fadeOut("fast");
                                                	sa.className = "down";
							gettagcount();
			                                e = document.getElementById("inboxme");
                                   			      $("#close").fadeOut("fast");
                                              		      $("#sender").fadeOut("fast"); 
                                           		      $("#composer").fadeOut("fast");
                                
                             			       e.className = "sideactive";
                            			       $("#inboxer").fadeIn("slow");
                            			       whatisopened=0;
    	                  			       sa = e;	
						       localStorage.clear();
						       openinbox(activeelement);
						}
                                        }
                                }
				}
                                else
                               	{
                                                animatemsg("Receivers field can not be left empty");
                                }
                	});	
			function showinbox()
			{
				$("#dlt").hide();
				sa.className = "down";
				$("#searchdiv").show();
				$("#imgforward").hide();
				$("#imgreply").hide();
				divname =  sa.id.slice(0,-2);
                                e = document.getElementById("inboxme");
				$("#mailicons").fadeIn("fast");  
                                document.getElementById("maildetails").style.display = "none";
				if ( divname == "compose" )
                                {
                                         $("#close").fadeOut("fast");
                                                 $("#sender").fadeOut("fast"); 
                                                 $("#composer").fadeOut("fast");

                                }
				else if( divname == "sent" )
                                {     document.getElementById("senter").style.display = "none";     
                               	      $("#draftdelete").fadeOut("fast");
				      document.getElementById("Sentmaildetails").style.display = "none";
				} 
				else if(divname == "trash" )
                                {               $("#trasher").hide();
						document.getElementById("trashdetails").style.display = "none"; 
				}
				else if( divname == "drafts" )
                                {      $("#draftdelete").fadeOut("fast");
				      document.getElementById("draftser").style.display = "none";
						document.getElementById("composerD").style.display = "none";
				}
                                $("#"+divname+"er").fadeOut("fast");
                                e.className = "sideactive";
                                $("#inboxer").fadeIn("slow");
                                whatisopened = 0;
                                sa = e;
                                
                                var xhr = new XMLHttpRequest();
                                var l = document.getElementById("idofuser").innerHTML;
                                xhr.open("GET",conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/show?id="+l,true);
                                xhr.send();

                                xhr.onreadystatechange = function()
                                {
                                        if( xhr.readyState == 4 && xhr.status == 200 )
                                        {       
                                                obj=JSON.parse(xhr.responseText);
                                                jQuery.each(obj, function(key, value) {
                                                            //console.log(key, value);
                                                            tmpobj = value;
                                                            jQuery.each(tmpobj,function(key,value){
                                                                    if (key=="tag"&&value=="Academics"){
                                                                         //console.log(key,value);
                                                                         }
                                                                    });
				           });
					   openinbox(activeelement);
                                	}       
				}
			}
			$("#inboxme").click(function(){	showinbox(); 
					$("#dlt").hide();
			});
		

			$("#draftsme").click(function(){
               			       
				       $("#dlt").hide();
				       sa.className = "down";
                              	       e = document.getElementById("draftsme");
                               	       document.getElementById("search").value = "";
	                               $("#searchbox").hide();
					$("#searchdiv").hide();
				       $("#mailicons").fadeOut("fast");  
				       divname =  sa.id.slice(0,-2);
                         	       if ( divname == "compose" )
                                	{
						 $("#close").fadeOut("fast");
						 $("#sender").fadeOut("fast"); 
						 $("#composer").fadeOut("fast");
	
					}
					 else if( divname == "sent" )
	                                 {
						$("#draftdelete").fadeOut("fast");     
						document.getElementById("senter").style.display = "none";    
					      document.getElementById("Sentmaildetails").style.display = "none";
					} 
					else if( divname == "inbox" )
					{
					     document.getElementById("inboxer").style.display = "none";
					     document.getElementById("maildetails").style.display = "none";

					}
					else if(divname == "trash" )
					{	$("#trasher").hide();
						document.getElementById("trashdetails").style.display = "none"; 
					}
					else if( divname == "drafts" )
                                {      $("#draftdelete").fadeOut("fast");
				      document.getElementById("draftser").style.display = "none";
						document.getElementById("composerD").style.display = "none";
				}
					$("#"+divname+"er").fadeOut("slow");
 
                      	                e.className = "sideactive";
        	            		$("#draftser").fadeIn("slow");
					sa = e;
				
					$("#draftdelete").fadeIn("slow");
					refreshdraftmails();
				
			});
			$("#sentme").click(function(){

				$("#dlt").hide();
				document.getElementById("search").value = "";
	                        $("#searchbox").hide();
				$("#searchdiv").hide();
	
				sa.className = "down";
                                e = document.getElementById("sentme");
                                divname =  sa.id.slice(0,-2);
				$("#mailicons").fadeOut("fast");     
				if ( divname == "compose" )
                                {
                                         $("#close").fadeOut("fast");
                                                 $("#sender").fadeOut("fast"); 
                                                 $("#composer").fadeOut("fast");

                                }
                             	else if( divname == "sent" )
				{
					$("#draftdelete").fadeOut("fast");
                                      document.getElementById("senter").style.display = "none";     
					document.getElementById("Sentmaildetails").style.display = "none";
				}else if(divname == "inbox" )
				{	
				     document.getElementById("inboxer").style.display = "none";
				     document.getElementById("maildetails").style.display = "none";
				}	
				else if(divname == "trash" )
				{
						$("#trasher").hide();
						document.getElementById("trashdetails").style.display = "none"; 		
				}
				else if( divname == "drafts" )
                                {      $("#draftdelete").fadeOut("fast");
				      document.getElementById("draftser").style.display = "none";
						document.getElementById("composerD").style.display = "none";
				}

				$("#draftdelete").fadeIn("fast");
			        $("#"+divname+"er").fadeOut("fast");
                           
			        e.className = "sideactive";
                                $("#senter").fadeIn("slow");
                                sa = e;
                               	
				document.getElementById("senter").style.display = "block";
        	                document.getElementById("Sentmaildetails").style.display = "none";             
	 
				refreshsentmails();
			});
			$("#trashme").click(function(){
				$("#dlt").show();
					sa.className = "down";
					e = document.getElementById("trashme");
					e.className = "sideactive";	
                                	divname =  sa.id.slice(0,-2); 
					document.getElementById("trashdetails").style.display = "none"; 
					$("#mailicons").fadeOut("fast"); 
					$("#searchdiv").hide();
					document.getElementById("search").value = "";
	                        $("#searchbox").hide();
                                	if ( divname == "compose" )
                                	{
                                        	 $("#close").fadeOut("fast");
                                                 $("#sender").fadeOut("fast"); 
                                                 $("#composer").fadeOut("fast");

	                               	}
                             	        else if( divname == "sent" )
					{
						$("#draftdelete").fadeOut("fast");
						document.getElementById("Sentmaildetails").style.display = "none";
                                      		document.getElementById("senter").style.display = "none";     
					}                                	
					else if(divname == "inbox" )
                        	        {       
                                	     document.getElementById("inboxer").style.display = "none";
                        	             document.getElementById("maildetails").style.display = "none";
                	                }       
					else if( divname == "drafts" )
                                {      $("#draftdelete").fadeOut("fast");
				      document.getElementById("draftser").style.display = "none";
						document.getElementById("composerD").style.display = "none";
				}
					sa = e;
					refreshtrashmails();
					$("#trasher").fadeIn("fast");

			});

			$("#closeS").click(function(){
				document.getElementById("Sentmaildetails").style.display = "none";
				document.getElementById("senter").style.display = "block";
			});
			$("#closeT").click(function(){
				document.getElementById("trashdetails").style.display = "none";
				document.getElementById("trasher").style.display = "block";
			});
			$("#trashdelete").click(function(){
					var xml = new XMLHttpRequest();
					xml.open("GET", conn+"://"+ip+":"+port+"/ITWSII_StudentsMail/main/deleteTrash", true);
					xml.send();
					xml.onreadystatechange = function(){
						if(xml.readyState == 4 && xml.status == 200){
							animatemsg("Trash Empty!");
							refreshtrashmails();
						}
					}
			});
		});
