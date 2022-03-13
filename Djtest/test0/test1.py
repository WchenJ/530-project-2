from email.policy import default
from django.test import TestCase
from test0.models import User, Healthdata


# Create your tests here.
class UserTestCase(TestCase):

    def setUp(self):
        # Create two objects, one with default ALL, one with specified last/first/address
        User.objects.create(Name="d", birthDate='1999-09-21',role="Docter")
        User.objects.create()

    def test_user_creation(self):
        definedUser = User.objects.get(firstName="Dr.Zhang")
        defaultUser = User.objects.get(firstName="Bian Zhi Ling")
        self.assertEqual(definedUser.role, "patient")
        self.assertEqual(defaultUser.role, "doctor")


class HealthdataTestCase(TestCase):

    def setUp(self):
        Healthdata.objects.create(id= 2,permission= 3,tempreture="36.5",time= "2022-03-05")
        Healthdata.objects.create()
        pass

    def test_Healthdata_creation(self):
        definedMed = Healthdata.objects.get(id=2)
        defaultMed = Healthdata.objects.get(permission=3)
        self.assertEqual(definedMed.id, 2)
        self.assertEqual(defaultMed.permission, 3)
        pass

