# Control flow, loops, functions,classes
# list, dictionary
# modules
# Week 1-12
# import data as data

# Add initials, convert phone number into integer only

# Read the json file to get customer data:
with open('Assessment 3.json','r') as file:
    customer_data = file.read()
print(customer_data)

# Convert the customer data into a list
# Load the JSON data into a list of dictionaries
import json
customer_data_list = json.loads(customer_data)

# Print out all customer data
print(customer_data_list)

class Person:
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone


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


# Ask user if there is more people to add
more_people = True
while more_people:
    person = get_person_details()
    persons_list.append(person)

    choice = input("Do you want to add more people? Enter 1 to add more / Enter any others to pass")
    if choice.lower() != "1":
        more_people = False

# All the customer names:
customer_name = []
for customer_info in customer_data_list:
    name_list = customer_info['name']
    customer_name.append(name_list)

print(customer_name)


# Add initial to customer data:
def add_initials_to_customers(customers):
    for customer_info in customers:
        name = customer_info['name']
        name_split = name.split()
        initials = name_split[0][0] + name_split[-1][0]
        customer_info['initials'] = initials
    return customers

customer_data_list_with_initials = add_initials_to_customers(customer_data_list)
# Print the new alist after initials have been added:
print(customer_data_list_with_initials)

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

def convert_phone_string_to_number(customers):
    for customer in customers:
        original_phone_number = customer['phone']
        plain_phone_numbers = original_phone_number.replace('-','')
        try:
            plain_phone_numbers = int(plain_phone_numbers)
            customer['phone'] = plain_phone_numbers
        except ValueError as e:
            print(f'Error: Invalid phone number: {original_phone_number}')
            customer['phone'] = original_phone_number
    return customers


modified_data_list_with_plain_phone_numbers = convert_phone_string_to_number(customer_data_list_with_initials)
if modified_data_list_with_plain_phone_numbers is not None:
    print(modified_data_list_with_plain_phone_numbers)


# I will store the modified information into a new csv file
import csv

field_names = ['name', 'age', 'email', 'phone', 'initials']

with open('modified_data_Fang_Shi.csv','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=field_names)
    writer.writeheader()
    writer.writerows(modified_data_list_with_plain_phone_numbers)

print('New CSV file created successfully. It contains modified information.')