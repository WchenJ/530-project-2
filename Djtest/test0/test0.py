from cgitb import reset
from django.test import TestCase
import requests

class GetTestCase(TestCase):

    def test_get_root(self):
        r = requests.get("http://127.0.0.1:8000/api-auth/")
        assert r.ok
    def test_get_Users(self):
        r1 = requests.get("http://127.0.0.1:8000//User/")
        r2 = requests.get("http://127.0.0.1:8000//User/1/")
        assert r1.ok
        assert r2.ok
    def test_get_devices(self):
        r = requests.get("http://127.0.0.1:8000//Device/")
        assert r.ok
    def test_get_Healthdata(self):
        r1 = requests.get("http://127.0.0.1:8000//Healthdata/")
        r2 = requests.get("http://127.0.0.1:8000//Healthdata/1/")
        assert r1.ok
        assert r2.ok
    def test_get_divrec(self):
        r = requests.get("http://127.0.0.1:8000//Divrec/")
        assert r.ok
    def test_get_permission(self):
        r = requests.get("http://127.0.0.1:8000//Permission/")
        assert r.ok