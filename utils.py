import json
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

def delete_patient(patients, delete_patients, delete_confirmation):
    for index, patient in enumerate(patients):
        if delete_patients == patient.patient_id:
            if delete_confirmation == 1:
                patients.pop(index)
                print("Patient record deleted")
            elif delete_confirmation == 2:
                print("Canceled delete patient record")
                break

def view_medical_history(patients, patient_id):
    found = False

    for patient in patients:
        if patient.patient_id == patient_id:
            found = True
            print(f"\n=== Medical History of {patient.name} ===")

            if not patient.medical_records:
                print("No medical records yet.")
            else:
                for index, record in enumerate(patient.medical_records, start=1):
                    print(f"\nRecord #{index}")
                    print(f"Date      : {record['date']}")
                    print(f"Diagnosis : {record['diagnosis']}")
                    print(f"Treatment : {record['treatment']}")
                    print(f"Doctor    : {record['doctor']}")

            break

    if not found:
        print("Patient not found.")

def save_data(patients):
    data = []
    for patient in patients:
        data.append({
            "patient_id": patient.patient_id,
            "name": patient.name,
            "age": patient.age,
            "gender": patient.gender,
            "contact_number": patient.contact_number,
            "medical_records": patient.medical_records
        })
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        patients = []
        
        for entry in data:
            patient = Patient(
                entry["patient_id"],
                entry["name"],
                entry["age"],
                entry["gender"],
                entry["contact_number"]
            )
            patient.medical_records = entry.get("medical_records", [])
            patients.append(patient)
        return patients
    except FileNotFoundError:
        return []