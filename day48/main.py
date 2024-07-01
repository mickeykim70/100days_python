from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

options = Options()
options.add_argument("disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 표시 제거
options.add_experimental_option('useAutomationExtension', False)  # 자동화 확장 기능 사용 안 함
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.amazon.com/Razer-DeathAdder-HyperSpeed-Wireless-Esports/dp/B0D4RF55QK/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.ymhoPooutCjkAYGYCOy8bssCYhnJCucTklYwTivnzR1gpqCPTYccehRx-5chRlYxHCjBH0gOucN0QcFmkpqB4X7hxdQrfPRbvMPh99o23m55zltmjxc6DJ4dBUwOZC9QWH94z-Tx1occFR89lFng9kcaoLCeT0f5OMwDAUO8JNwNy7lWe45zVODiZsDptX2X9ApLVELvFMwc4KQI-KCWp1i4bKTSVbwQki7Fbt40qRc.VfdBkQ8S7xr8KkQ-rUpnKcxJk7xnVJ6NScH7fktSKZI&dib_tag=se&keywords=gaming+mouse&pd_rd_r=013ee884-4f31-460a-9cb9-da79e2728065&pd_rd_w=yyUlY&pd_rd_wg=Be0xj&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=NQH0XBXCWHN99F0ZRWT3&qid=1719672991&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# input()

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(price_dollar.text)
print(price_cents.text)

# 쿠키저장
# cookies = driver.get_cookies()
# with open("cookies.json", "w") as file:
#     json.dump(cookies, file)

driver.quit()




