function BlogController() {
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
	
	Log.consoleLog(view);
	if(typeof view === 'undefined') return;
	Log.consoleLog(article);
	view.append(article.html);
}
