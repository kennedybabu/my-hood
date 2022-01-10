from django.test import TestCase
from .models import Hood

# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.kabete = Hood(hood_name = 'kabete')

    def test_instance(self):
        self.assertTrue(isinstance(self.kabete, Hood))

    def tearDown(self):
        Hood.objects.all().delete()

    def test_save_method(self):
        self.ngong.create_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood) > 0)
