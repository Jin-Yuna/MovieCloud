from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serailizers import ProfileSerializer
from rest_framework.decorators import api_view
from accounts.models import User
from django.shortcuts import redirect
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
import requests
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse

def kakaoLogin(request):
    auth_code = request.GET.get('code')
    kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': '683d19aa3f66f6c7d4ca3b08f6f139ed',
        'redirect_uri': 'http://127.0.0.1:8000/accounts/kakao/callback/',
        'code': auth_code,
    }
    token_req = requests.post(kakao_token_api, data=data)
    token_req_json = token_req.json()
    access_token = token_req_json.get("access_token")
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
    # # 회원 가입
    # User.objects.create(
    #     kakao_id = profile_json['id'],
    #     is_superuser = 0,
    #     is_staff = 0,
    #     is_active = 1, 
    #     date_joined = profile_json['connected_at'],
    #     password = access_token,
    #     nickname = profile_json['properties']['nickname']
    # )

    # return redirect(f'http://localhost:8080/kakaoLogin/{current_user}/')
    # try:
    #     # 기존에 가입된 유저의 Provider가 kakao가 아니면 에러 발생, 맞으면 로그인
    #     user = User.objects.get(email=email)
    #     social_user = SocialAccount.objects.get(user=user)
    #     print(social_user)
    # except User.DoesNotExist:
        

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/'
    client_class = OAuth2Client

@api_view(['GET'])
def profile(request, pk):
    
    user = get_object_or_404(User, pk=pk)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

