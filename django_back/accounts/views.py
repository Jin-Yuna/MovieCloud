from django.shortcuts import render, redirect
import requests
from rest_framework.response import Response

def kakaoLogin(request):
    restApiKey = '683d19aa3f66f6c7d4ca3b08f6f139ed'
    redirectUrl = 'http://127.0.0.1:8000/accounts/kakaoLogin'
    url = f'https://kauth.kakao.com/oauth/authorize?client_id={restApiKey}&redirect_uri={redirectUrl}&response_type=code'
    return redirect(url)

def kakaoLoginCallback(request):
    qs = request.GET['code']
    restApiKey = '683d19aa3f66f6c7d4ca3b08f6f139ed'
    redirect_uri = 'http://127.0.0.1:8000/accounts/kakaoLogin'
    url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={restApiKey}&redirect_uri={redirect_uri}&code={qs}'
    res = requests.post(url)
    result = res.json()
    return Response(result)

