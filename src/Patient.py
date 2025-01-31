from appointment import Appointment
from contactdetails import ContactDetails


class Patient:
    def __init__(self, name, age, gender,new_appointment: 'Appointment',contact_details:'ContactDetails'):
        self.name = name
        self.age = age
        self.gender = gender
        self.__appointment = new_appointment
        self.medical_history : list[Appointment] = []
        self.__contact_details = contact_details

    @staticmethod
    def validate_patient_information(self, age, gender):
        if age < 0 or age > 120:
            raise ValueError("age must be between 0 and 120")
        if gender not in ['M', 'F']:
            raise ValueError("gender must be either 'M' or 'F'")

    def get_name(self):
        return self.name

    def get_contact_details(self):
        return self.__contact_details

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def complete_appointment(self):
        self.__appointment.complete()

    def set_appointment(self,new_appointment):
        self.__appointment = new_appointment

    def add_to_medical_history(self, appointment):
        self.medical_history.append(appointment)
        print(len(self.medical_history))


    def check_medical_history(self):
        print(len(self.medical_history))
        for i in range(len(self.medical_history)):
            print(self.medical_history[i].show(1))

