var api_prefix = "/api/v1/";
var TAG = "blogAPI";

function getPostList(handler, errHandler) {
	var api_url = api_prefix + 'posts';
	$.get(api_url, function(data) {
		//console.log(data);
		
		if(typeof data !== 'undefined' && typeof data.blogpostids !== 'undefined') {
			var postList = data.blogpostids[0];
			for(var i=0, n=postList.length; i<n; i++) {
				var pid = postList[i];
				
			}			
		}
		handler(postList);
	});
}

/**
 *
 */
function getPostImgByImgId(imgId, handler, errHandler) {
	var api_url = api_prefix + 'image';
	$.get(api_url, function(data) {
		//console.log(data);
		if(typeof data !== 'undefined' && typeof data.blogpostids !== 'undefined') {
			var imgPath = data;
			handler(postList);
		}
	});
}

/**
 * Get a post content by requested post id 
 * @param {Object} pid the requested post id
 * @param {Object} handler
 * 
 *   photoids:
    [ 
      {pid}
      ...
    ],
  title: {title},
  last_modified: {timestamp},
  status_code: {publish value},
  authorid: {pid},
  created: {timestamp},
  content: {content},
  hospitalid: {hid}
 */
function getPostByPid(pid, handler) {
	var api_url = api_prefix + 'post/' + pid;
	$.get(api_url, function(data) {
		Log.d("getPostByPid()", data);
		if(typeof data !== 'undefined') {
			var preview = data.content.substring(0, 20)+"...";
			var createdDate = new Date(data.created);
			var postContent = {
				title: data.title,
				pet_type: 'default', 
				pet_name: 'default', 
				preview_content: preview,
				created_date: createdDate,
				photo_ids_list: data.photoids
			};
			handler(postContent);
		}else {
			//TODO error handle
			
		}
	});
}

function getPostsByPersonId(pid, handler, errorHandler) {
	_getPostsList('personid', pid, handler, errorHandler);
}

/**
 *	Get a id list of post by specified hospital id
 * @param hId int 
 * @param handler 
 * @param errHandler 
 */
function getPostsByHospitalId(hid, handler, errorHandler) {
	_getPostsList('hospitalid', hid, handler, errorHandler);
}

function _getPostsList(api, id, handler, errorHandler) {
	var api_url = api_prefix + 'posts?' + api + '=' +id;
	$.get(api_url, function(data) {
		//console.log(data);
		if(typeof data !== 'undefined' && typeof data.blogpostids !== 'undefined') {
			var postList = data.blogpostids;
			for(var i=0, n=postList.length; i<n; i++) {
				var pid = postList[i];
			}			
		}
		handler(postList);
	});
}
