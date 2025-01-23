from MedicalApp.hospital import Hospital

hospital =  Hospital("St Victors","Lagos")

def admin_menu():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    description = input("Try and describe the symptoms you are experiencing: ")

    hospital.create_patient(name,age,gender,phone,email,description)


def doctors_menu():
    pass

def cover_page():
    choice = input(""""
    Welcome to St Victors Hospital
    
    1.) You are a doctor
    2.) You are an administrator
    """)

    if choice == '2':
        admin_menu()

    elif choice == '1':
        doctors_menu()



cover_page()