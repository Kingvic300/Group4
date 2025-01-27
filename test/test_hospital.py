import unittest
from src.hospital import Hospital
from src.driver import hospital


class TestHospital(unittest.TestCase):
    def setUp(self):
        self.hospital = Hospital("Test Hospital", "Test Address")

    def test_create_patient(self):
        patient = self.hospital.create_patient(
            "Saka", 30, "M",
            "12345678901", "patient@email.com",
            "routine checkup"
        )

        self.assertIsNotNone(patient)
        self.assertEqual(patient.name, "Saka")
        self.assertEqual(patient.age, 30)

    def test_doctor_specialization_lookup(self):
        doctors = self.hospital.get_doctors_by_specialization("Pediatrician")

        self.assertIn("Hawkins", [doctor.get_name() for doctor in doctors.values()])

    def test_appointment_can_be_created(self):
        appointment = self.hospital.schedule_appointment(
            10, "M", "Kabiru",
            "12345678901", "child@email.com",
            "routine checkup"
        )
        self.assertEqual(hospital.doctor.get_name(), "Hawkins" )


        appointment_two = self.hospital.schedule_appointment(
            25, "M", "Adult Male",
            "12345678901", "adult@email.com",
            "general checkup"
        )
        self.assertEqual(appointment_two.doctor.get_name(), "Albert")