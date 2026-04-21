from patient import Patient

def add_patient(patients, patient_id, name, age, user_gender, contact_number):
    patient = Patient(patient_id, name, age, user_gender, contact_number)
    patients.append(patient)

def view_all_patients(patients):
    if not patients:
        print("Empty List")
    else:
        print("\n ====== PATIENTS =====")
        for patient in patients:
            print(patient)

def search_patient(patients, search):
    found = False
    for patient in patients:
        if search.lower() in patient.name.lower() or search in patient.patient_id:
            print(patient)
            found = True
    if not found:
        print("Not Found")

def update_patient(patients, update, name, age, gender, contact_number, choice_option):
    for index, patient in enumerate(patients):
        if update == patient.patient_id:
            if choice_option == 1:
                patients[index].name = name
            elif choice_option == 2:
                patients[index].age = age
            elif choice_option == 3:
                patients[index].gender = gender
            elif choice_option == 4:
                patients[index].contact_number = contact_number
            print(f"Patient: {patient.patient_id} updated info")

        
