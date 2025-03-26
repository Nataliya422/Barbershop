from django.test import TestCase
from .models import Master, Service, Review, Appointment
from datetime import date

class AppointmentModelTest(TestCase):
    def setUp(self):
        self.master = Master.objects.create(name="John Doe", experience=5)
        self.service = Service.objects.create(name="Haircut", price=20.00)
        Appointment.objects.create(
            master=self.master,
            service=self.service,
            client_name="Client One",
            date=date(2025, 12, 25),
            time="14:00"
        )

    def test_appointment_details(self):
        appointment = Appointment.objects.get(client_name="Client One")
        self.assertEqual(appointment.date, date(2025, 12, 25))
        self.assertEqual(appointment.time, "14:00")
