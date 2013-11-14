function BlogController() {
	this.TAG = 'BlogController';
	this.articleList = new Array();
	
}

BlogController.prototype.createArticle = function(aid, aContent) {
	var article = new Article(aid);
	article.setContent(aContent);
	//article.setType();
	this.articleList.push(article);
	return article;
};

BlogController.prototype.insertToView = function(article, view) {
	//Log.d(this.TAG, view);
	if(typeof view === 'undefined') return;
	Log.d(this.TAG, article);
	view.append(article.html);
	article.getPost(article.pid);
	this.articleList.push(article);
};

BlogController.prototype.sortBy = function() {
	
};

BlogController.prototype.filterByText = function(keyword) {
	var article = null;
	for(var i=0, n=this.articleList.length; i<n; i++) {
		article = this.articleList[i];
		var content = article.content;
		//Log.d(this.TAG, 'title:'+content.title+" keyword:"+keyword);
		if(content.title.indexOf(keyword) != -1) {
			Log.d(TAG, "find keyword from: "+content.title);
			article.show(true);
		}else {
			article.show(false);
		}
	}
};

BlogController.prototype.showAll = function(isShow) {
	for(var i=0, n=this.articleList.length; i<n; i++) {
		article = this.articleList[i];
		var content = article.content;
		article.show(isShow);
	}
}
