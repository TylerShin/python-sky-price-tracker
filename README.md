# SKY PRICE CRAWELR
일정 기간을 기준으로 가장 저렴한 항공권 가격을 알 수 있도록 도와주는 프로젝트입니다.

## Background
최저권 항공가 서비스들은 대부분 출발일과 도착일을 기준으로 검색해주고 있습니다.  
동시에 많은 직장인들은 휴가 일자가 n일로 한정되어 있습니다.  

그렇다면 휴가가 5일이라고 했을 때, 도쿄에 최저가로 가고 싶으면 어떻게 해야할까요?  
본인이 휴가를 떠날 수 있는 범위 (ex: 7~8월) 동안에,  
출발일-도착일이 5일 차이나는 집합을 하나씩 다 확인해봐야 최저가에 가까운 가격을 알 수 있을 겁니다.  

본 프로젝트는 이러한 불편함을 최소화시키고자 시작되었습니다.  

## How to use
**Requirements**
- Python 3+
- [Chrome Driver](http://chromedriver.chromium.org/downloads)
- [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium WebDriver Python](https://selenium-python.readthedocs.io/)

**Run the project**
1. 필요한 모듈과 프로그램을 모두 설치합니다.

2. `main.py` 파일을 열고 실행환경을 설정합니다.
    - SQLite3 에서 DB로 사용할 파일 path를 설정합니다. 필요하다면 디렉토리도 만들어줍니다.
    - ChromeDriver 실행파일의 위치를 지정합니다.
     
3. `main.py` 파일에서 검색하고 싶은 옵션을 선택합니다.
    - `seed_date = "2018-07-23"` 여행이 가능한 날짜
    - `date_range` = 3 여행 기간 (귀국일 - 출발일)
    - `search_range_in_day` = 61 (seed 날짜부터 검색할 날의 수. 61이면 seed 날짜에서 2달 후까지의 모든 일자를 검색함)
    - `adult_count` = 3 여행 인원(어른 기준)
    - `start_airport` = "ICN" 출발 공항(ICN = 인천)
    - `end_airport` = "TAK" 도착 공항(공항마다 다름)
    
    
 ## Contribute
 Welcome all of your contributes.  
 Just make PR or issue for this project.  
 thanks.
 
 