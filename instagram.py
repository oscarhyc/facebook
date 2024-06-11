from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import argv
import time

import time
PATH = "C:/Users/Oscar/Documents/ocpp/chromedriver-win64/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Here
driver = webdriver.Chrome(options=options)




driver.get("https://www.instagram.com/bowjaiiiii/")

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/div/div/div/div[1]/a')))
time.sleep(5)
print("1")

driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/div/div/div/div[1]/a').click()
#driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[5]/button/span[2]').click()
time.sleep(5)
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]'))
    )
print("2")
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[5]/button/span[2]').click()
time.sleep(5)
element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button'))
    )
username = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input')

password = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input')

password.clear()
username.clear()
username.send_keys("oscarhychan@gmail.com")

password.send_keys("s28571199")
password.send_keys(Keys.RETURN)
time.sleep(20)
print("3")
#WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')))
print("4")
imgs = driver.find_elements((By.CSS_SELECTOR,"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div._aatk._aatl > div > div._aamn > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x10l6tqk.x1ey2m1c.x13vifvy.x17qophe.xds687c.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > div > ul > li:nth-child(2) > div > div > div > div > div._aagu._aa20._aato > div._aagv > img"))
for img in  imgs:
    print(img.get_attribute("src"))
driver.close()

print("3")

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

