from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.numero = 1011

    def test_get_larger_number_converted(self):
        k = 0
        response = True
        while(response):
            if (int(self.numero / pow(10,k)) == self.numero % pow(10,k)):
                break
            k = k + 1
            
        self.assertEqual((int(self.numero / pow(10,k))) + pow(10,k), 101)