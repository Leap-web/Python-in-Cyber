# Thay_Bunleap W02
# Exercise 1
print("\nExercise 1")

def reverse_function(list):
    print(list[::-1])
reverse_function([1, 2, 3, 4, 5])


# Exercise 2
print("\nExercise 2")

List = [i*i for i in range (2, 21) if i%2 == 0]
print(List)


# Exercise 3
print("\nExercise 3")

def list(list1, list2):
    return list1 + [i for i in list2 if i not in list1]
list1 = [1, 2, 3]
list2 = [2, 3, 4, 5]
print(list(list1, list2))


# Exercise 4
print("\nExercise 4")

def max_min(tuple):
    return max(tuple), min(tuple)
max_min_tuple = (10, 5, 8, 12, 3)
print(max_min(max_min_tuple))


# Exercise 5 
print("\nExercise 5")

x = ("Phnom Penh",  "Siem Reap", "Battambang")
y = (11.5564, 13.3622,  13.0957)
z = (104.9282, 103.8597, 103.2022)

t = zip(x, y, z)
for (x, y, z) in t:
    print(f"City: {x}, Latitude: {y}, Longitude: {z}")


# Exercise 6 
print("\nExercise 6")

double_value = lambda x: {key: value *2 for key, value in x.items()}
x = {1:10, 2:20, 3:30, 4:40}
print(double_value(x))


# Exercise 7
print("\nExercise 7")

def count(str):
    return {key : str.count(key) for key in dictionary}
dictionary = "hello"
print(count(dictionary))

# Exercise 8
print("\nExercise 8")

def merge_dicts(dic1, dic2):
    dic3 = dic1.copy()
    dic3.update(dic2)
    for key in dic2:
        if key in dic1:
            dic3[key] = dic2[key] + dic1[key]
    return dic3
dic1 = {'a':1, 'b':3}
dic2 = {'b':2, 'c':4}
print(merge_dicts(dic1, dic2))


# Bonus
print("\nBonus")
import os

users = []
statuses = {}

def add_user():
    while True:
        user_name = input("\nEnter your name: ")
        email = input("\nEnter your email (must be a Gmail): ")
        
        if ("@" in email and email.endswith("@gmail.com")):
            users.append((user_name, email))
            statuses[user_name] = "active"
            print(f"\nUser '{user_name}' added successfully.")
            return
        else:
            print("\nPlease enter a correct Gmail address.")

def update_status():
    while True:
        user_name = input("\nEnter the username to update status: ")
        if (user_name in statuses):
            new_status = input("\nEnter new status (active or suspended): ").lower()
            if (new_status in ["active", "suspended"]):
                statuses[user_name] = new_status
                print(f"\nUser '{user_name}' status updated to '{new_status}'.")
                return
            else:
                print("\nPlease enter a valid status (active or suspended).")
        else:
            print("\nUser not found.")
        
def remove_user():
    remove = input("\nEnter a user to remove: ")
    for user_name, email in users:
        if (user_name == remove):
            users.remove((user_name, email))
            del statuses[user_name]
            print(f"\nUser '{user_name}' removed successfully.")
            return
    print("\nUser not found.")
    
def display_all():
    if (not users):
        print("\nNo users found.")
    else:
        print("\nCurrent user accounts:")
        print("------------------------------------------------------------")
        for user_name, email in users:
            status = statuses.get(user_name, "unknown")
            user_info = {
                "Username": user_name,
                "Email": email,
                "Status": status
            }
            print(user_info)
            
        # Count active users and print the total
        active_count = sum(1 for status in statuses.values() if status == "active")
        print("------------------------------------------------------------------")
        print(f"\nTotal active users: {active_count}")

def count_status():
    active_count = sum(status == "active" for status in statuses.values())
    suspended_count = sum(1 for status in statuses.values() if status == "suspended")
    print(f"\nActive users: {active_count}, Suspended users: {suspended_count}")

def main_menu():
    while True:
        print("""

                                        >>>-------------------------------------------------<<<
                                        |========/ Welcome To Data Management System /=========|
                                        <<<-------------------------------------------------->>>

        1. Add User
        2. Update User Status
        3. Remove User
        4. Display All Users
        5. Count User Status
        6. Exit

            """)


        try:
            user_input = int(input("Select an option to work on: ")) 
            if (user_input == 1):
                os.system('cls')
                print("\n|-----------------------@-Add User to Our Data Management System-@-----------------------|")
                add_user()
            elif (user_input == 2):
                os.system('cls')
                print("\n|------------------##-Update User Status To Our Data Management System-##------------------|")
                update_status()
            elif (user_input == 3):
                os.system('cls')
                print("\n|------------------**-Remove User From Our Data Management System-**------------------|")
                remove_user()
            elif (user_input == 4):
                os.system('cls')
                print("""\n                    |========================================================================|
                    |------------------------ Data Management System ------------------------|
                    |========================================================================|
                """)
                display_all()
                break
            elif (user_input == 5):
                os.system('cls')
                count_status()
            elif (user_input == 6):
                os.system('cls')
                print("\nExiting the system...")
                break
            else:
                print("\nEnter a valid number, please!")
        except ValueError:
            print("\nInvalid input. Please enter a number.")


if __name__ == "__main__":
    main_menu()