import requests
from bs4 import BeautifulSoup
from pprint import pprint
#url을 구분할 월~일요일 배열
weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#파일작성모드로 열기
f = open("C:\\Users\\Public\\Documents\\Webtoon.txt", 'w')
#월~일까지 반복
for day in weekday:
    #url 끝에 요일 배열 추가
    url = f"https://comic.naver.com/webtoon/weekdayList.nhn?week={day}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    html.close()
    #웹툰리스트 div
    div_link = soup.find('div', {'class':'list_area daily_img'})
    #한개의 웹툰 div - dl
    dl_link = div_link.findAll('dl')
    #요일 출력
    f.write(f"{day}day\n")
    for dl in dl_link:
        #제목 dl - dt - a - title
        dt_link = dl.findAll('dt')
        for dt in dt_link:
            dt_a = dt.select('a')
            for a in dt_a:
                dt_text = a.get('title') #title속성
        #작가 dl - dd - a
        dd_link = dl.findAll('dd',{'class':'desc'})
        for dd in dd_link:
            a_link = dd.find('a')
        #별점 dl - a
        star = dl.findAll('strong')
        #웹툰정보출력
        i = 0
        f.write(f"제목 :{dt_text}, 작가 :{a_link.text}, 별점 :{star[i].text}\n")
        i += 1
    print(end="\n")
#파일닫기
f.close()