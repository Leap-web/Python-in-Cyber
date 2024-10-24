print("Group2")
print("Member Team 10: Thay Bunleap and Pheng Manyta")

# Exercise 1
print("\nExercise I")

print("\nPart 1")
for i in range(5):
    print("Number: ", i+1)

print("\nPart2")
i = 0
while i<6:
    print("Count: ", i+1)
    if i == 7:
        break
    i +=1


print("\nPart 3")
i = 2
while i <= 11 :
    if i == 4:
        i+=1
        continue
    print("Count: ", i)
    i+=1

# Exercise 2
print("\nExercise II")

favorite_list = ['blueberry', 'avocado', 'kiwi', 'strawberry']
print("\nGood fruits = ", favorite_list)
favorite_list.append('passion')
print("\nUpdated fruits after add: ", favorite_list)
favorite_list.remove('kiwi')
print("\nUpdated fruits after remove: ",favorite_list)
favorite_list.sort()
print("\nFruits sorted: ", favorite_list)


# Exercise 3
print("\nExercise III")

print("\nExercise 1")
tuple = (1, 2, 3, 4, 5)
print("Integer Tuple: ", tuple)

# tuple[0] = 10

print("\nExercise 3")
convert = list(tuple)
print("Converted List: ", convert)

# Exercise 4
print("\nExercise IV")

dictionary = {"Alice": 30,  "Bob": 25, "Charlie": 35}
print("Ages: ", dictionary)
dictionary["Leap"] = 35
print("Updated Age: ", dictionary)
dictionary.pop("Bob")
print("Updated Ages after removing Bob: ", dictionary)
for i in dictionary:
    print(i, dictionary[i])

# Exercise 5
print("\nExercise V")   

def add(a, b):
    return a + b
print("Result of add(3, 5):  ", add(3, 5))

def greet():
    return 'Hello, World!'
print(greet())

x = lambda a: a**2
print("Square of 5: ",x(5))


# Bonus 
print("\nBonus")
import sys
import os

users = []
passwords = {}
def register():
    user_name = input("Enter a username to register:  ")
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long")
        elif ( not any (c.isupper() for c in password)):
            print("Password must have at least one uppercase letter")
        elif (not any (c.isdigit() for c in password)):
            print("Password must have at least one digit")
        elif all(c not in '!@#$%^&*()' for c in password):
            print("Password must have at least one special character")
        else:
            print("Registration successful with a strong password!")
            users.append(user_name)
            passwords[user_name] = password
            break
def login():
    attempts = 0
    user_name = input("Enter your username: ")
    while True:
        if (user_name in users):
            password = input("Enter your password: ")
            if passwords[user_name] == password:
                print("Login successful!")
                break
            else:
                attempts += 1
                if attempts <3:
                    print("Invalid credentials. You have", 3-attempts, "attempts left.")
                else:
                        print("Invalid credentials. You have 0 attempts left.")
                        print("Too many failed attempts. Access blocked.")
                        break
        else:
            print("User not found")
            break

def forget_pw():
    user_name = input("Enter your username to retrieve your password: ")
    if user_name in users:
        print("Your password is: ", passwords[user_name])
    else:
        print("User not found")

def exit():
    print("Exiting the system...")
    sys.exit()

def main():
    while True:
        while True:
            print("""
                                            ///////////////////////////////////////////////////////////
                                            |========/ Welcome To User Authentication System /=========|
                                            ...........................................................
            1. Register                   
            2. Login
            3. Forget Password
            4. Exit
                """)


            try:
                user_input = int(input("Choose an option (1-4): ")) 
                if (user_input == 1):
                    os.system('cls')
                    register()
                elif (user_input == 2):
                    os.system('cls')
                    login()
                elif (user_input == 3):
                    os.system('cls')
                    forget_pw()
                elif (user_input == 4):
                    os.system('cls')
                    exit()
                    break
                else:
                    print("\nEnter a valid number, please!")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    main()