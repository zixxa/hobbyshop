from django.test import TestCase
from src.users.forms import SignUpForm

class ProfileFormTestCase(TestCase):
    def full_form():
        form = SignUpForm(data={"username":"zixxa",
                                "email":"qwe@yandex.ru",
                                "password1":"zaqwsxcderfv12",
                                "password2":"zaqwsxcderfv12"
                                })

        sert.assertTemplateUsed(form, "/")
