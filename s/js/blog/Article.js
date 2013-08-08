function Article(aid) {
	//article id
	this.TAG = "Article"+aid;
	this.aid = (aid != null && typeof aid !== 'undefined')? aid : 0;
	this.html = null;
} 

/**
 *	<div id='{#id}' class='btn article_preview'>
 * 		<span class='pet_type'>CAT</span>
 * 		<span class='pet_name'>MAGGIE</span>
 * 		<span class='title'>MAGGIE got sick</span>
 * 		<div class='preview_body'>
 * 			<div class='preview_content'>今天因Maggie因為偷吃魚而卡到刺</div>
 * 		</div>
 * 	</div>
 * 
 * @param content and object that contains below data
 * { pet_type, pet_name, title, preview_content}
 */
Article.prototype.setContent = function(content) {
	var html = $("<div class='btn article_preview'></div>");
	Log.d(this.TAG, "id="+this.aid);
	Log.consoleLog(content);
	html.attr("id", "article_"+this.aid);
	var pType = $("<span class='pet_type btn btn-info disabled'>"+content.pet_type+"</span>");
	var pName = $("<span class='pet_name btn btn-success disabled '>"+content.pet_name+"</span>");
	var title = $("<span class='title'>"+content.title+"</span>");
	
	html.append(pType);
	html.append(pName);
	html.append(title);
	
	var previewBody = $("<div class='preview_body'></div>");
	var previewContent = $("<div class='preview_content'>"+content.preview_content+"</div>");
	previewBody.append(previewContent);
	html.append(previewBody);
	this.html = html;
};
