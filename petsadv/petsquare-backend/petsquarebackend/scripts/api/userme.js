/**
 * @api {get} /user/me/missions 1. List Missions of Current Login User
 * @apiVersion 1.0.0
 * @apiName GetMissionOfUser
 * @apiGroup UserMe
 *
 * @apiDescription Show Mission of Current Login User.
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} offset    offset
 * @apiParam {Number} size      size
 * @apiParam {String} type      mission types: rescue, pickup, stay, deliver, adopt
 * @apiParam {String} status    mission status
 * @apiParam {Boolean} completed    completed
 * @apiParam {Number} animal_id     animal_id
 * @apiParam {Number} reporter_id   user_id
 * @apiParam {Number} host_id       user_id
 * @apiParam {Number} dest_location_id  location_id
 * @apiParam {Number} from_location_id  location_id
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
function myMissions() {return;}
