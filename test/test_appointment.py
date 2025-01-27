import unittest
from datetime import date, time
from src.hospital import Hospital
from src.doctor import Doctor
from src.Patient import Patient
from src.contactdetails import ContactDetails
from src.appointment import Appointment

class TestAppointment(unittest.TestCase):
    def setUp(self):
        self.hospital = Hospital("Test Hospital", "Test Address")
        contact = ContactDetails("12345678901", "patient@email.com")
        self.doctor = Doctor("Albert", "General Practitioner")
        self.patient = Patient("Jesse", 30, "M", None, contact)

    def test_appointment_description(self):
        appointment = Appointment(
            date(2025, 1, 21),
            time(9, 0),
            self.doctor,
            self.patient,
            "mental health check"
        )
        self.assertEqual(appointment.get_description(), "mental health check")

    def test_appointment_is_not_completed_initially(self):
        appointment = Appointment(
            date(2025, 1, 21),
            time(9, 0),
            self.doctor,
            self.patient,
            "mental health check"
        )
        self.assertFalse(appointment.is_completed())

    def test_appointment_can_be_completed(self):
        appointment = Appointment(
            date(2025, 1, 21),
            time(9, 0),
            self.doctor,
            self.patient,
            "mental health check"
        )
        appointment.complete()
        self.assertTrue(appointment.is_completed())