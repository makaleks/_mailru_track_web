from django.test import TestCase
from webuser.models import Webuser
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def test_user_post_save(self):
        user = User(username="Doc")
        user.save()
        webuser = Webuser.objects.get(user__username="Doc")
        self.assertEqual(webuser.user, user)