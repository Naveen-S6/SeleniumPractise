from selenium import webdriver
import time
browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
browser.maximize_window()
time.sleep(2)
#to swtich to the first frame
browser.switch_to.frame("packageListFrame")
browser.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(2)
#switch to webpage
browser.switch_to.default_content()
time.sleep(2)
#switch to another frame
browser.switch_to.frame("packageFrame")
browser.find_element_by_link_text("WebDriver").click()
time.sleep(2)
#switch to webpage
browser.switch_to.default_content()
time.sleep(2)
#switch to another frame
browser.switch_to.frame("classFrame")
browser.find_element_by_partial_link_text("TR").click()
time.sleep(2)
browser.get_screenshot_as_file("Screentshot_Frame.png")
time.sleep(2)
browser.quit()