# Control flow, loops, functions,classes
# list, dictionary
# modules
# Week 1-12
# import data as data

# Add initials, convert phone number into integer only

import csv
import json
from person import Person

# Read the json file to get customer data:
with open('Assessment 3.json','r') as file:
    customer_data = file.read()
customer_data_list = json.loads(customer_data)
print(customer_data_list)


# Create an empty list to store Person objects
persons_list = []

# Iterate over the list of dictionaries
for person_dict in customer_data_list:
    # Extract the values from the dictionary
    name = person_dict['name']
    age = person_dict['age']
    email = person_dict['email']
    phone = person_dict['phone']

    # Create a Person object and append it to the list
    person = Person(name, age, email, phone)
    persons_list.append(person)

# Print all Person objects
for person in persons_list:
    print(person.name, person.age, person.email, person.phone)

# Function to get user input for a new person
def get_person_details():
    name = input("Enter the person's name: ")
    age = int(input("Enter the person's age: "))

    email = input("Enter the person's email: ")
    phone = input("Enter the person's phone number: ")
    return Person(name, age, email, phone)


more_people = True
while more_people:
    choice = input("Do you want to add more people? Enter 1 to add more / Enter any others to pass")
    if choice == "1":
        person = get_person_details()
        persons_list.append(person)
    else:
        more_people = False

# Add initial to customer data:
def add_initials_to_customers(customers):
    for customer_object in customers:
        name = customer_object.name
        name_split = name.split()
        initials = name_split[0][0] + name_split[-1][0]
        customer_object.initials = initials
    return customers

customer_data_list_with_initials = add_initials_to_customers(persons_list)


# Remove the'-' in phone numbers
# def remove_hyphen_in_phone_number(customers):
#     try:
#         for customer in customers:
#             phone_numbers = customer['phone']
#             plain_phone_numbers = phone_numbers.replace('-','')
#             plain_phone_numbers = int(plain_phone_numbers)
#             customer['phone'] = plain_phone_numbers
#         return customers
#     except ValueError as e:
#         print('Error: Invalid phone number format')
#         return None

# def convert_phone_string_to_number(customers):
#     for customer in customers:
#         original_phone_number = customer['phone']
#         plain_phone_numbers = original_phone_number.replace('-','')
#         try:
#             plain_phone_numbers = int(plain_phone_numbers)
#             customer['phone'] = plain_phone_numbers
#         except ValueError as e:
#             print(f'Error: Invalid phone number: {original_phone_number}')
#             customer['phone'] = original_phone_number
#     return customers


# modified_data_list_with_plain_phone_numbers = convert_phone_string_to_number(customer_data_list_with_initials)
# if modified_data_list_with_plain_phone_numbers is not None:
#     print(modified_data_list_with_plain_phone_numbers)



# Store the modified information into a new csv file



for person in customer_data_list_with_initials:
    modified_information = (f"name : {person.name}, "
                           f"age : {person.age}, "
                           f"email : {person.email}, "
                           f"phone : {person.phone}, "
                           f"initials : {person.initials}")

# Write objects to the CSV file, which is called 'modified_data_Fang_Shi.csv'
with open('modified_data_Fang_Shi.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['name', 'age', 'email', 'phone', 'initials'])

    for person in customer_data_list_with_initials:
        writer.writerow([person.name, person.age, person.email, person.phone, person.initials])

print('New CSV file created successfully. It contains modified information.')
