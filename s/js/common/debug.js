/**
 * @author zen
 */

Log = {
	isDebug : true
}

Log.d = function(TAG, msg){
    if (this.isDebug) {
        if (typeof console !== "undefined") {
            console.log("[" + TAG + "]\t" + msg);
        }
    }
}

Log.consoleLog = function(msg){
    if (this.isDebug) {
        if (typeof console !== "undefined") {
            console.log(msg);
        }
    }
}