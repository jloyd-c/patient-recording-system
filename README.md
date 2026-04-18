# 🏥 Patient Record System

A modular CLI application built with Python using Object-Oriented Programming (OOP) principles.

---

## 📁 Project Structure

```
patient-record-system/
│
├── main.py        # Main loop and menu
├── patient.py     # Patient class
├── records.py     # Medical records
├── utils.py       # Helper functions
└── data.json      # Database
```

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📚 What I Learned

- Object-Oriented Programming (OOP)
- File handling with JSON
- Modular Python project structure
- CLI application design

---

## 🛠️ Sprint Plan

### Sprint 1 — Patient Model (OOP)
**Description**
Create the Patient class using OOP principles.

**Acceptance Criteria**
- Patient class exists in patient.py
- Has `__init__` method with attributes: `patient_id`, `name`, `age`, `gender`, `contact_number`, `medical_records`
- Has `__str__` method that displays patient info cleanly
- `medical_records` starts as an empty list

---

### Sprint 2 — Add Patient
**Description**
Allow the user to add a new patient via CLI input.

**Acceptance Criteria**
- Has `add_patient()` function in main.py or utils.py
- Prompts for `patient_id`, `name`, `age`, `gender`, `contact_number`
- Adds a new Patient object to a list
- Shows a confirmation message after adding

---

### Sprint 3 — View All Patients
**Description**
Display all patients currently stored in the system.

**Acceptance Criteria**
- Has `view_all_patients()` function
- Displays all patient info in a clean format
- Shows a message when no patients exist yet

---

### Sprint 4 — Search Patient
**Description**
Search for a specific patient by ID or name.

**Acceptance Criteria**
- Has `search_patient()` function
- Can search by `patient_id` or `name`
- Displays patient info when found
- Shows a message when not found

---

### Sprint 5 — Update Patient Info
**Description**
Allow the user to update an existing patient's information.

**Acceptance Criteria**
- Has `update_patient()` function
- Finds patient by `patient_id`
- Can update `name`, `age`, `gender`, or `contact_number`
- Shows a confirmation message after updating

---

### Sprint 6 — Delete Patient
**Description**
Remove a patient record from the system.

**Acceptance Criteria**
- Has `delete_patient()` function
- Finds patient by `patient_id`
- Shows a confirmation prompt before deleting
- Shows a confirmation message after deleting

---

### Sprint 7 — Add Medical Record
**Description**
Add a medical record entry to a specific patient.

**Acceptance Criteria**
- Has `add_medical_record()` function in records.py
- Finds patient by `patient_id`
- Prompts for `date`, `diagnosis`, `treatment`, `doctor`
- Adds the record to the patient's `medical_records` list

---

### Sprint 8 — View Medical History
**Description**
Display all medical records of a specific patient.

**Acceptance Criteria**
- Has `view_medical_history()` function
- Finds patient by `patient_id`
- Displays all medical records in a clean format
- Shows a message when the patient has no records yet

---

### Sprint 9 — Save and Load Data
**Description**
Persist all patient data using a JSON file.

**Acceptance Criteria**
- Has `save_data()` and `load_data()` functions in utils.py
- Data is saved to `data.json`
- Data is loaded when the program starts
- Data is not lost after closing the program

---

### Sprint 10 — Summary Report
**Description**
Display a summary report of all patients in the system.

**Acceptance Criteria**
- Has `summary_report()` function
- Shows total number of patients
- Shows total number of medical records
- Shows a breakdown by gender

---

## 👨‍💻 Author

Built by [Your Name] as a Python learning project.
