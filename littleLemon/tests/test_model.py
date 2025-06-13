from django.test import TestCase
from myapp.models import Booking, Menu

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="chai", price=9.99, inventory=100)
        self.assertEqual(str(item), "chai : 9.99")
        
class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(name="John Doe", booking_date="2023-10-01 12:00:00", no_of_guests=4)
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 4)
        self.assertEqual(str(booking.booking_date), "2023-10-01 12:00:00")