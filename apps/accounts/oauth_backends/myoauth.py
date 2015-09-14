# -*- coding: utf-8 -*-

from social.backends.oauth import BaseOAuth2
from django.core.urlresolvers import reverse
from django.conf import settings

#class DjangoOAuth2(BaseOAuth2):
#    """Default OAuth2 authentication backend used by this package"""
#    name = settings.PROPRIETARY_BACKEND_NAME
#    AUTHORIZATION_URL = reverse('authorize')
#    ACCESS_TOKEN_URL = reverse('token')



class MyOAuthOAuth2(BaseOAuth2):
    name = 'myoauth'
    AUTHORIZATION_URL   = 'http://127.0.0.1:8000/o/authorize'
    ACCESS_TOKEN_URL    = 'http://127.0.0.1:8000/o/token'
    ACCESS_TOKEN_METHOD = 'POST'

    #def get_user_id(self, details, response):
    #    # Sometimes Instagram returns 'user', sometimes 'data', but API docs
    #    # says 'data' http://instagram.com/developer/endpoints/users/#get_users
    #    user = response.get('user') or response.get('data') or {}
    #    return user.get('id')
    #
    #def get_user_details(self, response):
    #    """Return user details from Instagram account"""
    #    # Sometimes Instagram returns 'user', sometimes 'data', but API docs
    #    # says 'data' http://instagram.com/developer/endpoints/users/#get_users
    #    user = response.get('user') or response.get('data') or {}
    #    username = user['username']
    #    email = user.get('email', '')
    #    fullname, first_name, last_name = self.get_user_names(
    #        user.get('full_name', '')
    #    )
    #    return {'username': username,
    #            'fullname': fullname,
    #            'first_name': first_name,
    #            'last_name': last_name,
    #            'email': email}
    #
    #def user_data(self, access_token, *args, **kwargs):
    #    """Loads user data from service"""
    #    return self.get_json('http://127.0.0.1:8000/v1/users/self',
    #                         params={'access_token': access_token})
