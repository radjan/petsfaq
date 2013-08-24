    /*** To show specialies and can create new species with select. Use the following HTML template.
     
     <ul id='specialties'></ul>  <!-- put this to where you want to show the selecotr -->
    ======= HTML template ======
    <div class='specialtySelector'>
      <li name='spec_item'>
       <label>種類：</label>
       <select name='species_' class='species'>
          <option value=''>未選擇</option>
       </select>
       <input name="newSpecies" type="text" placeholder="新增種類" class="input-block-level inputNewSpecies">
       <label>專科：</label>
       <select name='category_' class='category'>
          <option value='' class="optionCategory">一般</option>
       </select>
       <input name="newCategory" type="text" placeholder="新增專科" class="input-block-level inputNewCategory">
       <!-- <textarea class="inputNewCategory" rows="1" autofocus></textarea> -->
      </li> 
    </div>
    
    */

    var ready = false;
    var species = [];
    var categories = [];

    function initSpecialtiesSelection(rootElement, defaultAmonut, initValues) {
        $.ajax({
            url: "/api/v1/specialty/species",
            type: "GET",
            cache: false
        }).done(function(_data){
            species = _data;
            initSpecialties(rootElement, defaultAmonut, initValues);
        });
        
        $.ajax({
            url: "/api/v1/specialty/categories",
            type: "GET",
            cache: false
        }).done(function(_data){
            categories = _data;
            initSpecialties(rootElement, defaultAmonut, initValues);
        });
    }

    function initSpecialties(rootElement, defaultAmonut, initValues) {
        if (ready) {
            for (var i = 1; i <= defaultAmonut; i++) {
                var init = null;

                if(initValues != null && i <= initValues.length){
                    init = initValues[i-1];
                }
                addSpecialty(rootElement, i, init);    
            }
        } else {
            ready = true;
        }
    }

    function addSpecialty(rootElement, n, initValue) {
        var s = $(".specialtySelector").find('li[name=spec_item]').clone();
        var input_species = s.find('.species');
        for (i in species) {
            input_species.append('<option value="' + species[i]+ '">' + species[i] + '</option>');
        }
        input_species.append('<option value="createSpecies"> 找不到合適的種類，新增種類</option>');
        s.find(".inputNewSpecies").hide();
        // input_species.append('<option name="new_species" value="new">新增</option>');
        
        var input_categories = s.find('.category');
        for (i in categories) {
            input_categories.append('<option value="' + categories[i]+ '" class="optionCategory">' + categories[i] + '</option>');
        }
        input_categories.append('<option value="createCategory">找不到合適的專科，新增專科</option>');
        s.find(".inputNewCategory").hide();
        // input_categories.append('<option name="new_category" value="new">新增</option>');

        input_species.attr('name', input_species.attr('name') + n);
        input_categories.attr('name', input_categories.attr('name') + n);

        if(initValue != null){
            input_species.val(initValue.specialty.species);
            input_categories.val(initValue.specialty.category);    
        }else{
            input_categories.val("一般");    
        }

        rootElement.append(s);

        input_species.change(function(){
          var _inputNewSpecies = s.find(".inputNewSpecies");
          if (input_species.val() == "createSpecies") {
            _inputNewSpecies.show();
            _inputNewSpecies.attr("name", input_species.attr("name"));
            input_species.attr("name", input_species.attr("name")+"_bak");

          }else{
            if(_inputNewSpecies.css("display") != "none"){
              _inputNewSpecies.hide();
              input_species.attr("name", _inputNewSpecies.attr("name"));
              _inputNewSpecies.attr("name", "");
            }
          }

        });

        input_categories.change(function(){
          var _inputNewCategory = s.find(".inputNewCategory");
          if (input_categories.val() == "createCategory") {
            _inputNewCategory.show();
            _inputNewCategory.attr("name",input_categories.attr("name"));
            input_categories.attr("name",input_categories.attr("name")+"_bak");
          }else{
            if (_inputNewCategory.css("display") != "none") {
              _inputNewCategory.hide();
              input_categories.attr("name",_inputNewCategory.attr("name"));
              _inputNewCategory.attr("name","");  
            }
            
          }
        });
    }

    function setValue(){

    }
