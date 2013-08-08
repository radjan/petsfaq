var api_prefix = "/api/v1/";

function getPostList(handler, errHandler) {
	var api_url = api_prefix + 'posts';
	$.get(api_url, function(data) {
		console.log(data);
		
		if(typeof data !== 'undefined' && typeof data.blogpostids !== 'undefined') {
			var postList = data.blogpostids;
			for(var i=0, n=postList.length; i<n; i++) {
				var pid = postList[i];
				
			}			
		}
		
		
		
		handler();
	});
}

function getPostByPid(pid, handler) {
	
}
