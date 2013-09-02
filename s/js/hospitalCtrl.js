/***add hospital eventlistener***/
    //check has param
    $(document).ready(function (){
      var hid=$.url().param('hid');
      
      if(typeof(hid)=='undefined' || hid==''){

        showHospital();
        $("#hospital_data").hide();
      }else{
        //alert('');
       $('#collapseHospital').collapse({
            hide: true
         });
       showHospital();
       getVetData(hid);
      }

    });
    $('#accordion2 a').click(function (){
        //alert($('div[name=hospital_detail_template]').length);
        //has selected one of hospitals
        if($('div[name=hospital_detail_template]').length>1){
          $("#hospital_data").hide();
          $('#hospital_info').empty();
          $("#vets").empty();
          $("a[name=hLists]").text("Hopital Lists > ");

        }
    });

    function showHospital() {
      var q = $.url().param('q');
      
      var search_url = "/api/v1/hospital";
      if (q != undefined) {
        $('#name_search').val(q);
        search_url += '?name=*' + q;
      }
      //get hospital list
      $.ajax({
        url: search_url,
        type: "GET",
        cache: false
      }).done(function(data) {
        //alert( jQuery.parseJSON(data));
        createHospitals(data, hospitalClickHndlr);
      });
    }
    //event listener
    /**
    when input and search handler
    **/
    function nameSearch() {
      var url=window.location.toString(); 
      url=url.split("?")[0];
      $("#hospital_div div[name=hospital_template]").remove();
      //if no value in search input
      if($('#name_search').val().length<=0){
        if(url.split("?").length>1){
           //if before case has parameters,clear it
           window.location.href=url;
         }       
        return;
      }
      var p=document.createElement("p");
      var list_menu = "a[name=list_menu]";
      $(p).html="searching...";
       $(p).insertBefore(list_menu);
        window.location.href=url+"?q="+$('#name_search').val();
       /*
      $.ajax({
        url: "/api/v1/hospital?name=*" + $('#name_search').val() + "*",
        type: "GET",
        cache: false
      }).done(function(data) {
        //createHospitals(data,hospitalClickHndlr);
       
      });
     */
    }

    function createHospitals(_data, callback) {
      $("#hospital_div div[name=hospital_template]").remove();
      //empty和remove差別在前者清空tag裡的值，後者輕空tag和內容值

      var hospitals=_data;
      //alert(hospitals[0].id);
      //var hospitals = jQuery.parseJSON(_data);
      var list_menu = "a[name=list_menu]";

      for (i in hospitals) {
        //alert(hospitals[i].name);
        var h = $("div[name=hospital_template]").last().clone();
        h.find("h2[name=name]").text(hospitals[i].name);
        h.find("p[name=description]").text(hospitals[i].description);
        h.find("a[name=linkTo]").attr("href", hospitals[i].id);
        h.find("a[name=edit_mode]").attr("href", "/hospital/"+hospitals[i].id+"/edit");
        //hospital
        if(hospitals[i].logos!=""){
           // h.find("img").attr("src",hospitals[i].logos[0].img_blobkey);
            
        }
        h.find('p[name=address]').text(hospitals[i].zipcode+" "+hospitals[i].county+" "+hospitals[i].area+" "+hospitals[i].address);
        //$("#hospital_div").append(h);
        $(h).insertBefore(list_menu);
    
      }
      //add hospital deatil btn linstener
      if (typeof(callback) == 'function') {
        callback();
      };
    }
/**********/
/*click event listener handler*/
    /**  when create hospital, 
        add a[name=linkTo] click handler
     * [hospitalClickHndlr description]
     *  zmin
     */

    function hospitalClickHndlr() {


      $("a[name=linkTo]").click(function(e) {
        e.preventDefault();
        
        $("#collapseHospital").collapse('hide');
        $('#hospitalTab a:first').tab('show'); 
        var showItem = e.target.parentNode.parentNode;
        
        var hid=$(this).attr("href");
        $('input[name=hid]').val(hid);

        changeURL("hospitals?hid="+hid);
        //add vet list
        getVetData(hid); //get vets data
         });
       /**handler favorite add and remove**/
        $("a[name=favorite_btn]").click(function(){

            var isSelect=$(this).find('i').hasClass('icon-white');
            if(isSelect){
                $(this).find('i').removeClass('icon-white');
            }else{
                $(this).find('i').addClass('icon-white');
            }
        });
        /**handler favorite add and remove(end)**/        
    }
    //if click hospital detail, then has tabs(info,vets,blog) can choose
    $('#hospitalTab a').click(function (e) {
      e.preventDefault();
      var tabIndex=$(this).attr('href');
      var hid=$('input[name=]hid').val();
      
      if(tabIndex=="#hospital_blog" && $("input[name=blogLoad]").val()=='0'){
             loadPostsByHid(hid); //list post by hospital id
             $("input[name=blogLoad]").attr("value","1");
      }
      $(this).tab('show');
    });


    /** 0704 vet list get***/
    /**
     * [showHospitalDetail description] get hospital's vets
     * @param  {[String]} _hid [description] the hospital's id
     * @return {[type]}      [description]
     */

    function getVetData(_hid) {
      //alert('into getVetData');

      $.ajax({
        url: "/api/v1/hospital/" + _hid,
        type: "GET",
        cache: false
      }).done(function(data) {
          $('#collapseHospital').collapse({
            hide: true
         });
          $("#hospital_data").show();
          $("#hospital_info").tab('show');

        putVetData(data,_hid,addVetClickHndlr);    
      });
    }
    /**
     * [putVetData description] add vet data
     * @param  {[type]} hospital [description] hospital'json data
     * @return {[type]}          [description]
     */

    function putVetData(hospital,hid,callback) {


      var vets = $("#vets");
      //create hospital
     

      var h = $("div[name=hospital_detail_template]").clone();
      h.find("h2[name=name]").text(hospital.name);
      h.find("p[name=description]").text(hospital.description);
      h.find('p[name=address]').text(hospital.zipcode+" "+hospital.county+" "+hospital.area+" "+hospital.address);

      $("a[name=hLists]").text("Hopital Lists >"+hospital.name);


      $("#hospital_info").append(h);
     
      //vet
      
      var vs =hospital.vets;
      for (i in vs) {
        var v = $("div[name=oneVet]").last().clone();
        var a=document.createElement('a');
        a.href=vs[i].person.id;
        a.innerHTML=vs[i].person.name;
        //alert(a.innerHTML);
        v.find("span[name=vet_name]").append(a);
        v.find("span[name=vet_desc]").text(vs[i].description);
        v.find("span[name=vet_mail]").text(vs[i].person.email);

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
       //add hospital deatil btn linstener
      if (typeof(callback) == 'function') {
 
        callback(hid);
      };
    }
    //add vets blog and name btn click handler
    function addVetClickHndlr(hid){
      
      $("span[name=vet_name] a").click(function(e){
        
        e.preventDefault();
          //change and add param
          var url=window.location.toString();
          if(url.split("?").length<=1){
            //no param
            url+='?';
           }
           //url+='&hid='+hid+'vid='+$(this).attr("href");
           window.location.href='person/'+$(this).attr("href")+'?hid='+hid;
      });
    }

    function changeURL(url){
      window.history.pushState("", "Pets FAQ - hospitals", url);
    }

    /* Example for Yun-Tai */
     // function showHospitals(){
     //     $.ajax({
     //         url: "/api/v1/hospital",
     //         type: 'GET',
     //         cache: false
     //     }).done(function( data ) {
     //         var hospitals = jQuery.parseJSON(data);
     //         for(i in hospitals){
     //             $("#fromAJAX").append("<p>"+hospitals[i].name+":"+hospitals[i].description+":"+hospitals[i].specialty+"</p>");
     //         }
     //     });
     // }
     //
