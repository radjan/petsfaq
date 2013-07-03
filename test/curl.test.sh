
# create new hospital
curl -v -H "Content-Type: application/json" -X POST --data '{"name":"TEST_Hospital", "description":"test", "specialty":"save pets life", "address":"no 125 kr road", "phone":"3939889", "emergency":true}' http://localhost:8080/api/v1/hospital

echo "create a hospital ------------ \n"
curl -H "Content-Type: application/json" -X POST --data '{"name":"hospital for pets 2", "description":"test test", "specialty":"save pets life", "address":"no 125 kr road", "phone":"3939889", "emergency":true}' http://localhost:8080/api/v1/hospital

echo "create a person -------------- \n"
curl -H "Content-Type: application/json" -X POST --data '{"name":"Yun-Tai 001", "email":"test@test.com", "gender":"F", "phone":"3939889"}' http://localhost:8080/api/v1/person

echo "list all hospital ------------ \n"
curl  -X GET http://localhost:8080/api/v1/hospital
echo "list all account ------------ \n"
curl  -X GET http://localhost:8080/api/v1/account
echo "list all role ------------ \n"
curl  -X GET http://localhost:8080/api/v1/role
echo "list all person ------------ \n"
curl  -X GET http://localhost:8080/api/v1/person


# test PUT to edit blogpost attribute(escape for zsh)
#curl -X PUT -i -d '{ "abcde": "666", "publish" : 1  }' http://127.0.0.1:8080/api/v1/post/4573968371548160\?publish\=0
