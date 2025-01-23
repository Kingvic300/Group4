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

    def get_free_day(self,doctor):
        day = doctor.get_free_day()
        month = doctor.get_free_month()
        return date(2025,month,day)

    def get_free_time(self,doctor):
        hour = doctor.get_free_time()
        return time(hour,0)

    def schedule_appointment(self,age,gender,patient_name,description):

        doctor = self.__doctors["General Practitioner"]

        if age<13:
            doctor = self.__doctors["Pediatrician"]
        if gender=="Male" and age>13:
            doctor = self.__doctors["General Practitioner"]

        if gender=="Female" and age>13:
            doctor = self.__doctors["Gynaecologist"]

        schedule_date = self.get_free_day(doctor)
        schedule_time = self.get_free_time(doctor)

        new_appointment = Appointment(schedule_date,schedule_time,doctor.get_name(),patient_name,description)

        doctor.update_schedule(new_appointment)

        return new_appointment



    def create_patient(self,patient_name,patient_age,patient_gender,phone_number,email,description):

        patient_gender = patient_gender.lower()

        contact_info = ContactDetails(phone_number,email)
        appointment = self.schedule_appointment(patient_age, patient_gender, patient_name, description)

        new_patient = Patient(patient_name,patient_age,patient_gender,appointment,contact_info)
        self.__patients.append(new_patient)

        appointment.display()

