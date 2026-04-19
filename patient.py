class Patient:
    def __init__(self,patient_id, name, age, gender, contact_number):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.medical_records = []

    def __str__(self):
        return f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Contact Number: {self.contact_number} "