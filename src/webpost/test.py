from django.test import TestCase
from webpost.models import Post
from webuser.models import Webuser
from django.contrib.auth.models import User
from datetime import timedelta, datetime

from rest_framework.test import APIRequestFactory, APIClient

from oauth2_provider.models import Application, AccessToken


# def __create_token(user):
#     app = Application.objects.create(
#         client_type=Application.PUBLIC,
#         authorization_grant_type=Application.GRANT_IMPLICIT,
#         redirect_uris='https://www.none.com/oauth2/callback',
#         name='test_app',
#         user=user
#     )
#     assert app
#
#     access_token = AccessToken.objects.create(
#         user=user,
#         scope='read write',
#         expires=datetime.now() + timedelta(seconds=300),
#         token='secret-access-token-key',
#         application=app
#     )
#     assert access_token
#
#     return access_token

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User(username="Doc")
        self.user.save()
        self.webuser = Webuser.objects.get(user__username="Doc")

        self.bad_user = User(username="Docker")
        self.bad_user.save()
        self.bad_webuser = Webuser.objects.get(user=self.bad_user)
    def test_post_create(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        self.assertTrue(self.user.is_authenticated())
        response = client.post('/api/posts/', {'text':"Testing text"})
        self.assertEqual(response.status_code, 201)
        post = Post.objects.get(owner=self.webuser)
    def test_post_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        self.assertTrue(self.user.is_authenticated())
        response = client.post('/api/posts/', {'text': "Testing text"})

        client.force_authenticate(user=self.bad_user)
        response = client.put('/api/posts/%d/' % Post.objects.get(text="Testing text").pk, {'text': "Testing text"})
        self.assertEqual(response.status_code, 403)

        # factory = APIRequestFactory()
        #
        # # self.client.login sets up self.client.session to be usable
        # self.client.login(username='Doc', password='password')
        #
        # session = self.client.session
        # session['access_token'] = "super_test_token"
        # session.save()
        #
        # factory = APIRequestFactory()
        # request = factory.post('/notes/', {'title': 'new idea'})


class GeneralTestCase(TestCase):
    def test_general_access(self):
        client = APIClient()
        response = client.post('/')
        self.assertEqual(response.status_code, 302)
        response = client.post('/posts/')
        self.assertEqual(response.status_code, 200)
        response = client.post('/login/')
        self.assertEqual(response.status_code, 200)
