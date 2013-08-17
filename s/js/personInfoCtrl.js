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
	//put info to top tip menu
	var hid=$.url().param('hid');
	var hname='';
	
	var roles=person.roles;
	for(i in roles){
		console.log(roles[i].hospital.id+"/"+hid);
		if(roles[i].hospital.id==hid){			
			hname=roles[i].hospital.name;
			break;
		}
	}
	//case vets
	if(hname.length>0){
		$("a[name=hLists]").text("Hopital Lists > "+hname+" > "+person.name);
	}else{
		//not vets case
	}
	//put info to info.
	var v = $("div[name=oneVet]").last().clone();
	v.find("span[name=vet_name]").append(person.name);
	v.find("span[name=vet_desc]").text(person.description);
    v.find("span[name=vet_mail]").text(person.email);
    $("#vets").append(v);
    /*
        for (j in vs[i].experience) {
          v.find("dl[name=exp]").append("<dd>" + vs[i].experience[j] + "</dd>");
        }
        for (j in vs[i].education) {
          v.find("dl[name=exp]").append("<dd>" + vs[i].education[j] + "</dd>");
        }
        // alert(initSpecialties(1));
        for (j in vs[i].specialties) {
          var s = vs[i].specialties[j].specialty;
          v.find("dl[name=specialty]").append("<dd>" + s.species + ": " + s.category + "</dd>");
          // v.find("dl[name=specialty]").append("<ul id='specialties'></ul>");
        }
        vets.append(v);
      
      }
    */
	}