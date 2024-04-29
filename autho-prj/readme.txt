1. Running directly from the console with function calls:

commands to use:
list the users   - python3 cmd-line.ppy list
create the user  - python3 cmd-line.ppy create --email exmp_user@test.com --password "yourpassword" --email_verified True
update the user  - python3 cmd-line.ppy update --user_id "auth0|123456" --new_name "New Name"
                   note* - please add auth0| before the user id example "auth0|<user_id>"
delete user      - python3 cmd-line.ppy delete --user_id "auth0|123456"


2. Rest api method:

curl commands to use:
run the code = python3 flask-auth.py
list the user - 
curl http://127.0.0.1:3000/users

create the user - 
curl -X POST http://127.0.0.1:3000/users -d '{"connection": "Username-Password-Authentication", "email": "testuser2@something.com", "password": "Sample@1234", "email_verified": false}' -H "Content-Type: application/json"

delete the user -
curl -X DELETE http://127.0.0.1:3000/users/<user_id>

update the user - 
curl -X PUT http://127.0.0.1:3000/users/<user_id> -d '{"name": "test_user"}' -H "Content-Type: application/json"

note*= for <user_id> use "auth0|123456"

3. Docker and kubernates:

  - build the docker images using:
    > docker build -t <any-name-for-the-image> .
  - deploy using docker command :
    > docker run -p 3000:3000 <name of the built image>
  - repeat the same steps from step 2 to verify 
  - Kubernates deployment 
    > cd Kubernates-maninfest
    > kubectl apply -f user-auth-k8s.yaml
    note* - update the docker image in the k8s mainfest file 
  - you can test the service by using the loadbalancer service endpoint 
    repeat step 2 by update the localhost with loadbalancer end point
  - command to get the service endpoint 
    > kubectl get svc 


    


    
  