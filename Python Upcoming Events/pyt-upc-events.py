from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
#create new driver from webdriver module
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

## using CSS Selector
upc_events_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
#print(upc_events_time.get_attribute("datetime"))
event_date = [i.text for i in upc_events_dates]
print(event_date)

upc_events_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
#print(upc_events_name.get_attribute("innerHTML"))
event_title = [i.text for i in upc_events_name]
print(event_title)

events = {}

for j in range(len(event_date)):
  events[j] = {
    "time": event_date[j],
    "name": event_title[j]
  }
  
print(events)

driver.quit()


