/**
 * @api {get} /animal/:id 3. Read data of a Animal
 * @apiVersion 1.0.0
 * @apiName GetAnimal
 * @apiGroup Animal
 *
 * @apiDescription Show Animal
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Animal-ID
 * 
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         status: "adopted",
 *         description: "haha",
 *         createddatetime: "2014-02-19 00:18:28",
 *         owner: null,
 *         updateddatetime: "2014-02-19 00:18:28",
 *         image_assocs: [],
 *         type: "cat",
 *         sub_type: "normal",
 *         id: 1,
 *         finder: {},
 *         name: "pochi"
 *       }
 *     }
 */
function show() {return;}

/**
 * @api {get} /animals 2. List Animals
 * @apiVersion 1.0.0
 * @apiName ListAnimals
 * @apiGroup Animal
 * @apiDescription  List Animals
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} offset    offset
 * @apiParam {Number} size      size
 * @apiParam {Number} id        animal_id
 * @apiParam {String} name      animal name
 * @apiParam {String} type      speicies types // cat, dog, ...
 * @apiParam {String} sub_type  condition types // TBD: sick, newborn
 * @apiParam {String} status    status // TBD
 * @apiParam {Number} finder_id user_id
 * @apiParam {Number} owner_id  user_id
 * @apiParam {Number} find_location_id      location_id
 * @apiParam {Number} current_location_id   location_id
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
 *           status: "adopted",
 *           description: "haha",
 *           createddatetime: "2014-02-19 00:18:28",
 *           owner: null,
 *           updateddatetime: "2014-02-19 00:18:28",
 *           image_assocs: [],
 *           type: "cat",
 *           id: 1,
 *           finder: {},
 *           name: "pochi"
 *         },
 *        +{...},
 *         ..
 *       ]
 *     }
 */     
function list() {return;}

/**
 * @api {post} /animals 1. Create a new Animal
 * @apiVersion 1.0.0
 * @apiName PostAnimals
 * @apiGroup Animal
 *
 * @apiDescription Create Animal, auto assign the login user as the finder
 * 
 * @apiParam {Body} __Body__
 * @apiParam {String}   name                *Required, animal name
 * @apiParam {String}   type                *Required, speicies types // cat, dog, ...
 * @apiParam {String}   sub_type            *Required, condition types // TBD: sick, newborn
 * @apiParam {String}   status              *Required, status // TBD
 * @apiParam {String}   description         description
 * @apiParam {Number}   owner_id            user_id // in case the animal is a pet
 * @apiParam {Number}   find_location_id    location_id
 * @apiParam {Number}   current_location_id location_id
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
 *         status: "adopted",
 *         description: "haha",
 *         createddatetime: "2014-02-19 00:18:28",
 *         owner: null,
 *         updateddatetime: "2014-02-19 00:18:28",
 *         image_assocs: [],
 *         type: "cat",
 *         sub_type: "normal",
 *         id: 1,
 *         finder: {},
 *         name: "pochi"
 *       }
 *     }
 */

function create() {return;}

/**
 * @api {put} /animal/:id 4. Change a new Animal
 * @apiVersion 1.0.0
 * @apiName PutAnimal
 * @apiGroup Animal
 *
 * @apiDescription Update Animal
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number}   id                  Animal-ID
 * @apiParam {Body} __Body__
 * @apiParam {String}   name                animal name
 * @apiParam {String}   type                speicies types // cat, dog, ...
 * @apiParam {String}   sub_type            condition types // sick, newborn
 * @apiParam {String}   status              status
 * @apiParam {String}   description         description
 * @apiParam {Number}   finder_id           user_id
 * @apiParam {Number}   owner_id            user_id // in case the animal is a pet
 * @apiParam {Number}   find_location_id    location_id
 * @apiParam {Number}   current_location_id location_id
 *
 * @apiSuccessExample Successful Response Body:
 *     HTTP/1.1 200 OK
 *     {
 *       info: {
 *         status: true,
 *         msg: ""
 *       },
 *       data: {
 *         status: "adopted",
 *         description: "haha",
 *         createddatetime: "2014-02-19 00:18:28",
 *         owner: null,
 *         updateddatetime: "2014-02-19 00:18:28",
 *         image_assocs: [],
 *         type: "cat",
 *         sub_type: "normal",
 *         id: 1,
 *         finder: {},
 *         name: "pochi"
 *       }
 *     }
 */
function update() {return;}

/**
 * @api {delete} /animal/:id 5. Delete a Animal
 * @apiVersion 1.0.0
 * @apiName DeleteAnimal
 * @apiGroup Animal
 *
 * @apiDescription Delete Animal
 *
 * @apiParam {QueryString} __QueryString__ 
 * @apiParam {Number} id Animal-ID
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

