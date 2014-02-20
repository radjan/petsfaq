/**
 * @api {get} /location/:id 3. Read data of a Location
 * @apiVersion 1.0.0
 * @apiName GetLocation
 * @apiGroup Location
 *
 * @apiDescription Show Location
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Location-ID
 * 
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         description: "1",
 *         createddatetime: "2014-01-13, 00:47:42",
 *        +explorer: {...},
 *         longitude: 121.5130475,
 *        +checks: [...],
 *         address: "taipei",
 *         latitude: 25.040063,
 *         updateddatetime: "2014-01-13, 00:47:42",
 *         id: 1,
 *         name: "one"
 *       }
 *     }
 */
function show() {return;}

/**
 * @api {get} /locations 2. List Locations
 * @apiVersion 1.0.0
 * @apiName ListLocations
 * @apiGroup Location
 * @apiDescription  List Locations
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} offset offset
 * @apiParam {Number} size   size
 * 
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: "",
 *         count: 3
 *       },
 *       data: [
 *         {
 *           description: "1",
 *           createddatetime: "2014-01-13, 00:47:42",
 *          +explorer: {...}, // user object
 *           longitude: 121.5130475,
 *          +checks: [...],
 *           address: "taipei",
 *           latitude: 25.040063,
 *           updateddatetime: "2014-01-13, 00:47:42",
 *           id: 1,
 *           name: "one"
 *         },
 *        +{...},
 *         ..
 *       ]
 *     }
 */
function list() {return;}

/**
 * @api {post} /locations 1. Create a new Location
 * @apiVersion 1.0.0
 * @apiName PostLocations
 * @apiGroup Location
 *
 * @apiDescription Create Location
 * 
 * @apiParam {Body} __Body__
 * @apiParam {String}   name            name        
 * @apiParam {String}   description     description 
 * @apiParam {Number}   longitude       longitude         
 * @apiParam {Number}   latitude        latitude         
 * @apiParam {String}   address         address     
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         description: "1",
 *         createddatetime: "2014-01-13, 00:47:42",
 *        +explorer: {...},
 *         longitude: 121.5130475,
 *        +checks: [...],
 *         address: "taipei",
 *         latitude: 25.040063,
 *         updateddatetime: "2014-01-13, 00:47:42",
 *         id: 1,
 *         name: "one"
 *       }
 *     }
 */
function create() {return;}

/**
 * @api {put} /location/:id 4. Change a new Location
 * @apiVersion 1.0.0
 * @apiName PutLocation
 * @apiGroup Location
 *
 * @apiDescription Update Location
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Location-ID
 * @apiParam {Body} __Body__
 * @apiParam {String}   name            name        
 * @apiParam {String}   description     description 
 * @apiParam {Number}   longitude       longitude         
 * @apiParam {Number}   latitude        latitude         
 * @apiParam {String}   address         address     
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         description: "1",
 *         createddatetime: "2014-01-13, 00:47:42",
 *        +explorer: {...},
 *         longitude: 121.5130475,
 *        +checks: [...],
 *         address: "taipei",
 *         latitude: 25.040063,
 *         updateddatetime: "2014-01-13, 00:47:42",
 *         id: 1,
 *         name: "one"
 *       }
 *     }
 */
function update() {return;}

/**
 * @api {delete} /location/:id 5. Delete a Location
 * @apiVersion 1.0.0
 * @apiName DeleteLocation
 * @apiGroup Location
 *
 * @apiDescription Delete Location
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Location-ID
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true, 
 *         msg: "" 
 *       }, 
 *       data: null
 *     } 
 */

function delete() {return;}

/**
 * @api {get} /locations/search 6. Search Locations(by latlng)
 * @apiVersion 1.0.0
 * @apiName LocationsSearch
 * @apiGroup Location
 * @apiDescription  Search Locations(by latlng)
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} latitude  latitude
 * @apiParam {Number} longitude longitude
 * @apiParam {Number} radius    offset by degree (default: 0.00449661)
 * @apiParam {Number} size      return record counts (default: 100)
 * 
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: "",
 *         count: 1
 *       },
 *       data: [
 *         {
 *          +missions: [...],
 *           description: "1",
 *           createddatetime: "2014-01-13, 00:47:42",
 *          +explorer: {...}, // user object
 *           longitude: 121.5130475,
 *          +checks: [...],
 *          +pickup_missions_from: [...],
 *           address: "taipei",
 *           latitude: 25.040063,
 *           updateddatetime: "2014-01-13, 00:47:42",
 *           id: 1,
 *           name: "one"
 *         },
 *        +{...},
 *         ..
 *       ]
 *     }
 */
function search() {return;}


