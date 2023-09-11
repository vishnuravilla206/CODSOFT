#initializing the program by importing random
import random
import string
#user defining the length of the password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password=''.join(random.choice(characters) for _ in range(length))
    return password
#response to the users input 
def main():
    try:
        length = int (input("enter the desired password length :"))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
        #if length of password is less than 8 user is aked to give the input again
        password = generate_password(length)
        print("Generate Password:" , password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__=="__main__":
    main()

