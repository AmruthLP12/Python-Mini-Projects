import json

def add_person():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    person = {"name": name, "age": age, "email": email}
    return person


def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])


def delete_person(people):
    display_people(people)

    while True:

        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 and number > len(people):
                print("Invalid Number!,or out of range")
            else:
                break
        except:
            print("Invalid Number!")

    people.pop(number - 1)
    print("Person deleted successfully!")
    display_people(people)


def search_person(people):
    search_name = input("Enter the name you want to search: ")
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_people(results)


print("Hi, Welcome to Contact Management System !")
print()

with open("contacts.json", "r") as file:
    people = json.load(file)["contacts"]

while True:
    print("Contact List size:", len(people))
    commend = input("You can 'add','Delete',or 'search' and 'Q' to quit: ").lower()
    if commend == "add":
        person = add_person()
        people.append(person)
        print("Person added successfully!")
    elif commend == "delete":
        delete_person(people)
    elif commend == "search":
        search_person(people)
    elif commend == "q":
        break
    else:
        print("Invalid Input!")
        
with open("contacts.json", "w") as file:
    json.dump({"contacts": people}, file)
