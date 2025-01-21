class ContactDetails:
    def __init__(self,phone_number, email):
        self.__phone_number = phone_number
        self.__email = email


    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email