from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import argv


import time
PATH = "C:/Users/Oscar/Documents/ocpp/chromedriver-win64/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Here
driver = webdriver.Chrome(options=options)




driver.get("https://www.facebook.com/groups/1112645443487341/members")
time.sleep(5)
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/form/div/div[2]/input"))
    )
username = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/form/div/div[2]/input")
password = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/form/div/div[4]/input")

password.clear()
username.clear()
username.send_keys("oscarhychan@gmail.com")

password.send_keys("s28571199")
password.send_keys(Keys.RETURN)
time.sleep(1000)

driver.close()

print("logged")

#  results = driver.find_elements(By.CLASS_NAME,"css-xumdn4")
#  for k in range(20):
#      results = []
#      for i in range(100):
#          results = results + driver.find_elements(By.CLASS_NAME,"css-xumdn4")
#          click_count = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[3]/button[2]').click()
#         time.sleep(1)
#         with open(f'output_{k+1}.txt', 'w') as file:
#             for i, result in enumerate(results):
#                 file.write(str(result.text))
#                 if (i+1) % 8 == 0:
#                     file.write('\n')
#                 else:
#                     file.write(', ')

    # if (i+1) % 8 == 0:
    #      print(" ")

# with open("output.txt", "w") as file:
#     file.write(results)

# file.close()


# for i, result in enumerate(results):
#     print(result.text, end=", ")
#     if (i+1) % 8 == 0:
#          print(" ")

