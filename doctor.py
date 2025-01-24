class Doctor:
    def __init__(self,name,specialization):
        self.__name = name
        self.__specialization = specialization
        self.__schedule = []
        self.__appointment_history = []
        self.__free_time = 9
        self.__free_day = 21
        self.__free_month = 1


    def update_schedule(self,appointment):

        self.__free_time+=1
        if self.__free_time%17 == 0 :
            self.__free_day+=1

        self.__schedule.append(appointment)

    def get_schedule(self):
        return self.__schedule

    def review_schedule(self):
        for appointment in self.__schedule:
            appointment.display()

    def review_medical_history(self):
        for appointment in self.__appointment_history:
            appointment.display()

    def get_name(self):
        return self.__name

    def get_specialization(self):
        return self.__specialization

    def get_free_time(self):
        return self.__free_time%17

    def get_free_day(self):
        return self.__free_day%28

    def get_free_month(self):
        return self.__free_month

    @staticmethod
    def __validate_doctor_information(self, specialization):
        if specialization == "None" or  not specialization:
            raise ValueError("Invalid specialization")
