import requests
from .models import User
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from .serailizers import KakaoUserSerializer, ProfileSerializer
from rest_framework.decorators import api_view

def kakaoLogin(request):
    
    auth_code = request.GET.get('code')
    kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': '683d19aa3f66f6c7d4ca3b08f6f139ed',
        'redirect_uri': 'http://127.0.0.1:8000/kakaoLogin',
        'code': auth_code,
    }
    token_response = requests.post(kakao_token_api, data=data)
    access_token = token_response.json().get('access_token')
    user_info_response = requests.get('https://kapi.kakao.com/v2/user/me',
    headers={"Authorization": f'Bearer ${access_token}'})
    user_info_response = user_info_response.json()


    # 이미 있는 회원인지 검사
    is_exist = False
    users = User.objects.all()
    for user in users:
        if user.kakao_id == user_info_response['id']:
            is_exist = True
            break
    current_user = user_info_response['id']
    # 회원 가입
    if is_exist == False:
        User.objects.create(
            kakao_id = user_info_response['id'],
            is_superuser = 0,
            is_staff = 0,
            is_active = 1, 
            date_joined = user_info_response['connected_at'],
            password = access_token,
            nickname = user_info_response['properties']['nickname']
        )

    return redirect(f'http://localhost:8080/kakaoLogin/{current_user}/')


@api_view(['GET'])
def kakaoInfo(request, pk):
    current_user = get_object_or_404(User, kakao_id=pk)
    serializer = KakaoUserSerializer(current_user)
    return Response(serializer.data)

@api_view(['GET'])
def profile(request, pk):
    
    user = get_object_or_404(User, pk=pk)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

