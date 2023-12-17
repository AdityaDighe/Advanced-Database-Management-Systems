import json

file_path = "data.json"


with open(file_path, 'r') as file:
    data = json.load(file)

if "users" in data:
    user_data = data["users"]

    for user_id,user_info in user_data.items():
        print(f"User ID: {user_id}")
        print(f"Name: {user_info['name']}")
        print(f"Email: {user_info['email']}")
        print(f"Phone: {user_info['phone']}")

        # Display address details
        address = user_info.get('address', {})
        print("Address:")
        print(f"  Street: {address['area']}")
        print(f"  City: {address['city']}")
        print(f"  ZIP: {address['zip']}")
        print("")
    
else:
    print('no user found')


