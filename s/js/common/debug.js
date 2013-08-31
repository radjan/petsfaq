/**
 * @author zen
 */

Log = {
	isDebug : true
}

Log.d = function(TAG, msg){
    if (this.isDebug) {
        if (typeof console !== "undefined") {
            if(typeof msg === 'object'){
            	console.log("[" + TAG + "]==BEGIN ++++++++++++++++++++");
            	console.log(msg);
            	console.log("[" + TAG + "]==END-----------------------");
            }
            else console.log("[" + TAG + "]\t" + msg);
        }
    }
}
