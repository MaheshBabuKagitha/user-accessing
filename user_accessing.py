#access user with user ID & Password,hiding password while user entering

#getpass keyword will hide user input data
import getpass
#user data to verify
existed_data={"user ID":"Python123","user password":"HelloWorld"}
#ask user to enter userID
user_name=input("Enter User ID : ")
#ask user to enter password
user_password=getpass.getpass("Enter password(Hidden) : ")
#if userID matches
if user_name == existed_data["user ID"]:
    #if userID & password matches
    if user_password==existed_data["user password"]:
        print("Login Successfull")
    #if userID matches & password missmatches
    else:
        print("incorrect password")
#if userID missmatches
else:
    print("incorrect user ID")