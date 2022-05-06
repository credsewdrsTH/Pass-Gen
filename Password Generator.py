#import
import random

#welcome
print("* * * * Password Generator * * * *")

#Database of characters
Data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"

#function
def main():
    #fix bug code
    try:
        #main
        password_len = int(input("What length would you like your password to be : "))
        password_count = int(input("How many passwords would you like : "))
        for x in range(0,password_count):
            password  = ""
            for x in range(0,password_len):
                password_char = random.choice(Data)
                password      = password + password_char
            print("Here is your password : ", password)
    #fix bug code        
    except:
        print("something went wrong")

    Repeat = input("Would you like to use it again ")
    if Repeat == "yes":
        main()
    else:
        print("Bye")
        exit()
main()
#end