import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

# Set trip options
seed_date = "2018-07-23"
date_range = 3
search_range_in_day = 61
adult_count = 3
start_airport = "ICN"
end_airport = "TAK"

# Set sqlite3
# you should set DB path
# ex) conn = sqlite3.connect("db/test.db")
conn = sqlite3.connect("db/test.db")
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS trips (id integer PRIMARY KEY, start_airport text, end_airport text, price integer, start_date text, end_date text, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)")


# Set Selenium Chrome Driver
# please download chrome driver (http://chromedriver.chromium.org/downloads) and locate it wherever you want.
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# ex) driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
driver.set_page_load_timeout(3000)
driver.implicitly_wait(3)

def search_min_price(d1, d2):
    path = "https://store.naver.com/flights/v2/results?trip=RT&scity1=%s&ecity1=%s&scity2=%s&ecity2=%s&adult=%s&child=0&infant=0&sdate1=%s.&sdate2=%s.&fareType=Y" % (
        start_airport, end_airport, end_airport, start_airport, adult_count, d1, d2)
    driver.get(path)
    try:
        WebDriverWait(driver, 60).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, "tit_apply"))
        )
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        prices = soup.find_all("span", class_="txt_pay")
        driver.get_screenshot_as_file("./dst/success.png")
        price = prices[0]
        price_str = price.get_text(strip="true")
        p = price_str.replace(",", "")
        print(p)
        sql = "INSERT OR IGNORE INTO trips(start_airport, end_airport, price, start_date, end_date) values (?, ?, ?, ?, ?)"
        cur.execute(sql, (start_airport, end_airport, int(p), d1, d2))
        conn.commit()
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        driver.get_screenshot_as_file("./dst/fail.png")

d1 = datetime.date.fromisoformat(seed_date)
d2 = d1 + datetime.timedelta(days=date_range)
d1_string = d1.strftime("%Y.%m.%d")
d2_string = d2.strftime("%Y.%m.%d")

try:
    for i in range(0, search_range_in_day):
        seed_d1 = datetime.date.fromisoformat(seed_date)
        d1 = seed_d1 + datetime.timedelta(days=i)
        d2 = d1 + datetime.timedelta(days=date_range)
        d1_string = d1.strftime("%Y.%m.%d")
        d2_string = d2.strftime("%Y.%m.%d")
        search_min_price(d1_string, d2_string)
except Exception as e:
    print(e)
finally:
    cur.execute("SELECT * FROM trips")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    driver.quit()
    conn.close()
