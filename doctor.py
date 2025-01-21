class Doctor:
    def __init__(self,name,specialization):
        self.__name = name
        self.__specialization = specialization
        self.__schedule = []
        self.__medical_history = []


    def updateSchedule(self,appointment):
        self.__schedule.append(appointment)

    def reviewSchedule(self):
        for appointment in self.__schedule:
            appointment.display()


    def review_medical_history(self):
        for appointment in self.__medical_history:
            appointment.display()


    def getName(self):
        return self.__name

    def getSpecialization(self):
        return self.__specialization


