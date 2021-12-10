from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(r"C:\Users\91638\chromedriver.exe")
browser.get("https://sqengineer.com/practice-sites/practice-tables-selenium/")
rows = len(browser.find_elements(By.XPATH,"//*[@id='table1']/tbody/tr"))
cols = len(browser.find_elements(By.XPATH,"//*[@id='table1']/tbody/tr[1]/th"))

print("Number of rows:",rows)
print("Number of columns:",cols)

#to print the table
print("Automation Tool"+"            "+"Type"+"                        "+"Link")
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = browser.find_element(By.XPATH,"//*[@id='table1']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end="                  ")
    print()


