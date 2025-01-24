from appointment import Appointment
from contactdetails import ContactDetails
from Patient import Patient
from doctor import Doctor
from datetime import date
from datetime import time


class Hospital:

    def __init__(self, hospital_name, hospital_address):
        self.__hospital_name = hospital_name
        self.__hospital_address = hospital_address
        self.__doctors = {}
        self.__patients :list[Patient]= []
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

    def schedule_appointment(self,patient_age,patient_gender,patient_name,phone_number,email, description):

        doctor = self.__doctors["General Practitioner"]

        if patient_age<13:
            doctor = self.__doctors["Pediatrician"]
        elif patient_gender=="M" and patient_age>13:
            doctor = self.__doctors["General Practitioner"]
        elif patient_gender=="F" and patient_age>13:
            doctor = self.__doctors["Gynaecologist"]

        schedule_date = self.get_free_day(doctor)
        schedule_time = self.get_free_time(doctor)

        patient_contact = ContactDetails(phone_number,email)

        new_appointment = Appointment(schedule_date,schedule_time,doctor,patient_name,description)

        new_patient = Patient(patient_name, patient_age, patient_gender, new_appointment, patient_contact)

        new_patient.set_appointment(new_appointment)
        doctor.update_schedule(new_appointment)

        return new_appointment

    def create_patient(self,patient_name,patient_age,patient_gender,phone_number,email,description):

        patient_gender = patient_gender.lower()

        patient_contact = ContactDetails(phone_number,email)
        appointment = self.schedule_appointment(patient_age, patient_gender, patient_name, phone_number,email, description)

        new_patient = Patient(patient_name,patient_age,patient_gender,appointment, patient_contact)
        self.__patients.append(new_patient)

        appointment.display()
        return new_patient

    def find_patient_by_name(self,patient_name):
        for patient in self.__patients:
            if patient.name == patient_name:
                return patient
        return None

    def get_doctors_by_specialization(self, specialization):
        doctor_on_site = {}
        for name,doctor in self.__doctors.items():
            if doctor.get_specialization().lower() == specialization.lower():
                doctor_on_site[name] = doctor
        return doctor_on_site


    def verify_doctor_by_name(self, name_of_doctor):
        for doctor in self.__doctors.values():
            if doctor.get_name() == name_of_doctor:
                return doctor
        return None

    def get_all_doctors(self):
        return self.__doctors

    def get_all_patients(self):
        return self.__patients

    def fulfill_appointment(self, doctor, appointment):
        doctor._Doctor__schedule.remove(appointment)
        doctor._Doctor__appointment_history.append(appointment)
        appointment.complete()
        patient : Patient = self.find_patient_by_name(appointment.get_patient_name())
        patient.add_to_medical_history(appointment)

