
# create new hospital
curl -v -H "Content-Type: application/json" -X PUT --data '{"name":"hospital for save life", "description":"test", "specialty":"save pets life", "address":"no 125 kr road", "phone":"3939889", "emergency":true}' http://localhost:9080/api/v1/hospital
