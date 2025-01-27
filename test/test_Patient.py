import unittest
from src.contactdetails import ContactDetails
from src.doctor import Doctor
from src.hospital import Hospital

class TestPatient(unittest.TestCase):
    def setUp(self):
        contact = ContactDetails("12345678901", "patient@email.com")
        self.doctor = Doctor("Albert", "General Practitioner")
        self.hospital = Hospital("Test Hospital", "Test Location")
        self.patient = self.hospital.create_patient(
            "Sarah", 35, "F",
            "12345678901", "sarah@email.com",
            "initial consultation"
        )
    def test_medical_history_tracking(self):

        self.patient.complete_appointment()

        self.assertEqual(len(self.patient.medical_history), 1)