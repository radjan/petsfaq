/**
 * @api {get} /mission/:id 3. Read data of a Mission
 * @apiVersion 1.0.0
 * @apiName GetMission
 * @apiGroup Mission
 *
 * @apiDescription Show Mission
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Mission-ID
 * 
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         id: 1,
 *         status: "new",
 *         animal_id: 2,
 *         name: "救小貓",
 *         dest_location_id: null,
 *         reporter: {},
 *         createddatetime: "2014-02-19 00:18:28",
 *         completed: false,
 *         reporter_id: 1,
 *         note: "傍晚出沒，怕人，用罐頭吸引也不會過來",
 *         due_time: null,
 *         dest_location: null,
 *         place: "新店陽光橋橋下",
 *         animal: {},
 *         host_id: 1,
 *         host: {},
 *         updateddatetime: "2014-02-19 00:18:28",
 *         type: "rescue",
 *         accepter_assocs: [
 *           {
 *             mission: {},
 *             user: {},
 *             status: "accepted",
 *             createddatetime: "2014-02-19 00:18:28",
 *             is_owner: false,
 *             description: null,
 *             updateddatetime: "2014-02-19 00:18:28"
 *           }
 *         ]
 *       }
 *     }
 */
function show() {return;}

/**
 * @api {get} /missions 2. List Missions
 * @apiVersion 1.0.0
 * @apiName ListMissions
 * @apiGroup Mission
 * @apiDescription  List Missions
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
 *           msg: "",
 *           count: 3
 *       },
 *       data: [
 *         {
 *           id: 1,
 *           status: "new",
 *           animal_id: 2,
 *           name: "救小貓",
 *           dest_location_id: null,
 *           reporter: {},
 *           createddatetime: "2014-02-19 00:18:28",
 *           completed: false,
 *           reporter_id: 1,
 *           note: "傍晚出沒，怕人，用罐頭吸引也不會過來",
 *           due_time: null,
 *           dest_location: null,
 *           place: "新店陽光橋橋下",
 *           animal: {},
 *           host_id: 1,
 *           host: {},
 *           updateddatetime: "2014-02-19 00:18:28",
 *           type: "rescue",
 *           accepter_assocs: [
 *             {
 *               mission: {},
 *               user: {},
 *               status: "accepted",
 *               createddatetime: "2014-02-19 00:18:28",
 *               is_owner: false,
 *               description: null,
 *               updateddatetime: "2014-02-19 00:18:28"
 *             }
 *           ]
 *         },
 *        +{...},
 *         ..
 *       ]
 *     }
 */     
function list() {return;}

/**
 * @api {post} /missions 1. Create a new Mission
 * @apiVersion 1.0.0
 * @apiName PostMissions
 * @apiGroup Mission
 *
 * @apiDescription Create Mission
 * 
 * @apiParam {Body} __Body__
 * @apiParam {String}   name                mission name *Required
 * @apiParam {String}   type                valid mission types: rescue, pickup, stay, deliver, adopt *Required
 * @apiParam {String}   status              status *Required // TBD
 * @apiParam {String}   place               place description 
 * @apiParam {String}   note                note
 * @apiParam {Datetime} due_time            mission due time
 * @apiParam {Boolean}  completed           completed
 * @apiParam {Number}   animal_id           animal_id *Required
 * @apiParam {Number}   dest_location_id    location_id         
 * @apiParam {Number}   host_id             user_id
 * @apiParam {Number}   from_location_id    location_id // pickup mission only
 * @apiParam {String}   requirement         adopt requirement // adopt mission only
 * @apiParam {String}   period              description for staying period // stay mission only
 * @apiParam {String}   skill               description if special skill is needed // stay mission only
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *           id: 1,
 *           status: true,
 *           msg: ""
 *       },
 *       data: {
 *         id: 1,
 *         status: "new",
 *         animal_id: 2,
 *         name: "救小貓",
 *         dest_location_id: null,
 *         reporter: {},
 *         createddatetime: "2014-02-19 00:18:28",
 *         completed: false,
 *         reporter_id: 1,
 *         note: "傍晚出沒，怕人，用罐頭吸引也不會過來",
 *         due_time: null,
 *         dest_location: null,
 *         place: "新店陽光橋橋下",
 *         animal: {},
 *         host_id: 1,
 *         host: {},
 *         updateddatetime: "2014-02-19 00:18:28",
 *         type: "rescue",
 *         accepter_assocs: []
 *       }
 *     }
 */

function create() {return;}

/**
 * @api {put} /mission/:id 4. Change a new Mission
 * @apiVersion 1.0.0
 * @apiName PutMission
 * @apiGroup Mission
 *
 * @apiDescription Update Mission
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number}   id                  Mission-ID
 * @apiParam {Body} __Body__
 * @apiParam {String}   name                *Required, mission name 
 * @apiParam {String}   type                *Required but can not change, valid mission types: rescue, pickup, stay, deliver, adopt
 * @apiParam {String}   status              *Required, status // TBD       
 * @apiParam {String}   place               place description 
 * @apiParam {String}   note                note
 * @apiParam {Datetime} due_time            mission due time
 * @apiParam {Boolean}  completed           completed
 * @apiParam {Number}   animal_id           *Required, animal_id         
 * @apiParam {Number}   dest_location_id    location_id         
 * @apiParam {Number}   host_id             user_id
 * @apiParam {Number}   from_location_id    location_id // pickup mission only
 * @apiParam {String}   requirement         adopt requirement // adopt mission only
 * @apiParam {String}   period              description for staying period // stay mission only
 * @apiParam {String}   skill               description if special skill is needed // stay mission only
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         id: 1,
 *         status: "new",
 *         animal_id: 2,
 *         name: "救小貓",
 *         dest_location_id: null,
 *         reporter: {},
 *         createddatetime: "2014-02-19 00:18:28",
 *         completed: false,
 *         reporter_id: 1,
 *         note: "傍晚出沒，怕人，用罐頭吸引也不會過來",
 *         due_time: null,
 *         dest_location: null,
 *         place: "新店陽光橋橋下",
 *         animal: {},
 *         host_id: 1,
 *         host: {},
 *         updateddatetime: "2014-02-19 00:18:28",
 *         type: "rescue",
 *         accepter_assocs: [
 *           {
 *             mission: {},
 *             user: {},
 *             status: "accepted",
 *             createddatetime: "2014-02-19 00:18:28",
 *             is_owner: false,
 *             description: null,
 *             updateddatetime: "2014-02-19 00:18:28"
 *           }
 *         ]
 *       }
 *     }
 */
function update() {return;}

/**
 * @api {delete} /mission/:id 5. Delete a Mission
 * @apiVersion 1.0.0
 * @apiName DeleteMission
 * @apiGroup Mission
 *
 * @apiDescription Delete Mission
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Mission-ID
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

