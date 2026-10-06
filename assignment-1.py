# Section 1: Variables and Types

name = "Og'abek"
age = 22
height = 5.7
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# Section 2: User Input and Math

user_name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

current_year = 2026
user_age = current_year - birth_year

print(f"Hi, {user_name}! You are approximately {user_age} years old.")


# Section 3: Type Conversion and f-strings

number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

product = number1 * number2

print(f"{number1} × {number2} = {product}")


# Section 4: Formatted Receipt

item = "Laptop"
price = 800
quantity = 2

total = price * quantity

print("===========================")
print("        RECEIPT")
print("===========================")
print(f"Item:      {item}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")


# Section 5: Mini-Project - Profile Card

profile_name = input("What is your name? ")
hometown = input("Where are you from? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Tell me one fun fact about yourself: ")
profile_birth_year = int(input("What year were you born? "))

profile_age = current_year - profile_birth_year

print()
print("╔══════════════════════════════╗")
print(f"      PROFILE: {profile_name}")
print("╚══════════════════════════════╝")
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {profile_age}")
