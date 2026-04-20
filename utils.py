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