from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 표시 제거
options.add_experimental_option('useAutomationExtension', False)  # 자동화 확장 기능 사용 안 함
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# driver.find_element(By.LINK_TEXT,"MediaWiki").click()
search = driver.find_element(By.CLASS_NAME, "#search")
search.send_keys("python")

