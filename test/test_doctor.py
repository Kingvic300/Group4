import unittest
from src.doctor import Doctor
from src.appointment import Appointment
from src.Patient import Patient
from src.contactdetails import ContactDetails
from datetime import date, time

class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor("Albert", "General Practitioner")
        contact = ContactDetails("12345678901", "patient@email.com")
        self.patient = Patient("Saka", 30, "M", None, contact)

    def test_schedule_management(self):
        self.assertEqual(len(self.doctor.get_schedule()), 0)

        appointment = Appointment(date(2025, 1, 21), time(9, 0),
                                  self.doctor, self.patient,"Test description"
                        )

        self.doctor.update_schedule(appointment)

        self.assertEqual(len(self.doctor.get_schedule()), 1)