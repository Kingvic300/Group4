from contactdetails import ContactDetails
from hospital import Hospital


hospital = Hospital("St Victor's", "Lagos")


def validate_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Please enter something na. This cannot be empty")


def get_valid_age():
    while True:
        try:
            age = validate_input("Enter patient age: ")
            age = int(age)
            if 0 < age <= 120:
                return age
            print("Age must be between 1 and 120.")
        except ValueError:
            print("Invalid age. Please enter a valid age.")


def get_valid_gender():
    while True:
        gender = validate_input("Enter patient gender (M/F): ").upper()
        if gender in ['M', 'F']:
            return gender
        print("Invalid gender. Please enter 'M' or 'F'.")


def get_valid_phone_number():
    while True:
        phone_number = validate_input("Enter patient phone number: ")
        try:
            ContactDetails.validate_contact_details(phone_number, "temp@email.com")
            return phone_number
        except ValueError as e:
            print(str(e))


def get_valid_email():
    while True:
        email = validate_input("Enter patient email address: ")
        try:
            ContactDetails.validate_contact_details("11111111111", email)
            return email
        except ValueError as e:
            print(str(e))


def create_patient():
    name = validate_input("Enter patient name: ")
    age = get_valid_age()
    gender = get_valid_gender()
    phone_number = get_valid_phone_number()
    email = get_valid_email()
    description = validate_input("Try and describe the symptoms you are experiencing: ")

    hospital.create_patient(name, age, gender, phone_number, email, description)


def schedule_appointment():
    patient_name = validate_input("Enter patient name: ")
    patient = hospital.find_patient_by_name(patient_name)

    if patient:
        description = validate_input("Enter appointment description: ")
        new_appointment = hospital.schedule_appointment(patient.age, patient.gender,
                                                        patient.name, patient.get_contact_details().get_phone_number(),
                                                        patient.get_contact_details().get_email(), description)
        print("Appointment Scheduled:")
        new_appointment.display()
    else:
        print("Patient not found.")


def search_patient():
    name = validate_input("Enter patient name: ")
    patient = hospital.find_patient_by_name(name)

    if patient:
        print(f"Patient Name: {patient.name}")
        print(f"Age: {patient.age}")
        print(f"Gender: {patient.gender}")
        print(f"Contact: {patient.get_contact_details().get_phone_number()}")
    else:
        print("Patient not found.")


def search_doctor():
    specialization = validate_input("Enter doctor specialization: ")
    for name, doctor in hospital.get_doctors_by_specialization(specialization).items():
        print(f"Name: {doctor.get_name()}")
        print(f"Specialization: {doctor.get_specialization()}")


def view_all_doctors():
    for name, doctor in hospital.get_all_doctors().items():
        print(f"Name: {doctor.get_name()}")
        print(f"Specialization: {doctor.get_specialization()}\n")


def view_all_patients():
    for patient in hospital.get_all_patients():
        print(f"Name: {patient.get_name()}")
        print(f"Age: {patient.age}")
        print(f"Gender: {patient.get_gender()}\n")


def view_appointments():
    for name, doctor in hospital._Hospital__doctors.items():
        print(f"\nAppointments for Dr. {doctor.get_name()}:")
        doctor.review_schedule()


def view_patient_history():
    name = validate_input("Enter patient name: ")
    patient = hospital.find_patient_by_name(name)

    if patient:
        print(f"Medical History for {patient.name}:")
        patient.check_medical_history()
    else:
        print("Patient not found.")


def admin_menu():
    options = """
    Receptionist's Menu

    1. Create Patient
    2. Schedule Appointment
    3. Search Patient
    4. Search Doctor
    5. View All Patients
    6. View All Doctors
    7. View All Appointments
    8. View Patient Medical History
    9. Exit

    """
    while True:
        print(options)
        choice = validate_input("Enter your choice from the menu: ")

        if choice == '1':
            create_patient()
        elif choice == '2':
            schedule_appointment()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            search_doctor()
        elif choice == '5':
            view_all_patients()
        elif choice == '6':
            view_all_doctors()
        elif choice == '7':
            view_appointments()
        elif choice == '8':
            view_patient_history()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Try again.")


def view_doctor_schedule(doctor):
    print(f"Appointment Schedule for Dr. {doctor.get_name()}:")
    doctor.review_schedule()


def fulfill_appointment():
    doctor_name = validate_input("Enter doctor's name: ")
    doctor = hospital.verify_doctor_by_name(doctor_name)

    if not doctor:
        print("Doctor not found.")
        return

    print("Current Schedule:")
    doctor.review_schedule()

    if not doctor.get_schedule():
        print("No appointments to fulfill.")
        return

    appointment = doctor.get_schedule()[0]
    hospital.fulfill_appointment(doctor, appointment)



def view_doctor_history(doctor):
    print(f"Appointment History for Dr. {doctor.get_name()}:")
    doctor.review_medical_history()


def doctors_menu():
    name_of_doctor = validate_input("Enter your name: ")
    doctor = hospital.verify_doctor_by_name(name_of_doctor)

    if not doctor:
        print("Doctor is not in this hospital.")
        return

    options = """
    Doctor's Menu

    Press 1 to View Appointment Schedule
    Press 2 to View Appointment History
    Press 3 to Fulfill Appointment
    Press 4 to Exit 

    """
    while True:
        print(options)

        choice = validate_input("Enter your choice (1-3) from the menu: ")

        if choice == '1':
            view_doctor_schedule(doctor)
        elif choice == '2':
            view_doctor_history(doctor)
        elif choice == '3':
            fulfill_appointment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")


def cover_page():
    while True:
        choice = validate_input("""
        Welcome to St Victor's Hospital

        Are you a doctor at this hospital? Press 1
        Are you an administrator/receptionist? Press 2
        To Exit the application, Press 3

        Please, follow the guidelines
        """)

        if choice == '2':
            admin_menu()

        elif choice == '1':
            doctors_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")


cover_page()