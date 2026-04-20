from patient import Patient

def add_patient(patients, patient_id, name, age, user_gender, contact_number):
    patient = Patient(patient_id, name, age, user_gender, contact_number)
    patients.append(patient)

