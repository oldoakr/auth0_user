# from flask import Flask, request, jsonify
# import requests
from auth0.authentication import GetToken
from auth0.management import Auth0

#app = Flask(__name__)
# Auth0 credentials
domain = 'dev-7c8su7i5v2l2uz0a.us.auth0.com'
API_IDENTIFIER = 'https://dev-7c8su7i5v2l2uz0a.us.auth0.com/api/v2/'
client_id = 'ReBB1nUcySkXOo4N71nK54oWuiiVGIDQ'
client_secret = 'ao7hWIHt8fAurIAEDAfdBF0SqaajtKgkGtXbXu7EQhjByHIHEvLSJkTVA12J3RR_'



# domain = 'mydomain.auth0.com'
# client_id = 'myclientid'
# client_secret = 'myclientsecret'

get_token = GetToken(domain, client_id, client_secret=client_secret)
token = get_token.client_credentials('https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']
auth0 = Auth0(domain, token['access_token'])

auth0 = Auth0(domain, mgmt_api_token)

# read user 

users = auth0.users.list()
print(users)

# update user 

user_id = "auth0|662ebb7ee8cb006d963886f8"
auth0.users.update(user_id, {
    'name': 'test_user'
})

# delete user 

delete_user = auth0.users.delete(
    "auth0|662eacd7679968521daa2578"
)

# create user 

user_data = {
    'connection': 'Username-Password-Authentication',
    'email': 'testuser@something.com',
    'password': 'Sample@1234',
    'email_verified': False
}
try:
    user = auth0.users.create(user_data)
    print("User created successfully:", user)
except Exception as e:
    print("Failed to create user:", str(e))
users = auth0.users.list()
print(users)


