```python
from django.test import TestCase
from .models import Lead

class LeadModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Lead.objects.create(name='John', email='john@example.com', phone='1234567890', interested_in='Limo1')

    def test_name_content(self):
        lead = Lead.objects.get(id=1)
        expected_object_name = f'{lead.name}'
        self.assertEquals(expected_object_name, 'John')

    def test_email_content(self):
        lead = Lead.objects.get(id=1)
        expected_object_email = f'{lead.email}'
        self.assertEquals(expected_object_email, 'john@example.com')

    def test_phone_content(self):
        lead = Lead.objects.get(id=1)
        expected_object_phone = f'{lead.phone}'
        self.assertEquals(expected_object_phone, '1234567890')

    def test_interested_in_content(self):
        lead = Lead.objects.get(id=1)
        expected_object_interested_in = f'{lead.interested_in}'
        self.assertEquals(expected_object_interested_in, 'Limo1')
```