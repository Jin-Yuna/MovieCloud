# 1. 시작하기

```bash
python -m venv venv
source venv/Scripts/activate 
```

```bash
pip -r requirements.txt   (변동이 있으면 꼭 freeze)
```

```bash
python manage.py loaddata 데이터파일이름
```

- 데이터 =>  movie의 fixture안에 있습니다.
- 모든 영화 데이터 => movie.json 
- test는 데이터 데이터를 조금만 넣었습니다. `test.json`(장르이름버전)  `test2.json`(장르 번호 버전)
- 장르 번호 버전은 쓰려면 장르 테이블 필요(지금은 없음)

