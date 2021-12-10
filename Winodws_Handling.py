from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("http://demo.automationtesting.in/Windows.html")
browser.maximize_window()

browser.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

pages = browser.window_handles
#to get the name of the opened pages in the browser
for page in pages:
    browser.switch_to.window(page)
    print(browser.title)

#switch to the child window
browser.switch_to.window(pages[1])
browser.find_element(By.XPATH,"/html/body/div/main/section[2]/div/div/div[1]/div/div[2]/div/a").click()

browser.quit()