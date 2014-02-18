/**
 * @api {get} /image/data/:id 3. Read data of a Image
 * @apiVersion 1.0.0
 * @apiName GetImageData
 * @apiGroup Image
 *
 * @apiDescription Show Image
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Image-ID
 * 
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         description: "Fly Python",
 *         format: "PNG",
 *         createddatetime: "2014-01-12, 23:52:04",
 *         filename: "python.png",
 *        +uploader: {...},
 *         id: 1,
 *         updateddatetime: "2014-01-12, 23:52:04",
 *        +checks: [...]
 *       }
 *     }
 */
function show_data() {return;}

/**
 * @api {get} /image/:id 4. Show Image 
 * @apiVersion 1.0.0
 * @apiName GetImage
 * @apiGroup Image
 *
 * @apiDescription Show Image
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Image-ID
 * 
 */
function show() {return;}

/**
 * @api {get} /images 2. List data of Images
 * @apiVersion 1.0.0
 * @apiName ListImages
 * @apiGroup Image
 * @apiDescription  List Images
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} offset offset
 * @apiParam {Number} size   size
 * @apiParam {Number} user_id user_id
 * 
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: "",
 *         count: 2
 *       },
 *       data: [
 *         {
 *           description: "Fly Python",
 *           format: "PNG",
 *           createddatetime: "2014-01-13, 00:38:05",
 *           filename: "python.png",
 *          +uploader: {...},
 *           id: 1,
 *           updateddatetime: "2014-01-13, 00:38:05",
 *          +checks: [...]
 *         },
 *        +{...},
 *         ..
 *       ]
 *     }
 */
function list() {return;}

/**
 * @api {post} /images 1. Create a new Image
 * @apiVersion 1.0.0
 * @apiName PostImages
 * @apiGroup Image
 *
 * @apiDescription Create Image
 * 
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number}   id              Image-ID
 * @apiParam {POST-Params} __POST-Params__ 
 * @apiParam {File}     image           image file
 * @apiParam {String}   description     description 
 * @apiParam {Number}   user_id          user_id      
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         description: "Fly Python",
 *         format: "PNG",
 *         createddatetime: "2014-01-12, 23:52:04",
 *         filename: "python.png",
 *        +uploader: {...},
 *         id: 1,
 *         updateddatetime: "2014-01-12, 23:52:04",
 *        +checks: [...]
 *       }
 *     }
 */
function create() {return;}

/**
 * @api {put} /image/data/:id 5. Change a new Image
 * @apiVersion 1.0.0
 * @apiName PutImage
 * @apiGroup Image
 *
 * @apiDescription Update Image
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number}   id              Image-ID
 * @apiParam {POST-Params} __POST-Params__ 
 * @apiParam {File}     image           image file
 * @apiParam {String}   description     description 
 * @apiParam {Number}   user_id          user_id      
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         description: "Fly Python",
 *         format: "PNG",
 *         createddatetime: "2014-01-12, 23:52:04",
 *         filename: "python.png",
 *        +uploader: {...},
 *         id: 1,
 *         updateddatetime: "2014-01-12, 23:52:04",
 *        +checks: [...]
 *       }
 *     }
 */
function update() {return;}

/**
 * @api {delete} /image/:id 6. Delete a Image
 * @apiVersion 1.0.0
 * @apiName DeleteImage
 * @apiGroup Image
 *
 * @apiDescription Delete Image
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Image-ID
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

