from django.test import TestCase
from course.models import (
    Departement,
    Semester,
    Module,
    Course
)

class TestDepartementsModel(TestCase):
    def setUp(self):
        self.data1 = Departement.objects.create(
            name = 'django',
            views = 1337,
            count = 96
        )
    def test_departement_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Departement))