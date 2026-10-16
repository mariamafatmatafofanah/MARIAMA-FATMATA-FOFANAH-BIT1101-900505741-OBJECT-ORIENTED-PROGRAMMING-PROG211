# ==========================================
# PATIENT RECORD SYSTEM
# Object-Oriented Programming Assignment
# ==========================================


class Patient:
    # Class variable
    system_name = "Patient Record System"

    # Constructor
    def __init__(self, patient_id, name, age, gender, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition

    # Instance method
    def update_condition(self, new_condition):
        self.condition = new_condition
        print(f"{self.name}'s condition has been updated.")

    # Instance method
    def display_info(self):
        print("--------------------------------")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Condition:", self.condition)

    # Class method
    @classmethod
    def create_patient(cls, patient_id, name, age, gender, condition):
        return cls(patient_id, name, age, gender, condition)

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18


class HealthRecord:
    # Constructor
    def __init__(self, record_id, patient, doctor, treatment):
        self.record_id = record_id
        self.patient = patient
        self.doctor = doctor
        self.treatment = treatment

    # Instance method
    def display_record(self):
        print("--------------------------------")
        print("Health Record ID:", self.record_id)
        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor)
        print("Treatment:", self.treatment)

    # Instance method showing interaction between objects
    def update_patient_condition(self, new_condition):
        self.patient.update_condition(new_condition)
        print("Health record updated successfully.")


# ==========================================
# MAIN PROGRAM
# ==========================================

# List used to store multiple Patient objects
patients = []

# Creating Patient objects using the class method
patient1 = Patient.create_patient(
    "P001",
    "John Kamara",
    25,
    "Male",
    "Malaria"
)

patient2 = Patient.create_patient(
    "P002",
    "Mary Bangura",
    32,
    "Female",
    "Hypertension"
)

patient3 = Patient.create_patient(
    "P003",
    "Mohamed Sesay",
    17,
    "Male",
    "Fever"
)

# Add patient objects to the list
patients.append(patient1)
patients.append(patient2)
patients.append(patient3)


# ==========================================
# DISPLAY ALL PATIENTS
# ==========================================

print("========================================")
print("       PATIENT RECORD SYSTEM")
print("========================================")

for patient in patients:
    patient.display_info()


# ==========================================
# OBJECT INTERACTION
# ==========================================

# Creating a HealthRecord object using patient1
record1 = HealthRecord(
    "R001",
    patient1,
    "Dr. Johnson",
    "Antimalarial medication"
)

# Display health record
print("\nHEALTH RECORD")
record1.display_record()


# HealthRecord interacts with Patient object
print("\nUPDATING PATIENT CONDITION")
record1.update_patient_condition("Recovering from malaria")


# Display updated patient information
print("\nUPDATED PATIENT INFORMATION")
patient1.display_info()


# ==========================================
# STATIC METHOD
# ==========================================

print("\nAGE CHECK")

if Patient.is_adult(patient1.age):
    print(patient1.name, "is an adult.")
else:
    print(patient1.name, "is a minor.")

if Patient.is_adult(patient3.age):
    print(patient3.name, "is an adult.")
else:
    print(patient3.name, "is a minor.")


# ==========================================
# DISPLAY SYSTEM NAME
# ==========================================

print("\nSystem:", Patient.system_name)