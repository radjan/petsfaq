define({ api: [
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
          "content": "   HTTP/1.1 200 OK\n   {\n       info: {\n           status: true,\n           msg: \"\"\n       },\n       data: {\n           description: \"1\",\n           title: \"check1\",\n           createddatetime: \"2014-01-03, 20:46:03\",\n           image: {\n               description: \"1\",\n               format: \"PNG\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               userid: 1,\n               filename: \"python.png\",\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1\n           },\n           userid: 1,\n           location: {\n               description: \"1\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               userid: 1,\n               longtitude: 121.5130475,\n               address: \"taipei\",\n               latitude: 25.040063,\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1,\n               name: \"one\"\n           },\n           updateddatetime: \"2014-01-03, 20:46:03\",\n           id: 1\n       }\n   }\n"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n       info: {\n           status: true,\n               msg: \"\",\n               count: 3\n       },\n           data: [\n           {\n               description: \"1\",\n               title: \"check1\",\n               createddatetime: \"2013-12-27, 00:32:11\",\n               image: {\n                   description: \"1\",\n                   format: \"PNG\",\n                   createddatetime: \"2013-12-27, 00:32:11\",\n                   userid: 1,\n                   filename: \"python.png\",\n                   updateddatetime: \"2013-12-27, 00:32:11\",\n                   id: 1\n               },\n               userid: 1,\n               location: {\n                   description: \"1\",\n                   createddatetime: \"2013-12-27, 00:32:11\",\n                   userid: 1,\n                   longtitude: 121.5130475,\n                   address: \"taipei\",\n                   latitude: 25.040063,\n                   updateddatetime: \"2013-12-27, 00:32:11\",\n                   id: 1,\n                   name: \"one\"\n               },\n               updateddatetime: \"2013-12-27, 00:32:11\",\n               id: 1\n           },\n           {\n               description: \"2\",\n               title: \"check2\",\n               createddatetime: \"2013-12-27, 00:32:11\",\n               image: {\n                   description: \"1\",\n                   format: \"PNG\",\n                   createddatetime: \"2013-12-27, 00:32:11\",\n                   userid: 1,\n                   filename: \"python.png\",\n                   updateddatetime: \"2013-12-27, 00:32:11\",\n                   id: 1\n               },\n               userid: 1,\n               location: {\n                   description: \"1\",\n                   createddatetime: \"2013-12-27, 00:32:11\",\n                   userid: 1,\n                   longtitude: 121.5130475,\n                   address: \"taipei\",\n                   latitude: 25.040063,\n                   updateddatetime: \"2013-12-27, 00:32:11\",\n                   id: 1,\n                   name: \"one\"\n               },\n               updateddatetime: \"2013-12-27, 00:32:11\",\n               id: 2\n           },\n           {\n               description: \"3\",\n               title: \"check3\",\n               createddatetime: \"2013-12-27, 00:32:11\",\n               image: {\n                   description: \"1\",\n                   format: \"PNG\",\n                   createddatetime: \"2013-12-27, 00:32:11\",\n                   userid: 1,\n                   filename: \"python.png\",\n                   updateddatetime: \"2013-12-27, 00:32:11\",\n                   id: 1\n               },\n               userid: 1,\n               location: {\n                   description: \"1\",\n                   createddatetime: \"2013-12-27, 00:32:11\",\n                   userid: 1,\n                   longtitude: 121.5130475,\n                   address: \"taipei\",\n                   latitude: 25.040063,\n                   updateddatetime: \"2013-12-27, 00:32:11\",\n                   id: 1,\n                   name: \"one\"\n               },\n               updateddatetime: \"2013-12-27, 00:32:11\",\n               id: 3\n           }\n       ]\n   }\n"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n       info: {\n           status: true,\n           msg: \"\"\n       },\n       data: {\n           description: \"1\",\n           title: \"check1\",\n           createddatetime: \"2014-01-03, 20:46:03\",\n           image: {\n               description: \"1\",\n               format: \"PNG\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               userid: 1,\n               filename: \"python.png\",\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1\n           },\n           userid: 1,\n           location: {\n               description: \"1\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               userid: 1,\n               longtitude: 121.5130475,\n               address: \"taipei\",\n               latitude: 25.040063,\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1,\n               name: \"one\"\n           },\n           updateddatetime: \"2014-01-03, 20:46:03\",\n           id: 1\n       }\n   }\n"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n       info: {\n           status: true,\n           msg: \"\"\n       },\n       data: {\n           description: \"1\",\n           title: \"check1\",\n           createddatetime: \"2014-01-03, 20:46:03\",\n           image: {\n               description: \"1\",\n               format: \"PNG\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               userid: 1,\n               filename: \"python.png\",\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1\n           },\n           userid: 1,\n           location: {\n               description: \"1\",\n               createddatetime: \"2014-01-03, 20:46:03\",\n               userid: 1,\n               longtitude: 121.5130475,\n               address: \"taipei\",\n               latitude: 25.040063,\n               updateddatetime: \"2014-01-03, 20:46:03\",\n               id: 1,\n               name: \"one\"\n           },\n           updateddatetime: \"2014-01-03, 20:46:03\",\n           id: 1\n       }\n   }\n"
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
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       format: \"PNG\",\n       createddatetime: \"2013-12-27, 02:19:09\",\n       userid: 1,\n       filename: \"python.png\",\n       updateddatetime: \"2013-12-27, 02:19:09\",\n       id: 1\n     }\n   }\n"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n         msg: \"\",\n         count: 2\n     },\n       data: [\n       {\n         description: \"1\",\n         format: \"PNG\",\n         createddatetime: \"2013-12-27, 02:19:09\",\n         userid: 1,\n         filename: \"python.png\",\n         updateddatetime: \"2013-12-27, 02:19:09\",\n         id: 1\n       },\n       {\n         description: \"2\",\n         format: \"PNG\",\n         createddatetime: \"2013-12-27, 02:19:10\",\n         userid: 1,\n         filename: \"python2.png\",\n         updateddatetime: \"2013-12-27, 02:19:10\",\n         id: 2\n       }\n     ]\n   }\n"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       format: \"PNG\",\n       createddatetime: \"2013-12-27, 02:19:09\",\n       userid: 1,\n       filename: \"python.png\",\n       updateddatetime: \"2013-12-27, 02:19:09\",\n       id: 1\n     }\n   }\n"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       format: \"PNG\",\n       createddatetime: \"2013-12-27, 02:19:09\",\n       userid: 1,\n       filename: \"python.png\",\n       updateddatetime: \"2013-12-27, 02:19:09\",\n       id: 1\n     }\n   }\n"
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
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n       msg: \"\"\n     },\n     data: {\n       description: \"1\",\n       createddatetime: \"2013-12-24, 02:54:24\",\n       userid: 1,\n       name: \"one\",\n       address: \"taipei\",\n       updateddatetime: \"2013-12-24, 02:54:24\",\n       id: 1,\n       longtitude: 121.5130475,\n       latitude: 25.040063\n     }\n   }\n"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n     info: {\n       status: true,\n         msg: \"\",\n         count: 3\n     },\n       data: [\n       {\n         description: \"1\",\n         createddatetime: \"2013-12-24, 02:54:24\",\n         userid: 1,\n         name: \"one\",\n         address: \"taipei\",\n         updateddatetime: \"2013-12-24, 02:54:24\",\n         id: 1,\n         longtitude: 121.5130475,\n         latitude: 25.040063\n       },\n       {\n         description: \"1\",\n         createddatetime: \"2013-12-24, 02:54:24\",\n         userid: 1,\n         name: \"one\",\n         address: \"taipei\",\n         updateddatetime: \"2013-12-24, 02:54:24\",\n         id: 2,\n         longtitude: 121.5130475,\n         latitude: 25.040063\n       },\n       {\n         description: \"1\",\n         createddatetime: \"2013-12-24, 02:54:24\",\n         userid: 1,\n         name: \"one\",\n         address: \"taipei\",\n         updateddatetime: \"2013-12-24, 02:54:24\",\n         id: 3,\n         longtitude: 121.5130475,\n         latitude: 25.040063\n       }\n     ]\n   }\n"
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
            "field": "longtitude",
            "optional": false,
            "description": "longtitude"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n       info: {\n           status: true,\n           msg: \"\"\n       },\n       data: {\n           description: \"dd\",\n           createddatetime: \"2013-12-24, 04:22:50\",\n           userid: 1,\n           name: \"nn\",\n           address: \"address\",\n           updateddatetime: \"2013-12-24, 04:22:50\",\n           id: 1,\n           longtitude: 121.5130475,\n           latitude: 25.040063\n       }\n   }\n"
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
            "field": "longtitude",
            "optional": false,
            "description": "longtitude"
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
          },
          {
            "group": "Parameter",
            "type": "Number",
            "field": "userid",
            "optional": false,
            "description": "userid"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Successful Response Body:",
          "content": "   HTTP/1.1 200 OK\n   {\n       info: {\n           status: true,\n           msg: \"\"\n       },\n       data: {\n           description: \"description\",\n           createddatetime: \"2013-12-24, 04:22:50\",\n           userid: 1,\n           name: \"name\",\n           address: \"address\",\n           updateddatetime: \"2013-12-24, 04:25:50\",\n           id: 1,\n           longtitude: 121.5130475,\n           latitude: 25.040063\n       }\n   }\n"
        }
      ]
    },
    "filename": "api/location.js"
  }
] });