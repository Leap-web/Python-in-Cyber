# Exercise 1


print("Exercise 1")
n = int(input('Enter first number: '))
y = int(input('Enter second number: '))

# Addition
addition = n + y
print('Sum:', addition)

# Subtraction
subtraction = n - y
print('Difference: ', subtraction)

# multiplication
multiplication = n * y
print('Product: ', multiplication)

# Division
division = n/y
print('Quotient: ', division)


# Exercise 2

print("\nExercise 2")

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))

if x > y and x > z:
    print('The largest number is ', x)
elif y > x and y > z:
    print('The largest number is ', y)
elif x == y == z:
    print('All numbers are equal')
else:
    print('The largest number is ', z)


# Exercise 3

print("\nExercise 3")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Exercise 4

print("\nExercise 4")
n = int(input('Enter a number: '))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print('Factorial of', n, 'is', fact)



# Exercise 5 

print("\nExercise 5")
s = input("Enter a string: ")

reverse_s = s[::-1] # we use slicing [::] it meant we don't need to specifying the starting and ending points 
if( s == reverse_s ):
    print(s, "is a palindrome.")
else:
    print(s,"is not a palindrome")


# Bonus 
# password strength checker 

print("\nBonus Exercise")
pw = input("Enter a password to check its strength: ")

# Check length
if len(pw) < 8:
    print("Password strength: Weak")
    print("Enter uppercase, lowercase, digits and any special characters for strong passwords")
elif (
    not any(c.isupper() for c in pw) # check uppercase letters
    or not any(c.islower() for c in pw) # check lowercase letters
    or not any(c.isdigit() for c in pw)  # check digits
    or all(c not in '!@#$%^&*()' for c in pw) # check special characters
):
    print("Password strength: Moderate")
    print("Enter uppercase, lowercase, digits and any special characters for strong passwords")
else:
    print("Password strength: Strong")