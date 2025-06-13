from django.test import TestCase
from .models import Booking, Menu

# Create your tests here.
class MenuModelTest(TestCase):
    def test_get_item(self):
        item =  Menu.objects.create(name="chai", price=9.99, inventory=100)
        self.assertEqual(str(item), "chai : 9.99")
        
