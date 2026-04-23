def add_medical_record(patients):
    patient_id = input("Enter Patient ID: ")

    found_patient = None
    for patient in patients:
        if patient_id == patient.patient_id:
            found_patient = patient
            break

    if not found_patient:
        print("Patient not found.")
        return

    date = input("Enter Date (YYYY-MM-DD): ")
    diagnosis = input("Enter Diagnosis: ")
    treatment = input("Enter Treatment: ")
    doctor = input("Enter Doctor: ")

    record = {
        "date": date,
        "diagnosis": diagnosis,
        "treatment": treatment,
        "doctor": doctor
    }

    found_patient.medical_records.append(record)
    print(f"Medical record added successfully for Patient ID: {patient_id}")