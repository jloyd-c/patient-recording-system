from patient import Patient
from utils import add_patient, view_all_patients, search_patient, update_patient

patients = []

def gender():
     print("1. Male")
     print("2. Female")

def menu():
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patients")
    print("4. Update Patients")
    print("5. Exit")

def update_choices():
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Gender")
    print("4. Update Contact Number")

while True:
    menu()
    try:
        user_input = int(input("Choose an Options: "))
    except ValueError:
        print("Invalid Input Please Enter Number!")
        continue

    if user_input == 1:
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            try:
                age = int(input("Enter Patient Age: "))
            except ValueError:
                print("Invalid Input Please Enter Number!")
                continue
            gender()
            try:
                user_gender = int(input("Choose Gender: "))
            except ValueError:
                print("Invalid Input Please Enter Number!")
                continue
            if user_gender == 1:
                 user_gender = "Male"
            elif user_gender == 2:
                 user_gender = "Female"
            try:
                contact_number = int(input("Enter Patient Contact Number: "))
            except ValueError:
                print("Invalid Input Please Enter Number!")
                continue

            add_patient(patients, patient_id, name, age, user_gender, contact_number)
            print("Patient added successfully!")
    
    elif user_input == 2:
        view_all_patients(patients)
    
    elif user_input == 3:
        search = input("Enter name or patient ID: ")
        search_patient(patients, search)

    elif user_input == 4:
        view_all_patients(patients)
        if len(patients) == 0:
             continue
        update = input("Enter Patient ID: ")
        update_choices()
        choice_option = int(input("Enter Update Choices: "))
        if choice_option == 1:
            name = input("Enter Patient Name: ")
        elif choice_option == 2:
            try:
                age = int(input("Enter Patient Age: "))
            except ValueError:
                    print("Invalid Input Please Enter Number!")
                    continue
        elif choice_option == 3:
            gender()
            try:
                user_gender = int(input("Choose Gender: "))
            except ValueError:
                    print("Invalid Input Please Enter Number!")
                    continue
            if user_gender == 1:
                    user_gender = "Male"
            elif user_gender == 2:
                    user_gender = "Female"
        elif choice_option == 4:
            try:
                contact_number = int(input("Enter Patient Contact Number: "))
            except ValueError:
                    print("Invalid Input Please Enter Number!")
                    continue
        update_patient(patients, update, name, age, user_gender, contact_number, choice_option)

    elif user_input == 5:
        print("Goodbye!")
        break