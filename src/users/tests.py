from django.test import TestCase
from src.users.forms import SignUpForm

class ProfileFormTestCase(TestCase):
    def full_form():
        form = SignUpForm(data={"username":"zixxa"
                                "email":"123@yandex.ru"
                                "password1":"zaqwsxcderfv12"
                                "password2":"zaqwsxcderfv12"
                                })
        self.assertEqual(
            form.errors["username"], ["Username error"]
            form.errors["email"], ["Email error"]
            form.errors["password1"], ["Pass error"]
            form.errors["password2"], ["Pass2 error"]
        )

