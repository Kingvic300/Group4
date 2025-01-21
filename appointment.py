

class Appointment:
    def __init__(self,date ,time,doctor_name,patient_name,description):
        self.__date = date
        self.__time = time
        self.__doctor_name = doctor_name
        self.__patient_name = patient_name
        self.__is_completed = False
        self.__description = description

    def display(self):
        display = f""""
                Patient : {self.__patient_name}
                date : {self.__date}
                time : {self.__time}
                description : {self.__description}
                Doctor : {self.__doctor_name}    
                
        """

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_doctor_name(self):
        return self.__doctor_name

    def get_patient_name(self):
        return self.__patient_name

    def set_date(self,new_date):
        self.__date = new_date

    def set_time(self,new_time):
        self.__time = new_time

    def is_completed(self):
        return self.__is_completed

    def complete(self):
        self.__is_completed = True