import argparse
from auth0.authentication import GetToken
from auth0.management import Auth0

# Auth0 credentials
domain = 'dev-7c8su7i5v2l2uz0a.us.auth0.com'
client_id = 'ReBB1nUcySkXOo4N71nK54oWuiiVGIDQ'
client_secret = 'ao7hWIHt8fAurIAEDAfdBF0SqaajtKgkGtXbXu7EQhjByHIHEvLSJkTVA12J3RR_'

def get_access_token(domain, client_id, client_secret):
    get_token = GetToken(domain, client_id, client_secret=client_secret)
    token = get_token.client_credentials('https://{}/api/v2/'.format(domain))
    mgmt_api_token = token['access_token']
    return Auth0(domain, mgmt_api_token)

def list_users(auth0):
    return auth0.users.list()

def update_user(auth0, user_id, new_name):
    return auth0.users.update(user_id, {'name': new_name})

def delete_user(auth0, user_id):
    return auth0.users.delete(user_id)

def create_user(auth0, user_data):
    try:
        user = auth0.users.create(user_data)
        print("User created successfully:", user)
    except Exception as e:
        print("Failed to create user:", str(e))
        
def main():
    parser = argparse.ArgumentParser(description="Manage users.")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # List users
    list_parser = subparsers.add_parser('list', help='List all users')

    # Create user
    create_parser = subparsers.add_parser('create', help='create a new user')
    create_parser.add_argument('--email', required=True, help='email')
    create_parser.add_argument('--password', required=True, help='Password')
    create_parser.add_argument('--email_verified', type=bool, default=False, help='verification status')

    # Update user
    update_parser = subparsers.add_parser('update', help='update user')
    update_parser.add_argument('--user_id', required=True, help='user ID')
    update_parser.add_argument('--new_name', required=True, help='new name')

    # Delete user
    delete_parser = subparsers.add_parser('delete', help='delete a user')
    delete_parser.add_argument('--user_id', required=True, help='user ID to delete')
    
    
    args = parser.parse_args()
    auth0 = get_access_token(domain, client_id, client_secret)
    if args.command == 'list':
        users = list_users(auth0)
        print(users)
    elif args.command == 'create':
        user_data = {
            'connection': 'Username-Password-Authentication',
            'email': args.email,
            'password': args.password,
            'email_verified': args.email_verified
        }
        create_user(auth0, user_data)
    elif args.command == 'update':
        update_user(auth0, args.user_id, args.new_name)
    elif args.command == 'delete':
        delete_user(auth0, args.user_id)

if __name__ == "__main__":
    main()
