class ContactDetails:
    def __init__(self,phone_number, email):
        self.validate_contact_details(phone_number, email)
        self.__phone_number = phone_number
        self.__email = email

    @staticmethod
    def validate_contact_details(phone_number, email):
        if not phone_number.isdigit() or len(phone_number) != 11:
            raise ValueError("The phone number is not valid")

        if '@' not in email or '.' not in email:
            raise ValueError("The email is not valid")

    def get_phone_number(self):
        return self.__phone_number

    def get_email(self):
        return self.__email