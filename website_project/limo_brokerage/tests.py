```python
from django.test import TestCase
from .models import Limo, Tracking

class LimoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Limo.objects.create(name='Test Limo', description='This is a test limo', image='test.jpg', availability=True, location='Test Location')

    def test_name_content(self):
        limo = Limo.objects.get(id=1)
        expected_object_name = f'{limo.name}'
        self.assertEquals(expected_object_name, 'Test Limo')

class TrackingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tracking.objects.create(limo_id=1, current_location='Test Location')

    def test_location_content(self):
        tracking = Tracking.objects.get(id=1)
        expected_object_location = f'{tracking.current_location}'
        self.assertEquals(expected_object_location, 'Test Location')
```