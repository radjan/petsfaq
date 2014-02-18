/**
 * @api {get} /check/:id 3. Read data of a Check
 * @apiVersion 1.0.0
 * @apiName GetCheck
 * @apiGroup Check
 *
 * @apiDescription Show Check
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Check-ID
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
 *         title: "check1",
 *         createddatetime: "2014-01-12, 23:52:04",
 *        +image: {...},
 *        +user: {...},
 *         updateddatetime: "2014-01-12, 23:52:04",
 *         id: 1,
 *        +location: {...}
 *       }
 *     }
 */
function show() {return;}

/**
 * @api {get} /checks 2. List Checks
 * @apiVersion 1.0.0
 * @apiName ListChecks
 * @apiGroup Check
 * @apiDescription  List Checks
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
 *           msg: "",
 *           count: 3
 *       },
 *       data: [
 *         {
 *           description: "1",
 *           title: "check1",
 *           createddatetime: "2014-01-12, 23:52:04",
 *          +image: {...},
 *          +user: {...},
 *           updateddatetime: "2014-01-12, 23:52:04",
 *           id: 1,
 *          +location: {...}
 *         },
 *        +{...},
 *         ..
 *       ]
 *     }
 */     
function list() {return;}

/**
 * @api {post} /checks 1. Create a new Check
 * @apiVersion 1.0.0
 * @apiName PostChecks
 * @apiGroup Check
 *
 * @apiDescription Create Check
 * 
 * @apiParam {Body} __Body__
 * @apiParam {String}   title           title        
 * @apiParam {String}   description     description 
 * @apiParam {Number}   location_id     location_id         
 * @apiParam {Number}   image_id        image_id         
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *         info: {
 *             status: true,
 *             msg: ""
 *         },
 *         data: {
 *             description: "1",
 *             title: "check1",
 *             createddatetime: "2014-01-03, 20:46:03",
 *             image: {
 *                 description: "1",
 *                 format: "PNG",
 *                 createddatetime: "2014-01-03, 20:46:03",
 *                 user_id: 1,
 *                 filename: "python.png",
 *                 updateddatetime: "2014-01-03, 20:46:03",
 *                 id: 1
 *             },
 *             user_id: 1,
 *             location: {
 *                 description: "1",
 *                 createddatetime: "2014-01-03, 20:46:03",
 *                 user_id: 1,
 *                 longtitude: 121.5130475,
 *                 address: "taipei",
 *                 latitude: 25.040063,
 *                 updateddatetime: "2014-01-03, 20:46:03",
 *                 id: 1,
 *                 name: "one"
 *             },
 *             updateddatetime: "2014-01-03, 20:46:03",
 *             id: 1
 *         }
 *     }
 */

function create() {return;}

/**
 * @api {put} /check/:id 4. Change a new Check
 * @apiVersion 1.0.0
 * @apiName PutCheck
 * @apiGroup Check
 *
 * @apiDescription Update Check
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number}   id              Check-ID
 * @apiParam {Body} __Body__
 * @apiParam {String}   title           title        
 * @apiParam {String}   description     description 
 * @apiParam {Number}   location_id     location_id         
 * @apiParam {Number}   image_id        image_id         
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
 *         title: "check1",
 *         createddatetime: "2014-01-12, 23:52:04",
 *        +image: {...},
 *        +user: {...},
 *         updateddatetime: "2014-01-12, 23:52:04",
 *         id: 1,
 *        +location: {...}
 *       }
 *     }
 */
function update() {return;}

/**
 * @api {delete} /check/:id 5. Delete a Check
 * @apiVersion 1.0.0
 * @apiName DeleteCheck
 * @apiGroup Check
 *
 * @apiDescription Delete Check
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Check-ID
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

