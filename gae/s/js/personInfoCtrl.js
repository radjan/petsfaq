/***add listener***/
var search_url = "/api/v1";

$(document).ready(function(){
	$('#accordion2 a').click(function(e){
		e.preventDefault();
		var hid=$(location).attr('href').split('=')[1];
		console.log('into ');
		if(hid=='undefined'){
			document.location.href='/hospitals';
		}
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
	loadPostsByPid(pid);
	$.ajax({
        url: search_url+'/person/'+pid,
        type: "GET",
        cache: false
      }).done(function(data) {
       putPersonData(data);

       //console.log(data.name);
      });
	
});
function putPersonData(person){
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
		if(roles[i].kind=="Role_Vet"){
			putPersonRole(roles[i]);
		}
	}
	//case vets
	if(hname.length>0){
		$("a[name=hLists]").text("Hopital Lists > "+hname+" > "+person.name);
	}else{
		//not vets case
		$("a[name=hLists]").text(person.name);
	}

	}

function putPersonRole(data){
	
	//identify role:{Role_vet}
	var roleTag=$("div[name=role_templete]").last().clone();
		roleTag.find('a').attr('href','#role_'+data.id);
		roleTag.find('a').text('獸醫');
		roleTag.find('.accordion_body').id='role_'+data.id;
	var roleFrame=roleTag.find('.accordion-inner');
	var roleInfo=$('dl[name=role_vet]').last().clone();
	roleInfo.append('<dt>簡介</dt><dd>'+data.description+'</dd>');
	
	roleInfo.append('<dt>所屬醫院</dt><dd>'+data.hospital.name+'</dd>');
	roleInfo.append('<dd>'+data.hospital.zipcode+data.hospital.county+data.hospital.address+'</dd>');
	roleInfo.append('<dt>個人門診時間</dt><dd> &nbsp</dd>');
	roleInfo.append('<dt>專長</dt>');
	var specialties=data.specialties;

	for(var i in specialties){

		roleInfo.append('<dd>'+specialties[i].specialty.species+" : "+specialties[i].specialty.category+'科</dd>');		
	}
	roleInfo.append('<dt>學歷</dt><dd>'+data.education+'</dd>');
	roleInfo.append('<dt>經歷</dt><dd>'+data.experience+'</dd>');
	roleFrame.append(roleInfo);
	$('#accordion_roles').append(roleTag);
}