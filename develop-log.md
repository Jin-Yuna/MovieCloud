# 개발로그



- 5/15 첫 회의

아이디어 구상을 위한 브레인스토밍



- 5/16

아이디어 디벨롭 - 드라마, 영화 명소 빅데이터를 활용한 영화 명소 추천 서비스



- 5/17

아이디어 피벗팅 - 데이터의 부실 (드라마 위주, 데이터 수 적음)

=> 날씨에 따른 영화 추천, 그리고 영화 기록 서비스 (방구석 1열의 영화로그)

++ DB 1차 모델링 (ERD)



- 5/18

아이디어 확정 

와이어프레임 구성



- 5/19

movie 데이터 전처리 완료

ERD 완료

Component 구성 완료

서버 구축 시작



- 5/20

movie 데이터 재  전처리

커뮤니티 모델 구성 및 영화 연동 / 서버구축 / vue 연동중

소셜 로그인 토큰 받기 완료

git 오류 => push가 되지 않음 => git log를 출력해보니 origin/master와 master가 달라서 발생한 문제



- 5/21

vue 컴포넌트 구조화 및 수정

현재 위치 및 날씨 조회 기능 구현

=> store에서 유지보수 관리를 위해 modules로 위치와 날씨 정보를 빼서 진행 => 데이터가 업데이트 되지 못하고 undefined로 처리됨 

=> 모듈로 빼지 않고 store index.js 내에 적었더니 해결됨 

=> 문제는 과연 무엇이었을까?

지도 출력 

=> 오류 : Indicate whether to send a cookie in a cross-site request by specifying its SameSite attribute 

=> script로 sdk를 가져올 때 //dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=fcf79d7950891e2a0bcbec183a0187dd 

대신 https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=fcf79d7950891e2a0bcbec183a0187dd 입력 

=> 해결 완료! (크롬 쿠키 정책 때문에 그렇다고 함)

마커 구현하고, 키워드 검색을 하던 중 코드를 대규모로 변형시켰다가 돌이킬 수 없어서 정상적인 곳으로 돌리려고 노력하다가 겨우 돌리긴 했는데, 뭔가 달라졌음. 근데 모르겠음

기록의 중요성...

기능 하나 사소한 거라도 구현하면.. 푸쉬하자..ㅠㅠㅠ



- 5/22

지도 구현 완료, 내 위치를 중심으로 특정 반경 내에 있는 영화관 조사 후 정보 추출 => 마커 표시 및 정보 표시 완료



- 5/23

소셜 로그인 완료 => 기존 user랑 이어줌

