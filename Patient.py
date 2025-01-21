from MedicalApp import appointment


class Patient:
    def __init__(self, name, age, gender,new_appointment,contact_details):
        self.name = name
        self.age = age
        self.gender = gender
        self.__appointment = new_appointment
        self.medical_history = []
        self.__contact_details = contact_details

    def get_name(self):
        return self.name

    def get_contact_details(self):
        return self.__contact_details

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender



    def complete_appointment(self):
        self.medical_history.append(self.__appointment)
        self.__appointment.complete()

    def set_appointment(self,new_appointment):
        self.__appointment = new_appointment


