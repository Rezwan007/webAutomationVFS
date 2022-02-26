import time
import csv

import pytesseract
import os
import sys

import random
import socket
import struct

from twocaptcha import TwoCaptcha

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
path = os.path.abspath(os.getcwd())

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
'197.38.59.143'
socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
'228.237.175.64'

# PROXY="176.9.119.170:8080"
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "proxyType": "MANUAL",
#
# }
# webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True

url = "https://row1.vfsglobal.com/GlobalAppointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/EpJs2NIweLgQQ8d+rbZm2FGx5CHm/l3tpvUMzs2dkBUvzmr37Un+1CH0C4/6fHwqQ=="
extension = "https://chrome.google.com/webstore/detail/hcaptcha-solver/lfpfbgeoodeejmjdlfjbfjkemjlblijg"
# web driver import with path
# browser = webdriver.Chrome("../../Documents/Python_Scripts/chromedriver.exe")


# add extension from chrome
chrome_options = Options()
chrome_options.add_extension('C:/Users/Rezwan/PycharmProjects/webAutomationVFS/ex/hcaptcha.crx')
browser = webdriver.Chrome(options=chrome_options, executable_path='../../Documents/Python_Scripts/chromedriver')

browser.get(url)
time.sleep(20)
# Assign the value in the field
# usernameinput = input("Please enter your EmailId")
username_textbox = browser.find_element_by_id("EmailId")
username_textbox.send_keys("utsha1234@gmail.com")
# username_textbox.send_keys(usernameinput)

# passwordinput = input("Please Enter your Password")
password_textbox = browser.find_element_by_id("Password")
password_textbox.send_keys("Rezwan@007")
# password_textbox.send_keys(passwordinput)

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


# change frame
# browser.switch_to.frame("Main")

def get_captcha(driver, element, path):
    element = browser.find_element_by_id("CaptchaImage")
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y'] + 120
    right = location['x'] + size['width'] + 140
    bottom = location['y'] + size['height'] + 140

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'png')  # saves new cropped image

    captcha = pytesseract.image_to_string(image)
    captcha = captcha.replace(" ", "").strip()
    print("captcha image saved: ", captcha)


# download image/captcha
img = browser.find_element_by_id("CaptchaInputText")
get_captcha(browser, img, "captcha.png")

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

api_key = os.getenv('APIKEY_2CAPTCHA', '634fbcaa51e41ae95f54251634ffb0ba')

solver = TwoCaptcha(api_key)

try:
    result = solver.normal('captcha.png')

except Exception as e:
    sys.exit(e)

else:
    # sys.exit('solved: ' + str(result))
    print("Captcha is:", result)
    print("Captcha is:", result['code'])
    # print("Captcha code is:" result(code))
    time.sleep(5)

captch_textbox = browser.find_element_by_id("CaptchaInputText")
solution = result['code']
captch_textboxdd = ActionChains(browser)
captch_textboxdd.move_to_element(captch_textbox).click()
# action.click()
captch_textboxdd.key_down(Keys.SHIFT)
captch_textboxdd.send_keys(solution)
captch_textboxdd.key_up(Keys.SHIFT)
captch_textboxdd.perform()
time.sleep(5)  # waiting is mandatory

browser.implicitly_wait(30)
# Final button fit for to login
login_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div/form/div[4]/input")
login_button.submit()
print("login Successful")

# print("login Successful")

browser.implicitly_wait(30)
# Click link for to go search
link = browser.find_element_by_xpath('//*[@id="Accordion1"]/div/div[2]/div/ul/li[1]/a')
link.click()
print("Waiting for reload the page")

browser.implicitly_wait(30)
time.sleep(15)
# click dropdown by values
LocationId = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.NAME, 'LocationId'))
)
LocationIdDD = Select(LocationId)
LocationIdDD.select_by_value('448')
print("waiting for relaod the drop-down")

time.sleep(10)
browser.implicitly_wait(30)
# click second dropdown by index
VisaCategoryId = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.NAME, 'VisaCategoryId'))
)
VisaCategoryIdDD = Select(VisaCategoryId)
VisaCategoryIdDD.select_by_value('3437')
print("Waiting for earliest date of visa schedule")

browser.implicitly_wait(30)
# Click in the link for Schedule of visa
try:
    # link2 = browser.find_element_by_link_text('Click here to know the earliest available date')
    # print(link2)
    # wait 10 seconds before looking for element
    visa_date = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="trNonPrime"]/td[1]'))
    )
    print(visa_date.text)
    print("Succefully clicking on the link for visa schedule")
except:
    print("Waiting for the visa schedule date")
    browser.quit()
    # Pick the date for earliest visa schedule
    # visa_date = browser.find_element(By.XPATH,'//*[@id="trNonPrime"]/td[1]')
    # print(visa_date.text)

print('*' * 10)

browser.implicitly_wait(30)
# print some text of update work
print("Now final click for the schedule")
continue_button = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[3]/form/div[2]/input'))
)
continue_button.submit()

browser.implicitly_wait(30)
# Add Customer button fit for to login
addCustomer_button = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[3]/a'))
)
addCustomer_button.click()
print("Waiting for Image captcha solution by manual")

# image captcha
# time.sleep(50)
# browser.execute_script("document.getElementByName('h-recaptcha-response').style.display = 'block';")
# # browser.execute_script("documents.getElementByXpath('textarea[@name='h-captcha-response'].style.display='block')")
# browser.find_element_by_xpath("textarea[@name='h-captcha-response']").send_keys(result['captchaId'])
# browser.execute_script("document.getElementByName('h-recaptcha-response').style.display = 'block';")
# # browser.execute_script("documents.getElementByXpath('textarea[@name='h-captcha-response'].style.display='block')")
# browser.find_element_by_xpath("textarea[@name='h-captcha-response").send_keys(result['code'])
# browser.execute_script("document.getElementByName('h-recaptcha-response').style.display = 'none';")
# # browser.execute_script("documents.getElementByXpath('textarea[@name='h-captcha-response'].style.display='none')")
# 2captcha solution for recaptcha v3
api_key = os.getenv('APIKEY_2CAPTCHA', '634fbcaa51e41ae95f54251634ffb0ba')

solver = TwoCaptcha(api_key)

try:
    result = solver.hcaptcha(
        sitekey='33f96e6a-38cd-421b-bb68-7806e1764460',
        url='https://2captcha.com/demo/hcaptcha?difficulty=easy',
        proxy={
            'type': 'HTTPS:',
            'uri': 'login:password@127.0.0.2:1000'
        }
    )

except Exception as e:
    sys.exit(e)

else:
    # sys.exit('result: ' + str(result))
    print("Captcha is solved:", result)
    print("Captcha ID is:", result['captchaId'])
    print("Captcha code is:", result['code'])

    browser.execute_script(f"document.getElementsByName('h-captcha-response')[0] = '{result['captchaId']}';")
    time.sleep(1)
    browser.execute_script(f"document.getElementsByName('h-recaptcha-response')[1] = '{result['code']}';")
    time.sleep(1)
    browser.execute_script("document.getElementById('challenge-form').submit();")
    # XPATH of textarea = //textarea[@name='h-captcha-response']
    # recaptchafield.send_keys(recaptchafield)
    # recaptchafield.send_keys(recaptchafield.higher())
    # recaptchafield.keys_down(Keys.ENTER)

# recaptchafield = input("Enter the reCatch code: ")
# recaptchafieldinput = browser.find_element_by_id("h-captcha-response-1mqwulue1iv")
# recaptchafieldinput.send_keys(recaptchafield)
# recaptchafieldinput.send_keys(Keys.ENTER)
#
# checkboxforHcaptcha= browser.find_element_by_id("checkbox").click()
time.sleep(50)

# Web automation from CSV
browser.implicitly_wait(30)
time.sleep(10)
print("Wait couple of min")
browser.implicitly_wait(30)
with open('Add_New_Customer.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    try:
        for line in csv_reader:
            # Passport Number
            passport_number = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[1]/div[2]/input')
            passport_number.send_keys(line[0])
            browser.implicitly_wait(30)

            # Date of Birth
            DOB = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/form/div[2]/div[2]/input')
            DOB.send_keys(line[1])
            browser.implicitly_wait(30)

            # Passport Expiry date
            Passport_Expiry_Date = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[3]/div[2]/input')
            Passport_Expiry_Date.send_keys(line[2])
            browser.implicitly_wait(30)

            # Nationality Select
            NationalityId = browser.find_element_by_name('NationalityId')
            NationalityIdDD = Select(NationalityId)
            NationalityIdDD.select_by_value('11')
            browser.implicitly_wait(30)

            # Fiirst name
            First_name = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[5]/div[2]/input').clear()
            # First_name.clear()
            browser.implicitly_wait(30)
            # First_name.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
            First_name = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[5]/div[2]/input')
            First_name.send_keys(line[4])
            # First_name.sendKeys(Keys.chord(Keys.CONTROL, "a"), [4]);
            browser.implicitly_wait(30)

            # Last Name
            Last_name = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[6]/div[2]/input').clear()
            # Last_name.clear()
            browser.implicitly_wait(30)
            # Last_name.sendKeys(Keys.chord(Keys.CONTROL, "a"), line[5]);
            Last_name = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/form/div[6]/div[2]/input')
            Last_name.send_keys(line[5])
            browser.implicitly_wait(30)

            # Select Gender
            GenderId = browser.find_element_by_name('GenderId')
            GenderIdDD = Select(GenderId)
            GenderIdDD.select_by_value('1')
            browser.implicitly_wait(30)

            # Country Code
            Country_code = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[1]').clear()
            # Country_code.clear()
            time.sleep(2)
            # Country_code.send_keys(Keys.chord(Keys.SHIFT, "="), line[7]);
            Country_code = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[1]')
            Country_code.send_keys("+88")
            browser.implicitly_wait(30)

            # Mobile Number Without 0
            Mobile_Number = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[2]').clear()
            # Mobile_Number.clear()
            browser.implicitly_wait(30)
            # Mobile_Number.sendKeys(Keys.chord(Keys.CONTROL, "a"), [9]);
            Mobile_Number = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[2]')
            Mobile_Number.send_keys(line[9])

            # Email address
            Email = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[9]/div[2]/input').clear()
            browser.implicitly_wait(30)
            Email = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/form/div[9]/div[2]/input')
            Email.send_keys(line[8])
            browser.implicitly_wait(30)

            # Click for final submit button
            print("Click for submit button")
            submit_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div[3]/div[4]/form/div[12]/input[2]")
            submit_button.submit()
            time.sleep(10)

            browser.implicitly_wait(30)
    except:
        browser.start_client()

# Continue button after add new customer
continue_button2 = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located(By.XPATH, ("/html/body/div[2]/div[1]/div[3]/div[4]/form/div[2]/input"))
)
continue_button2.submit()

WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()
print("alert accepted")

# continue button again after get the total price of visa schedule
continue_button3 = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located(By.XPATH, ("/html/body/div[2]/div[1]/div[3]/div[12]/input"))
)
continue_button3.submit()
browser.implicitly_wait(30)

# picking date from calender
# browser.switchTo().frame(0);

# browser.implicitly_wait(2)
# browser.maximize_window()
#
# browser.findElement(By.id("datepicker")).click();
# browser.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
#
# dateWidget = browser.find_element_by_id("ui-datepicker-div")
# rows = dateWidget.find_elements_by_tag_name("tr")
# columns = dateWidget.find_elements_by_tag_name("td")
#
# for cell in columns:
#     if cell.gettext().equal('10'):
#         cell.find_element_by_link_text('10').click()
#         break
# exit

# RBG selected date XPATH: //div[@id='calendar']//td[@style='background-color: rgb(188, 237, 145); cursor: pointer;']
# all the date XPATH: //div[@id='calendar']//td[@class]//div[@class='fc-day-number']
# selected date using date-date: //td[@data-date]

date_date_start= input("Please input the starting date")


alldates= browser.find_element(By.XPATH,"//div[@id='calendar']//td[@class]//div[@class='fc-day-number']")
rbgdates= browser.find_element(By.XPATH, "//div[@id='calendar']//td[@style='background-color: rgb(188, 237, 145); cursor: pointer;']")

for dateelement in alldates:
    date=dateelement.text
    print(date)
    if date== rbgdates:
        dateelement.click()
        selecttime= browser.find_elements(By.XPATH,"//input[@name='selectedTimeBand']")
        selecttime.click()
        scheduletime= browser.find_elements(By.XPATH, "//td[@style='text-align:center']")
        scheduletimetxt=scheduletime.text
        print(scheduletimetxt)
    else:
        print("Date Not found")
    break

# confirm button after get the schedule date
confirmButton= browser.find_element(By.XPATH, "//input[@value='Confirm']")
confirmButton.click()

# ajax confirmation

#
browser.close()
# Restart

# quit()
