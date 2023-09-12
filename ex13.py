user_info = {
    "1" : {
            'Name' : "Manish",
            'Age' : "20"
        },
    "2" : {
            'Name' : "Harish",
            'Age' : "21"
        },
    "3" : {
            'Name' : "Nitin",
            'Age' : "17"
        }
}
search_id = input("Enter the User ID to retrieve details: ")
if search_id in user_info:
    user_details = user_info[search_id]
    print(f"User ID: {search_id}")
    print(f"User Name: {user_details['Name']}")
    print(f"User Age: {user_details['Age']}")
else:
    print("User ID not found.")

