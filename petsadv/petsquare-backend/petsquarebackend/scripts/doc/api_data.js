define({ api: [
  {
    "type": "delete",
    "url": "/animal/:id",
    "title": "5. Delete a Animal",
    "version": "1.0.0",
    "name": "DeleteAnimal",
    "group": "Animal",
    "description": "Delete Animal",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Animal-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: null\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "get",
    "url": "/animal/:id",
    "title": "3. Read data of a Animal",
    "version": "1.0.0",
    "name": "GetAnimal",
    "group": "Animal",
    "description": "Show Animal",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Animal-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       status: \"adopted\",\n       description: \"haha\",\n       createddatetime: \"2014-02-19 00:18:28\",\n       owner: null,\n       updateddatetime: \"2014-02-19 00:18:28\",\n       image_assocs: [],\n       type: \"cat\",\n       sub_type: \"normal\",\n       id: 1,\n       finder: {},\n       name: \"pochi\"\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "post",
    "url": "/animal/:id/images",
    "title": "6. Link the Animal with a Image",
    "version": "1.0.0",
    "name": "LinkAnimalImage",
    "group": "Animal",
    "description": "Link the Animal with a Image",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Animal-ID"
          },
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "image_id",
            "optional": false,
            "description": "*Required, a existed image_id"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "status"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n        status: \"halfway\",\n        description: \"XD\",\n        createddatetime: \"2014-02-22 14:45:29\",\n        image: {...},\n        animal: {...},\n        updateddatetime: \"2014-02-22 14:45:29\",\n        id: 1\n      }\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "get",
    "url": "/animals",
    "title": "2. List Animals",
    "version": "1.0.0",
    "name": "ListAnimals",
    "group": "Animal",
    "description": "List Animals",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "offset",
            "optional": false,
            "description": "offset"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "size",
            "optional": false,
            "description": "size"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "animal_id"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "animal name"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "type",
            "optional": false,
            "description": "speicies types // cat, dog, ..."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "sub_type",
            "optional": false,
            "description": "condition types // TBD: sick, newborn"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "status // TBD"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "finder_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "owner_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "find_location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "current_location_id",
            "optional": false,
            "description": "location_id"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n         msg: \"\",\n         count: 3\n     },\n     data: [\n       {\n         status: \"adopted\",\n         description: \"haha\",\n         createddatetime: \"2014-02-19 00:18:28\",\n         owner: null,\n         updateddatetime: \"2014-02-19 00:18:28\",\n         image_assocs: [],\n         type: \"cat\",\n         id: 1,\n         finder: {},\n         name: \"pochi\"\n       },\n      +{...},\n       ..\n     ]\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "post",
    "url": "/animals",
    "title": "1. Create a new Animal",
    "version": "1.0.0",
    "name": "PostAnimals",
    "group": "Animal",
    "description": "Create Animal, auto assign the login user as the finder",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "*Required, animal name"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "type",
            "optional": false,
            "description": "*Required, speicies types // cat, dog, ..."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "sub_type",
            "optional": false,
            "description": "*Required, condition types // TBD: sick, newborn"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "*Required, status // TBD"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "owner_id",
            "optional": false,
            "description": "user_id // in case the animal is a pet"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "find_location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "current_location_id",
            "optional": false,
            "description": "location_id"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n         id: 1,\n         status: true,\n         msg: \"\"\n     },\n     data: {\n       status: \"adopted\",\n       description: \"haha\",\n       createddatetime: \"2014-02-19 00:18:28\",\n       owner: null,\n       updateddatetime: \"2014-02-19 00:18:28\",\n       image_assocs: [],\n       type: \"cat\",\n       sub_type: \"normal\",\n       id: 1,\n       finder: {},\n       name: \"pochi\"\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "put",
    "url": "/animal/:id",
    "title": "4. Change a new Animal",
    "version": "1.0.0",
    "name": "PutAnimal",
    "group": "Animal",
    "description": "Update Animal",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Animal-ID"
          },
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "animal name"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "type",
            "optional": false,
            "description": "speicies types // cat, dog, ..."
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "sub_type",
            "optional": false,
            "description": "condition types // sick, newborn"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "status"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "finder_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "owner_id",
            "optional": false,
            "description": "user_id // in case the animal is a pet"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "find_location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "current_location_id",
            "optional": false,
            "description": "location_id"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       status: \"adopted\",\n       description: \"haha\",\n       createddatetime: \"2014-02-19 00:18:28\",\n       owner: null,\n       updateddatetime: \"2014-02-19 00:18:28\",\n       image_assocs: [],\n       type: \"cat\",\n       sub_type: \"normal\",\n       id: 1,\n       finder: {},\n       name: \"pochi\"\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "get",
    "url": "/animal/:id/image/:image_id",
    "title": "7. Get the Metadata of the Animal-Image Linkage",
    "version": "1.0.0",
    "name": "ShowAnimalImageMeta",
    "group": "Animal",
    "description": "Show the Metadata of an Animal-Image Linkage",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Animal-ID"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "image_id",
            "optional": false,
            "description": "Image-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n        status: \"halfway\",\n        description: \"XD\",\n        createddatetime: \"2014-02-22 14:45:29\",\n        image: {...},\n        animal: {...},\n        updateddatetime: \"2014-02-22 14:45:29\",\n        id: 1\n      }\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "delete",
    "url": "/animal/:id/image/:image_id",
    "title": "9. Unlink the Animal with a Image",
    "version": "1.0.0",
    "name": "UnlinkAnimalImage",
    "group": "Animal",
    "description": "Unink the Animal with a Image",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Animal-ID"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "image_id",
            "optional": false,
            "description": "Image-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: null\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "put",
    "url": "/animal/:id/image/:image_id",
    "title": "8. Update the Metadata of the Animal-Image Linkage",
    "version": "1.0.0",
    "name": "UpdateAnimalImageMeta",
    "group": "Animal",
    "description": "Update the Metadata of an Animal-Image Linkage",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Animal-ID"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "image_id",
            "optional": false,
            "description": "Image-ID"
          },
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "status"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n        status: \"halfway\",\n        description: \"XD\",\n        createddatetime: \"2014-02-22 14:45:29\",\n        image: {...},\n        animal: {...},\n        updateddatetime: \"2014-02-22 14:45:29\",\n        id: 1\n      }\n   }\n"
        }
      ]
    },
    "filename": "api/animal.js"
  },
  {
    "type": "delete",
    "url": "/check/:id",
    "title": "5. Delete a Check",
    "version": "1.0.0",
    "name": "DeleteCheck",
    "group": "Check",
    "description": "Delete Check",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Check-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true, \n       msg: \"\" \n     }, \n     data: null\n   }\n"
        }
      ]
    },
    "filename": "api/check.js"
  },
  {
    "type": "get",
    "url": "/check/:id",
    "title": "3. Read data of a Check",
    "version": "1.0.0",
    "name": "GetCheck",
    "group": "Check",
    "description": "Show Check",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Check-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       title: \"check1\",\n       createddatetime: \"2014-01-12, 23:52:04\",\n      +image: {...},\n      +user: {...},\n       updateddatetime: \"2014-01-12, 23:52:04\",\n       id: 1,\n      +location: {...}\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/check.js"
  },
  {
    "type": "get",
    "url": "/checks",
    "title": "2. List Checks",
    "version": "1.0.0",
    "name": "ListChecks",
    "group": "Check",
    "description": "List Checks",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "offset",
            "optional": false,
            "description": "offset"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "size",
            "optional": false,
            "description": "size"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n         msg: \"\",\n         count: 3\n     },\n     data: [\n       {\n         description: \"1\",\n         title: \"check1\",\n         createddatetime: \"2014-01-12, 23:52:04\",\n        +image: {...},\n        +user: {...},\n         updateddatetime: \"2014-01-12, 23:52:04\",\n         id: 1,\n        +location: {...}\n       },\n      +{...},\n       ..\n     ]\n   }\n"
        }
      ]
    },
    "filename": "api/check.js"
  },
  {
    "type": "post",
    "url": "/checks",
    "title": "1. Create a new Check",
    "version": "1.0.0",
    "name": "PostChecks",
    "group": "Check",
    "description": "Create Check",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "title",
            "optional": false,
            "description": "title"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "image_id",
            "optional": false,
            "description": "image_id"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n       info: {\n           status: true,\n           msg: \"\"\n       },\n       data: {\n           description: \"1\",\n           title: \"check1\",\n           createddatetime: \"2014-01-03, 20:46:03\",\n           image: {\n               description: \"1\",\n               format: \"PNG\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               user_id: 1,\n               filename: \"python.png\",\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1\n           },\n           user_id: 1,\n           location: {\n               description: \"1\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               user_id: 1,\n               longitude: 121.5130475,\n               address: \"taipei\",\n               latitude: 25.040063,\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1,\n               name: \"one\"\n           },\n           updateddatetime: \"2014-01-03, 20:46:03\",\n           id: 1\n       }\n   }\n"
        }
      ]
    },
    "filename": "api/check.js"
  },
  {
    "type": "put",
    "url": "/check/:id",
    "title": "4. Change a new Check",
    "version": "1.0.0",
    "name": "PutCheck",
    "group": "Check",
    "description": "Update Check",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Check-ID"
          },
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "title",
            "optional": false,
            "description": "title"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "image_id",
            "optional": false,
            "description": "image_id"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       title: \"check1\",\n       createddatetime: \"2014-01-12, 23:52:04\",\n      +image: {...},\n      +user: {...},\n       updateddatetime: \"2014-01-12, 23:52:04\",\n       id: 1,\n      +location: {...}\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/check.js"
  },
  {
    "type": "delete",
    "url": "/image/:id",
    "title": "6. Delete a Image",
    "version": "1.0.0",
    "name": "DeleteImage",
    "group": "Image",
    "description": "Delete Image",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Image-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true, \n       msg: \"\" \n     }, \n     data: null\n   }\n"
        }
      ]
    },
    "filename": "api/image.js"
  },
  {
    "type": "get",
    "url": "/image/:id",
    "title": "4. Show Image",
    "version": "1.0.0",
    "name": "GetImage",
    "group": "Image",
    "description": "Show Image",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Image-ID"
          }
        ]
      }
    },
    "filename": "api/image.js"
  },
  {
    "type": "get",
    "url": "/image/data/:id",
    "title": "3. Read data of a Image",
    "version": "1.0.0",
    "name": "GetImageData",
    "group": "Image",
    "description": "Show Image",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Image-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"Fly Python\",\n       format: \"PNG\",\n       createddatetime: \"2014-01-12, 23:52:04\",\n       filename: \"python.png\",\n      +uploader: {...},\n       id: 1,\n       updateddatetime: \"2014-01-12, 23:52:04\",\n      +checks: [...]\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/image.js"
  },
  {
    "type": "get",
    "url": "/images",
    "title": "2. List data of Images",
    "version": "1.0.0",
    "name": "ListImages",
    "group": "Image",
    "description": "List Images",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "offset",
            "optional": false,
            "description": "offset"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "size",
            "optional": false,
            "description": "size"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\",\n       count: 2\n     },\n     data: [\n       {\n         description: \"Fly Python\",\n         format: \"PNG\",\n         createddatetime: \"2014-01-13, 00:38:05\",\n         filename: \"python.png\",\n        +uploader: {...},\n         id: 1,\n         updateddatetime: \"2014-01-13, 00:38:05\",\n        +checks: [...]\n       },\n      +{...},\n       ..\n     ]\n   }\n"
        }
      ]
    },
    "filename": "api/image.js"
  },
  {
    "type": "post",
    "url": "/images",
    "title": "1. Create a new Image",
    "version": "1.0.0",
    "name": "PostImages",
    "group": "Image",
    "description": "Create Image",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Image-ID"
          },
          {
            "group": "Parameter",
            "type": "POST-Params",
            "field": "__POST-Params__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "File",
            "field": "image",
            "optional": false,
            "description": "image file"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"Fly Python\",\n       format: \"PNG\",\n       createddatetime: \"2014-01-12, 23:52:04\",\n       filename: \"python.png\",\n      +uploader: {...},\n       id: 1,\n       updateddatetime: \"2014-01-12, 23:52:04\",\n      +checks: [...]\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/image.js"
  },
  {
    "type": "put",
    "url": "/image/data/:id",
    "title": "5. Change a new Image",
    "version": "1.0.0",
    "name": "PutImage",
    "group": "Image",
    "description": "Update Image",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Image-ID"
          },
          {
            "group": "Parameter",
            "type": "POST-Params",
            "field": "__POST-Params__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "File",
            "field": "image",
            "optional": false,
            "description": "image file"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"Fly Python\",\n       format: \"PNG\",\n       createddatetime: \"2014-01-12, 23:52:04\",\n       filename: \"python.png\",\n      +uploader: {...},\n       id: 1,\n       updateddatetime: \"2014-01-12, 23:52:04\",\n      +checks: [...]\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/image.js"
  },
  {
    "type": "delete",
    "url": "/location/:id",
    "title": "5. Delete a Location",
    "version": "1.0.0",
    "name": "DeleteLocation",
    "group": "Location",
    "description": "Delete Location",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Location-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true, \n       msg: \"\" \n     }, \n     data: null\n   }\n"
        }
      ]
    },
    "filename": "api/location.js"
  },
  {
    "type": "get",
    "url": "/location/:id",
    "title": "3. Read data of a Location",
    "version": "1.0.0",
    "name": "GetLocation",
    "group": "Location",
    "description": "Show Location",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Location-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       createddatetime: \"2014-01-13, 00:47:42\",\n      +explorer: {...},\n       longitude: 121.5130475,\n      +checks: [...],\n       address: \"taipei\",\n       latitude: 25.040063,\n       updateddatetime: \"2014-01-13, 00:47:42\",\n       id: 1,\n       name: \"one\"\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/location.js"
  },
  {
    "type": "get",
    "url": "/locations",
    "title": "2. List Locations",
    "version": "1.0.0",
    "name": "ListLocations",
    "group": "Location",
    "description": "List Locations",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "offset",
            "optional": false,
            "description": "offset"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "size",
            "optional": false,
            "description": "size"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\",\n       count: 3\n     },\n     data: [\n       {\n         description: \"1\",\n         createddatetime: \"2014-01-13, 00:47:42\",\n        +explorer: {...}, // user object\n         longitude: 121.5130475,\n        +checks: [...],\n         address: \"taipei\",\n         latitude: 25.040063,\n         updateddatetime: \"2014-01-13, 00:47:42\",\n         id: 1,\n         name: \"one\"\n       },\n      +{...},\n       ..\n     ]\n   }\n"
        }
      ]
    },
    "filename": "api/location.js"
  },
  {
    "type": "get",
    "url": "/locations/search",
    "title": "6. Search Locations(by latlng)",
    "version": "1.0.0",
    "name": "LocationsSearch",
    "group": "Location",
    "description": "Search Locations(by latlng)",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "latitude",
            "optional": false,
            "description": "latitude"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "longitude",
            "optional": false,
            "description": "longitude"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "radius",
            "optional": false,
            "description": "offset by degree (default: 0.00449661)"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "size",
            "optional": false,
            "description": "return record counts (default: 100)"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\",\n       count: 1\n     },\n     data: [\n       {\n        +missions: [...],\n         description: \"1\",\n         createddatetime: \"2014-01-13, 00:47:42\",\n        +explorer: {...}, // user object\n         longitude: 121.5130475,\n        +checks: [...],\n        +pickup_missions_from: [...],\n         address: \"taipei\",\n         latitude: 25.040063,\n         updateddatetime: \"2014-01-13, 00:47:42\",\n         id: 1,\n         name: \"one\"\n       },\n      +{...},\n       ..\n     ]\n   }\n"
        }
      ]
    },
    "filename": "api/location.js"
  },
  {
    "type": "post",
    "url": "/locations",
    "title": "1. Create a new Location",
    "version": "1.0.0",
    "name": "PostLocations",
    "group": "Location",
    "description": "Create Location",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "name"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "longitude",
            "optional": false,
            "description": "longitude"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "latitude",
            "optional": false,
            "description": "latitude"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "address",
            "optional": false,
            "description": "address"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       createddatetime: \"2014-01-13, 00:47:42\",\n      +explorer: {...},\n       longitude: 121.5130475,\n      +checks: [...],\n       address: \"taipei\",\n       latitude: 25.040063,\n       updateddatetime: \"2014-01-13, 00:47:42\",\n       id: 1,\n       name: \"one\"\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/location.js"
  },
  {
    "type": "put",
    "url": "/location/:id",
    "title": "4. Change a new Location",
    "version": "1.0.0",
    "name": "PutLocation",
    "group": "Location",
    "description": "Update Location",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Location-ID"
          },
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "name"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "description",
            "optional": false,
            "description": "description"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "longitude",
            "optional": false,
            "description": "longitude"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "latitude",
            "optional": false,
            "description": "latitude"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "address",
            "optional": false,
            "description": "address"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       createddatetime: \"2014-01-13, 00:47:42\",\n      +explorer: {...},\n       longitude: 121.5130475,\n      +checks: [...],\n       address: \"taipei\",\n       latitude: 25.040063,\n       updateddatetime: \"2014-01-13, 00:47:42\",\n       id: 1,\n       name: \"one\"\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/location.js"
  },
  {
    "type": "delete",
    "url": "/mission/:id",
    "title": "5. Delete a Mission",
    "version": "1.0.0",
    "name": "DeleteMission",
    "group": "Mission",
    "description": "Delete Mission",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Mission-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true, \n       msg: \"\" \n     }, \n     data: null\n   }\n"
        }
      ]
    },
    "filename": "api/mission.js"
  },
  {
    "type": "get",
    "url": "/mission/:id",
    "title": "3. Read data of a Mission",
    "version": "1.0.0",
    "name": "GetMission",
    "group": "Mission",
    "description": "Show Mission",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Mission-ID"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       id: 1,\n       status: \"new\",\n       animal_id: 2,\n       name: \"救小貓\",\n       dest_location_id: null,\n       reporter: {},\n       createddatetime: \"2014-02-19 00:18:28\",\n       completed: false,\n       reporter_id: 1,\n       note: \"傍晚出沒，怕人，用罐頭吸引也不會過來\",\n       due_time: null,\n       dest_location: null,\n       place: \"新店陽光橋橋下\",\n       animal: {},\n       host_id: 1,\n       host: {},\n       updateddatetime: \"2014-02-19 00:18:28\",\n       type: \"rescue\",\n       accepter_assocs: [\n         {\n           mission: {},\n           user: {},\n           status: \"accepted\",\n           createddatetime: \"2014-02-19 00:18:28\",\n           is_owner: false,\n           description: null,\n           updateddatetime: \"2014-02-19 00:18:28\"\n         }\n       ]\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/mission.js"
  },
  {
    "type": "get",
    "url": "/missions",
    "title": "2. List Missions",
    "version": "1.0.0",
    "name": "ListMissions",
    "group": "Mission",
    "description": "List Missions",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "offset",
            "optional": false,
            "description": "offset"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "size",
            "optional": false,
            "description": "size"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "type",
            "optional": false,
            "description": "mission types: rescue, pickup, stay, deliver, adopt, support"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "mission status"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "field": "completed",
            "optional": false,
            "description": "completed"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "animal_id",
            "optional": false,
            "description": "animal_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "reporter_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "host_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "dest_location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "from_location_id",
            "optional": false,
            "description": "location_id"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n         msg: \"\",\n         count: 3\n     },\n     data: [\n       {\n         id: 1,\n         status: \"new\",\n         animal_id: 2,\n         name: \"救小貓\",\n         dest_location_id: null,\n         reporter: {},\n         createddatetime: \"2014-02-19 00:18:28\",\n         completed: false,\n         reporter_id: 1,\n         note: \"傍晚出沒，怕人，用罐頭吸引也不會過來\",\n         due_time: null,\n         dest_location: null,\n         place: \"新店陽光橋橋下\",\n         animal: {},\n         host_id: 1,\n         host: {},\n         updateddatetime: \"2014-02-19 00:18:28\",\n         type: \"rescue\",\n         accepter_assocs: [\n           {\n             mission: {},\n             user: {},\n             status: \"accepted\",\n             createddatetime: \"2014-02-19 00:18:28\",\n             is_owner: false,\n             description: null,\n             updateddatetime: \"2014-02-19 00:18:28\"\n           }\n         ]\n       },\n      +{...},\n       ..\n     ]\n   }\n"
        }
      ]
    },
    "filename": "api/mission.js"
  },
  {
    "type": "post",
    "url": "/missions",
    "title": "1. Create a new Mission",
    "version": "1.0.0",
    "name": "PostMissions",
    "group": "Mission",
    "description": "Create Mission, auto assign the login user as the reporter",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "*Required, mission name"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "type",
            "optional": false,
            "description": "*Required, valid mission types: rescue, pickup, stay, deliver, adopt, support"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "*Required, status // TBD"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "place",
            "optional": false,
            "description": "place description"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "note",
            "optional": false,
            "description": "note"
          },
          {
            "group": "Parameter",
            "type": "Datetime",
            "field": "due_time",
            "optional": false,
            "description": "mission due time, format example: 2014-02-21 16:15:00"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "field": "completed",
            "optional": false,
            "description": "completed"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "animal_id",
            "optional": false,
            "description": "*Required, animal_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "dest_location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "host_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "from_location_id",
            "optional": false,
            "description": "location_id // pickup mission only"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "requirement",
            "optional": false,
            "description": "adopt requirement // adopt mission only"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "period",
            "optional": false,
            "description": "description for staying period // stay mission only"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "skill",
            "optional": false,
            "description": "description if special skill is needed // stay mission only"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n         id: 1,\n         status: true,\n         msg: \"\"\n     },\n     data: {\n       id: 1,\n       status: \"new\",\n       animal_id: 2,\n       name: \"救小貓\",\n       dest_location_id: null,\n       reporter: {},\n       createddatetime: \"2014-02-19 00:18:28\",\n       completed: false,\n       reporter_id: 1,\n       note: \"傍晚出沒，怕人，用罐頭吸引也不會過來\",\n       due_time: null,\n       dest_location: null,\n       place: \"新店陽光橋橋下\",\n       animal: {},\n       host_id: 1,\n       host: {},\n       updateddatetime: \"2014-02-19 00:18:28\",\n       type: \"rescue\",\n       accepter_assocs: []\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/mission.js"
  },
  {
    "type": "put",
    "url": "/mission/:id",
    "title": "4. Change a new Mission",
    "version": "1.0.0",
    "name": "PutMission",
    "group": "Mission",
    "description": "Update Mission",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Mission-ID"
          },
          {
            "group": "Parameter",
            "type": "Body",
            "field": "__Body__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "*Required, mission name"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "type",
            "optional": false,
            "description": "*Required but can not change, valid mission types: rescue, pickup, stay, deliver, adopt, support"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "*Required, status // TBD"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "place",
            "optional": false,
            "description": "place description"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "note",
            "optional": false,
            "description": "note"
          },
          {
            "group": "Parameter",
            "type": "Datetime",
            "field": "due_time",
            "optional": false,
            "description": "mission due time, format example: 2014-02-21 16:15:00"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "field": "completed",
            "optional": false,
            "description": "completed"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "animal_id",
            "optional": false,
            "description": "*Required, animal_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "dest_location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "reporter_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "host_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "from_location_id",
            "optional": false,
            "description": "location_id // pickup mission only"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "requirement",
            "optional": false,
            "description": "adopt requirement // adopt mission only"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "period",
            "optional": false,
            "description": "description for staying period // stay mission only"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "skill",
            "optional": false,
            "description": "description if special skill is needed // stay mission only"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       id: 1,\n       status: \"new\",\n       animal_id: 2,\n       name: \"救小貓\",\n       dest_location_id: null,\n       reporter: {},\n       createddatetime: \"2014-02-19 00:18:28\",\n       completed: false,\n       reporter_id: 1,\n       note: \"傍晚出沒，怕人，用罐頭吸引也不會過來\",\n       due_time: null,\n       dest_location: null,\n       place: \"新店陽光橋橋下\",\n       animal: {},\n       host_id: 1,\n       host: {},\n       updateddatetime: \"2014-02-19 00:18:28\",\n       type: \"rescue\",\n       accepter_assocs: [\n         {\n           mission: {},\n           user: {},\n           status: \"accepted\",\n           createddatetime: \"2014-02-19 00:18:28\",\n           is_owner: false,\n           description: null,\n           updateddatetime: \"2014-02-19 00:18:28\"\n         }\n       ]\n     }\n   }\n"
        }
      ]
    },
    "filename": "api/mission.js"
  },
  {
    "type": "get",
    "url": "/user/me/missions",
    "title": "1. List Missions of Current Login User",
    "version": "1.0.0",
    "name": "GetMissionOfUser",
    "group": "UserMe",
    "description": "Show Mission of Current Login User.",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "QueryString",
            "field": "__QueryString__",
            "optional": false,
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "offset",
            "optional": false,
            "description": "offset"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "size",
            "optional": false,
            "description": "size"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "type",
            "optional": false,
            "description": "mission types: rescue, pickup, stay, deliver, adopt"
          },
          {
            "group": "Parameter",
            "type": "String",
            "field": "status",
            "optional": false,
            "description": "mission status"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "field": "completed",
            "optional": false,
            "description": "completed"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "animal_id",
            "optional": false,
            "description": "animal_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "reporter_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "host_id",
            "optional": false,
            "description": "user_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "dest_location_id",
            "optional": false,
            "description": "location_id"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "from_location_id",
            "optional": false,
            "description": "location_id"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n         msg: \"\",\n         count: 3\n     },\n     data: [\n       {\n         id: 1,\n         status: \"new\",\n         animal_id: 2,\n         name: \"救小貓\",\n         dest_location_id: null,\n         reporter: {},\n         createddatetime: \"2014-02-19 00:18:28\",\n         completed: false,\n         reporter_id: 1,\n         note: \"傍晚出沒，怕人，用罐頭吸引也不會過來\",\n         due_time: null,\n         dest_location: null,\n         place: \"新店陽光橋橋下\",\n         animal: {},\n         host_id: 1,\n         host: {},\n         updateddatetime: \"2014-02-19 00:18:28\",\n         type: \"rescue\",\n         accepter_assocs: [\n           {\n             mission: {},\n             user: {},\n             status: \"accepted\",\n             createddatetime: \"2014-02-19 00:18:28\",\n             is_owner: false,\n             description: null,\n             updateddatetime: \"2014-02-19 00:18:28\"\n           }\n         ]\n       },\n      +{...},\n       ..\n     ]\n   }\n"
        }
      ]
    },
    "filename": "api/userme.js"
  }
] });