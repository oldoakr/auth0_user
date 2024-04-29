from flask import Flask, jsonify
from flask import request
from auth0.authentication import GetToken
from auth0.management import Auth0

app = Flask(__name__)

# Auth0 credentials
domain = 'dev-7c8su7i5v2l2uz0a.us.auth0.com'
client_id = 'ReBB1nUcySkXOo4N71nK54oWuiiVGIDQ'
client_secret = 'ao7hWIHt8fAurIAEDAfdBF0SqaajtKgkGtXbXu7EQhjByHIHEvLSJkTVA12J3RR_'

get_token = GetToken(domain, client_id, client_secret=client_secret)
token = get_token.client_credentials('https://{}/api/v2/'.format(domain))
mgmt_api_token = token['access_token']
auth0 = Auth0(domain, mgmt_api_token)


@app.route('/users', methods=['GET'])
def get_users():
    users = auth0.users.list()
    return jsonify(users)

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    update_data = {'name': 'test_user'}
    try:
        updated_user = auth0.users.update(user_id, update_data)
        return jsonify(updated_user)
    except Exception as error:
        return jsonify({'error': error})

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        auth0.users.delete(user_id)
        return jsonify({'message': 'User deleted successfully'})
    except Exception as error:
        return jsonify({'error': error})


@app.route('/users', methods=['POST'])
def create_user():
    request_data = request.get_json()
    user_data = {
        'connection': 'Username-Password-Authentication',
        'email': 'testuser2@something.com',
        'password': 'Sample@12345',
        'email_verified': False
    }
    user_data.update(request_data)
    try:
        created_user = auth0.users.create(user_data)
        return jsonify(created_user)
    except Exception as error:
        return jsonify({'error': error})

if __name__ == '__main__':
    app.run(debug=False, port=3000)
