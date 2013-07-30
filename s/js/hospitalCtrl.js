   /*setting browser height*/
    var showIndex = 0; //the select item index
    //var initLists_h = parseInt($(window).height() - $("#hospital_div").offset().top); //the browser height
     // alert( initLists_h);
    var firstY = 0; //the first hospital point of y
    //$("#hospital_div").height(initLists_h);
    /****/
    $(document).ready(

    function showHospital() {
      var q = $.url().param('q');
      //alert(q);
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
    });
    //event listener
    $(document).ready(function(){
         /*add accordion2 handler**/
    /**if collapseHospital in means clear vets data**/
    $("#hospitalTab").hide();
    $("#accordion2 a[name=hLists]").click(function(e){

       var length=$("div[name=oneVet]").length;
       //alert(length);
       if(length>1){
        $("#vets").empty();
        $("a[name=hLists]").text("Hopital Lists >");
        $("#hospitalTab").hide();
        $("#hospital_info").empty();
        //$("#hospital_info").empty();
        //$("#hospital_info").empty();
       }
    });
    });
    function nameSearch() {
      $("#hospital_div div[name=hospital_template]").remove();
      var p=document.createElement("p");
      var list_menu = "a[name=list_menu]";
      $(p).html="searching...";
       $(p).insertBefore(list_menu);
      $.ajax({
        url: "/api/v1/hospital?name=*" + $('#name_search').val() + "*",
        type: "GET",
        cache: false
      }).done(function(data) {
        createHospitals(data,hospitalClickHndlr);
      });
    }

    function createHospitals(_data, callback) {
      $("#hospital_div div[name=hospital_template]").remove();
      //empty和remove差別在前者清空tag裡的值，後者輕空tag漢內容值

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
        var showItem = e.target.parentNode.parentNode;
        //var hSize = $('div[name=hospital_template]').length-1;//-1 include the 
        /**zmin 140716 ui**/
       
       var hid=$(this).attr("href");
        //add vet list
        getVetData(hid); //get vets data
        
        /**zmin 140716 ui(end)**/
      });
      /***zmin e**/

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
    $('#hospitalTab a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    });


    /** 0704 vet list get***/
    /**
     * [showHospitalDetail description] get hospital's vets
     * @param  {[String]} _hid [description] the hospital's id
     * @return {[type]}      [description]
     */

    function getVetData(_hid) {
      $.ajax({
        url: "/api/v1/hospital/" + _hid,
        type: "GET",
        cache: false
      }).done(function(data) {
          $("#accordion2 a[name=hLists]").click();
          $("#hospitalTab").show();
          $("#hospital_info").tab('show');
        putVetData(data);    
      });
    }
    /**
     * [putVetData description] add vet data
     * @param  {[type]} hospital [description] hospital'json data
     * @return {[type]}          [description]
     */

    function putVetData(hospital,callback) {
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
        v.find("span[name=vet_name]").text(vs[i].person.name);
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
        callback();
      };
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