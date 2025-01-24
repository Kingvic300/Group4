from datetime import date
from datetime import time

from PythonClass.ClassExercises.MedicalApp.doctor import Doctor



class Appointment:
    def __init__(self, date: date, time: time, doctor:'Doctor', patient:'Patient' , description:str):
        self.__appointment_date = date
        self.__appointment_time = time
        self.__doctor = doctor
        self.__patient = patient
        self.__is_completed = False
        self.__description = description

    def display(self):
        display = f"""
                Patient : {self.__patient.get_name()}
                date :{self.__appointment_date}
                time : {self.__appointment_time}
                description : {self.__description}
                Doctor : {self.__doctor.get_name()}    

        """
        print(display)

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    # def get_doctor_name(self):
    #     return self.__doctor_name
    #
    # def get_patient_name(self):
    #     return self.__patient_name

    def set_date(self, new_date):
        self.__date = new_date

    def set_time(self, new_time):
        self.__time = new_time

    def is_completed(self):
        return self.__is_completed

    def complete(self):
        self.__is_completed = True
        self.__patient.add_to_medical_history(self)