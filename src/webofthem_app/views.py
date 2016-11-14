from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

from oauth2_provider.models import AccessToken

class ApiAccess(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        try:
            key = request.META.get('HTTP_AUTHORIZATION').split()[1]
            token = AccessToken.objects.get(token=key)
            return HttpResponse(token.expires
                    )
        except:
            return HttpResponse('Hello, OAuth2!')
