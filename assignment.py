class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment

    def __str__(self):
        return f"Record {self.record_id}: {self.diagnosis}, Treatment: {self.treatment}"


class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_record = None  # Composition

    def assign_medical_record(self, record_id, diagnosis, treatment):
        self.medical_record = MedicalRecord(record_id, diagnosis, treatment)

    def __str__(self):
        record_info = str(self.medical_record) if self.medical_record else "No medical record"
        return f"Patient {self.patient_id}: {self.name}, Age: {self.age}\n{record_info}"


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.patients = []  # Aggregation

    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)

    def __str__(self):
        patient_list = ", ".join([p.name for p in self.patients]) or "No assigned patients"
        return f"Doctor {self.doctor_id}: {self.name} ({self.specialization})\nPatients: {patient_list}"


class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []  # Composition

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def __str__(self):
        doctor_list = "\n".join([str(doc) for doc in self.doctors]) or "No doctors available"
        return f"Department: {self.name}\n{doctor_list}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []  # Composition

    def add_department(self, department):
        self.departments.append(department)

    def __str__(self):
        dept_list = "\n".join([str(dept) for dept in self.departments]) or "No departments available"
        return f"Hospital: {self.name}\n{dept_list}"


# Example Usage
if __name__ == "__main__":
    hospital = Hospital("City General Hospital")
    
    dept1 = Department("Cardiology")
    dept2 = Department("Neurology")
    
    doctor1 = Doctor(1, "Dr. Smith", "Cardiologist")
    doctor2 = Doctor(2, "Dr. Johnson", "Neurologist")
    
    patient1 = Patient(101, "Alice", 30)
    patient2 = Patient(102, "Bob", 45)
    
    patient1.assign_medical_record(1, "Heart Disease", "Medication and lifestyle change")
    doctor1.add_patient(patient1)
    doctor2.add_patient(patient2)
    
    dept1.add_doctor(doctor1)
    dept2.add_doctor(doctor2)
    
    hospital.add_department(dept1)
    hospital.add_department(dept2)
    
    print(hospital)
