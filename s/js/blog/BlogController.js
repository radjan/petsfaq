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
	//Log.d(this.TAG, article);
	view.append(article.html);
	article.getPost(article.pid);
};

BlogController.prototype.sortBy = function() {
	
};
