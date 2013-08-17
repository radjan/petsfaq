/***add listener***/
$(document).ready(function(){
	$('#accordion2 a').click(function(e){
		e.preventDefault();
		var hid=$(location).attr('href').split('=')[1];
		console.log('into ');
		document.location.href='/hospitals'+'?hid='+hid;

	});
});
	//if click hospital detail, then has tabs(info,vets,blog) can choose
    $('#personTab a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    });
//ajax
$(document).ready(function(){
	
	//set accortinion not collapse
	$('#collapseHospital').collapse({
  		hide: true
	});
	var search_url = "/api/v1";
	/*
	$.ajax({
        url: search_url+'/hospital/'+hid,
        type: "GET",
        cache: false
      }).done(function(data) {

       console.log(data.name);
      });
    */
	//get vet's data
	var url=$(location).attr('href');
	var pid=url.split('/')[url.split('/').length-1].split('?')[0];
	
	$.ajax({
        url: search_url+'/person/'+pid,
        type: "GET",
        cache: false
      }).done(function(data) {
       putVetData(data);
       //console.log(data.name);
      });
	
});
function putVetData(person){
	//console.log(person.name);
	
	var hid=$.url().param('hid');
	var hname='';
	//add person img and name
	var p=$("div[name=person_info]");
	p.find('h2[name=name]').text(person.name);
	
	//add role and change top tip menu
	var roles=person.roles;
	for(i in roles){
		//console.log(roles[i].hospital.id+"/"+hid);
		if(roles[i].hospital.id==hid){			
			hname=roles[i].hospital.name;	
		}
		if(roles[i].kind=='Role_vet'){
		var roleTag=$("div[name=role_templete]").last().clone();
		roleTag.find('a').attr('href','#role_'+roles[i].id);
		roleTag.find('a').text('獸醫');
		roleTag.find('.accordion_body').id='role_'+roles[i].id;
		}
	}
	//case vets
	if(hname.length>0){
		$("a[name=hLists]").text("Hopital Lists > "+hname+" > "+person.name);
	}else{
		//not vets case
	}

	}
function putVetRole(data){
	//identify role:{Role_vet}
	
}