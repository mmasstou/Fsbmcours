from django.test import TestCase
from course.models import (
    Departement,
    Semester,
    Module,
    Course
)
from account.models import User

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
    def test_departement_model_return(self):
        data = self.data1
        self.assertEqual(str(data), "django")


class TestCoursesModel(TestCase):
   
    def setUp(self):
        user_qs = User.objects.create(
            username = 'admin'
        )
        departement_qs =Departement.objects.create(
                name = 'django',
                views = 1337,
                count = 96
            )
        semester_qs = Semester.objects.create(
            name = "semester 1",
            auther = user_qs,
            departement = departement_qs,
            slug = "semester-1"
        )
        module_qs = Module.objects.create(
            name = "Mecanique de Solide",
            views = 1337,
            count = 1337,
            semester = semester_qs,
            slug = "mecanique-de-solide"

        )
        self.data11 = Course.objects.create(
            name = 'django',
            views = 1337,
            count = 96,
            module = module_qs,
            course_file = "test"
        )
    def test_course_model_entry(self):
        data = self.data11
        self.assertTrue(isinstance(data, Course))