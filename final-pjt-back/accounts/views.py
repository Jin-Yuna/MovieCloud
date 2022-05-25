from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serailizers import ProfileSerializer
from rest_framework.decorators import api_view
from accounts.models import User
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
import requests
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.http import JsonResponse
from .serailizers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

def kakaoLogin(request):
    print('시작해랑')
    auth_code = request.headers['code']
    access_token = request.headers['Token']
    print(auth_code)
    print(access_token)
    """
    Email Request
    """
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    profile_json = profile_request.json()
    print(profile_json)
    kakao_account = profile_json.get('kakao_account')
    print(kakao_account)
    """
    Signup or Signin Request
    """
    # 기존에 가입된 유저가 없으면 새로 가입
    # BASE_URL = ''
    BASE_URL = 'http://127.0.0.1:8000/'
    data = {'access_token': access_token, 'code': auth_code}
    accept = requests.post(
        f"{BASE_URL}kakao/login/finish/", data=data)
    accept_status = accept.status_code
    if accept_status != 200:
        return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
    # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
    accept_json = accept.json()
    print(accept_json)
    accept_json.pop('user', None)
    print(accept_json)
    return JsonResponse(accept_json)      

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/'
    client_class = OAuth2Client

@api_view(['GET'])
def profile(request, pk):
    
    user = get_object_or_404(User, pk=pk)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, pk):
    person = get_object_or_404(User, pk=pk)
    if person != request.user:
        # 지금 보고있는 사람의 팔로잉 목록에 내가 있으면
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            serializer = ProfileSerializer(person)
            return Response(serializer.data)
        else:
            person.followers.add(request.user)
            serializer = ProfileSerializer(person)
            return Response(serializer.data)
    