# Final Project 



movie cloud



- 아이디어 구상

  - 컨셉 : **movie cloud!** 날씨 + 물방울이 모여 하나의 구름 cloud

  - Main Topic :  날씨에 따른 영화 추천, 그리고 영화 기록 서비스 (방구석 1열의 영화로그)

  - 기능  
    - 날씨에 따른 영화 추천 서비스
    - 박스오피스 순위, 평점 순위 별 영화 추천
    - 위치 추적 및 나와 가까운 영화관 추천
    - 영화 검색
    - 유저의 영화로그 - 좋아요, 팔로우, 댓글 모두 포함

  

- DB 모델링

  https://www.erdcloud.com/d/G8cXxibj3XtrzyNzo

  ![캡처](final_project.assets/캡처-16529446236811.PNG)

  

- 컴포넌트 모델링

  https://app.diagrams.net/?src=about#G1JWp5ZrQux3Rr7myTiI-TF0OEcIUqQLBF

  ![Untitled Diagram-Page-4.drawio](final_project.assets/Untitled Diagram-Page-4.drawio.png)

  ![뷰 구조화](final_project.assets/뷰 구조화.PNG)

  ![Untitled Diagram-Page-3.drawio](final_project.assets/Untitled Diagram-Page-3.drawio.png)

  ![Untitled Diagram-Page-2.drawio](final_project.assets/Untitled Diagram-Page-2.drawio.png)

  ![Untitled Diagram-Page-1.drawio](final_project.assets/Untitled Diagram-Page-1.drawio.png)

- 디자인

  https://www.figma.com/file/k1Lz7Fjnq88zOU0xguTGHk/movie_project

- 기능 개발

  - 추천 알고리즘 (유저 기반)

    https://proinlab.com/archives/2103

  - API ?

    - tmdb

      https://developers.themoviedb.org/3

      - 영화 데이터 가져와 저장법
  
        https://velog.io/@ready2start/Mollbar-%ED%8A%B8%EB%9F%AC%EB%B8%94-%EC%8A%88%ED%8C%85-%EC%98%81%ED%99%94-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0
  
        
    
    - 로그인/회원가입 - 카카오 api
    
      https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api
    
      소셜 로그인 https://loffin.tistory.com/47
    
    - 지도 
    
      - 위치 추척
    
        https://developer.mozilla.org/ko/docs/Web/API/Geolocation_API/Using_the_Geolocation_API
    
        https://7942yongdae.tistory.com/150
    
      - 현재 위치의 날씨 추적
    
        https://velog.io/@latte_h/%ED%98%84%EC%9E%AC-%EC%9C%84%EC%B9%98%EC%9D%98-%EB%82%A0%EC%94%A8-%EC%A0%95%EB%B3%B4-%ED%91%9C%EC%8B%9C
    
    - 극장 조회? - 카카오맵 api (키워드로 장소 검색)
    
      https://apis.map.kakao.com/web/sample/keywordBasic/
    
    - 국내 지역별 영화 드라마 촬영장소 및 시설 데이터 (참고)
    
      https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=8631a170-ed98-4bc1-8757-de0a4d75d85e
      
      



---------------------------------

참고

프로젝트 계획법 https://ko.khanacademy.org/computing/computer-programming/programming/good-practices/a/planning-a-programming-project

로딩 애니메이션 https://story.pxd.co.kr/922

타이포그래피 https://www.youtube.com/watch?v=vJNVramny9k

눈 내리는 효과 https://www.blueb.co.kr/?r=home&c=1/20&m=bluebdata&bid=js_3d&cat=Canvas

로그인 디자인 구현 https://lucidmaj7.tistory.com/251

