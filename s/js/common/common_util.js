var dateFormat1 = "yyyy/mm/dd<br/>H:MM:ss TT";

/**
 * please include the date.format.js first 
 */
function getDateString(date, format) {
	if(typeof format === 'undefined')
		format = dateFormat1;
	return date.format(format);
	
	/*var d = date.getDate();
    var m = date.getMonth() + 1;
    var y = date.getFullYear();
    return '' + y + '/' + (m<=9 ? '0' + m : m) + '/' + (d <= 9 ? '0' + d : d);
	*/
}

function delayedCall(fn, time) {
    setTimeout(fn, time);
}
