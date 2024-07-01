from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 표시 제거
options.add_experimental_option('useAutomationExtension', False)  # 자동화 확장 기능 사용 안 함
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.python.org/")


event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}
for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }


print(events)


