userpassword =  int (input("Enter your passsword..."))
retry_number = 1

print("---")
while userpassword != 1990:
    print("Invalid password. Try again...")
    userpassword = int (input("Password: "))
    retry_number +=1 
print("Password is accepted...")
print("Retry number is ", retry_number)
1990

print("---")

retry_number = 0
while True:
    userpassword = int (input ("Enter your password..."))
    retry_number += 1
    if userpassword == 1990:
        print("Password is accepted...")
        break
    else:
        print("Password is not correct. Try again...")

print("Retry number is ", retry_number)

print("---")      

retry_number = 0
while True:
    userpassword = input ("Enter your password...")
    retry_number += 1
    if  not userpassword.isnumeric():
        print("Type is invalid...")
        continue
    if int (userpassword)== 1990:
        print("Password is accepted...")
        break
    else:
        print("Password is not correct. Try again...")
print("Retry number is ", retry_number)

print("---")      




