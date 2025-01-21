from MedicalApp.Patient import Patient
from MedicalApp.appointment import Appointment
from MedicalApp.contactdetails import ContactDetails
from MedicalApp.doctor import Doctor
from datetime import date
from datetime import time


class Hospital:

    def __init__(self, hospital_name, hospital_address):
        self.__hospital_name = hospital_name
        self.__hospital_address = hospital_address
        self.__doctors = {}
        self.__patients = []
        self.get_doctors()

    def get_doctors(self):

        self.__doctors["General Practitioner"] = Doctor("Albert","General Practitioner")
        self.__doctors["Obstetrician"] = Doctor("Isaac","Obstetrician")
        self.__doctors["Pediatrician"] = Doctor("Hawkins","Pediatrician")
        self.__doctors["Surgeon"] = Doctor("Carson","Surgeon")
        self.__doctors["Gynaecologist"] = Doctor("Salami","Gynaecologist")


    def schedule_appointment(self,age,gender,patient_name,description):

        doctor = self.__doctors["General Practitioner"]

        if age<13:
            doctor = self.__doctors["Pediatrician"]
        if gender=="Male" and age>13:
            doctor = self.__doctors["General Practitioner"]

        if gender=="Female" and age>13:
            doctor = self.__doctors["Gynaecologist"]

        schedule_date = date(2025,1,13)
        schedule_time = time(9,0)

        new_appointment = Appointment(date,schedule_time,doctor.getName(),patient_name,description)

        doctor.updateSchedule(new_appointment)

        return new_appointment



    def create_patient(self,patient_name,patient_age,patient_gender,phone_number,email,description):
        contact_info = ContactDetails(phone_number,email)
        appointment = self.schedule_appointment(patient_age, patient_gender, patient_name, description)

        new_patient = Patient(patient_name,patient_age,patient_gender,appointment,contact_info)
        self.__patients.append(new_patient)

