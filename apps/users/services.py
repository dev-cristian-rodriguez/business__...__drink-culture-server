# services.py
from django.conf import settings
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from urllib.parse import urlencode
from typing import Dict, Any
from dotenv import load_dotenv
import requests
import jwt
import os

GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'
# LOGIN_URL = f'{settings.BASE_APP_URL}/internal/login'

load_dotenv()


# Exchange authorization token with access token
def google_get_access_token(code: str) -> str:
    data = {
        'code': code,
        'client_id': os.getenv("OAUTH_CLIENT_ID"),
        'client_secret': os.getenv("OAUTH_CLIENT_SECRET"),
        'redirect_uri': os.getenv('REDIRECT_URI'),
        'grant_type': 'authorization_code'
    }

    response = requests.post(GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)
    
    if not response.ok:
        raise ValidationError('Could not get access token from Google.')
    
    access_token = response.json().get('access_token')

    return access_token

# Get user info from google
def google_get_user_info(access_token: str) -> Dict[str, Any]:
    response = requests.get(
        GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )

    if not response.ok:
        raise ValidationError('Could not get user info from Google.')
    
    return response.json()


# def get_user_data(validated_data):
#     domain = settings.BASE_API_URL
#     redirect_uri = f'{domain}/auth/api/login/google/'

#     code = validated_data.get('code')
#     error = validated_data.get('error')

#     if error or not code:
#         params = urlencode({'error': error})
#         return redirect(f'{LOGIN_URL}?{params}')
    
#     access_token = google_get_access_token(code=code, redirect_uri=redirect_uri)
#     user_data = google_get_user_info(access_token=access_token)

#     # Creates user in DB if first time login
#     User.objects.get_or_create(
#         username = user_data['email'],
#         email = user_data['email'],
#         first_name = user_data.get('given_name'), 
#         last_name = user_data.get('family_name')
#     )
    
#     profile_data = {
#         'email': user_data['email'],
#         'first_name': user_data.get('given_name'),
#         'last_name': user_data.get('family_name'),
#     }
    
#     return profile_data