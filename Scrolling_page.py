from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
browser.maximize_window()

#By pixel approach
#browser.execute_script("window.scrollBy(0,1500)","")

#Till finding a element apprach
#element = browser.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
#browser.execute_script("arguments[0].scrollIntoView();", element)

#till page end appraoch
browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
browser.quit()