
password = "123123"
authorised = False

while authorised != True:
    user_input = input("please enter your password : ")
    if user_input == password:
        print("accses granted")
    authorised = True
else: 
      print("password incorrect pls try again")

















