function Article(pid) {
	//article id
	this.TAG = "Article"+pid;
	this.pid = (pid != null && typeof pid !== 'undefined')? pid : 0;
	this.html = null;
	this.content = {};
	
	this._init();
} 

Article.prototype._init = function() {
	var html = $("<div class='article_wrapper'></div>");
	//Log.d(this.TAG, "pid="+this.pid);
	html.attr("id", this.pid);
	html.append("<div class='ajax-load'><img src='s/img/common/ajax-loader-small-trans.gif' /></div>")
	this.html = html;
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
	var arrow = $("<i class='arrow_left'></i>");
	var contentBody = $("<div class='btn article_preview span4' style='width:70%'></div>");
	this.content = content;
	Log.d(this.TAG, "pid="+this.pid);
	//Log.d(this.TAG, content);
	//html.attr("id", "article_"+this.pid);
	var pType = $("<span class='pet_type '>"+content.pet_type+"</span>");
	var pName = $("<span class='pet_name '>"+content.pet_name+"</span>");
	var title = $("<span class='title'>"+content.title+"</span>");
	var createdDate = $("<div class='date span1 small' style='width:20%'>"+getDateString(content.created_date)+"</div>");
	
	contentBody.append(pType);
	contentBody.append(pName);
	contentBody.append(title);
	
	var previewBody = $("<div class='preview_body'></div>");
	var previewContent = $("<div class='preview_content'>"+content.preview_content+"<i class='icon-play'></i></div>");
	previewBody.append(previewContent);
	contentBody.append(previewBody);
	
	this.html.append(arrow);
	this.html.append(contentBody);
	this.html.append(createdDate);
};

Article.prototype.getPost = function(postId) {
	var _this = this;
	var callback = function(content){
		_this.setContent(content);
		//remove ajax-loading animation
		$("div[id='"+_this.pid+"'] div.ajax-load").remove();
	};
	getPostByPid(postId, callback);
};

Article.prototype.show = function(isShow) {
	Log.d(this.html);
	if(isShow)
		this.html.show();
	else this.html.hide();
};