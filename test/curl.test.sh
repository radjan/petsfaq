
# create new hospital
curl -v -H "Content-Type: application/json" -X PUT --data '{"name":"TEST_Hospital", "description":"test", "specialty":"save pets life", "address":"no 125 kr road", "phone":"3939889", "emergency":true}' http://localhost:9080/api/v1/hospital

curl -v -H "Content-Type: application/json" -X PUT --data '{"name":"hospital for pets", "description":"test test", "specialty":"save pets life", "address":"no 125 kr road", "phone":"3939889", "emergency":true}' http://localhost:9080/api/v1/hospital

curl -v -X GET http://localhost:9080/api/v1/hospital
