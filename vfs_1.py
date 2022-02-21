import time
import csv

import pytesseract
import os
import sys
import pydub
import urllib

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from twocaptcha import TwoCaptcha

from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from speech_recognition import Recognizer, AudioFile

from time import sleep
from random import randint

from PIL import Image
from selenium import webdriver
from PIL import Image, ImageFilter
import selenium.common.exceptions as SeleniumExceptions

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
path = os.path.abspath(os.getcwd())

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy = "127.0.0.1:1000"
webdriver.DesiredCapabilities.FIREFOX['proxy']={
    "httpProxy":proxy,
    "ftpProxy":proxy,
    "sslProxy":proxy,
    "noProxy":None,
    "proxyType":"MANUAL",
    "autodetect":False
}

# web driver import with path
browser = webdriver.Chrome("../../Documents/Python_Scripts/chromedriver.exe")
browser.get(
    "https://row1.vfsglobal.com/GlobalAppointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/EpJs2NIweLgQQ8d+rbZm2FGx5CHm/l3tpvUMzs2dkBUvzmr37Un+1CH0C4/6fHwqQ==")
wait = WebDriverWait(browser, 600)

# Assign the value in the field
username_textbox = browser.find_element_by_id("EmailId")
username_textbox.send_keys("vfsdate9@gmail.com")

password_textbox = browser.find_element_by_id("Password")
password_textbox.send_keys("Mr1234567@")

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
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'png')  # saves new cropped image

    captcha = pytesseract.image_to_string(image)
    captcha = captcha.replace(" ", "").strip()
    print("captcha image saved: ",captcha)

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
    time.sleep(5)


# captcha input from terminal
captch = input("Enter the catch number: ")
captch_textbox = browser.find_element_by_id("CaptchaInputText")
captch_textbox.send_keys(captch)

browser.implicitly_wait(30)
# Final button fit for to login
login_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div/form/div[4]/input")
login_button.submit()
print("login Successful")

# print("login Successful")

browser.implicitly_wait(30)

# Click link for to go search
link = browser.find_element_by_link_text('Schedule Appointment')
link.click()
print("Waiting for reload the page")

browser.implicitly_wait(30)
time.sleep(10)
# click dropdown by values
LocationId = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'LocationId'))
)
LocationIdDD = Select(LocationId)
LocationIdDD.select_by_value('217')
print("waiting for relaod the drop-down")

browser.implicitly_wait(30)
# click second dropdown by index
VisaCategoryId = WebDriverWait(browser, 10).until(
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
    visa_date = WebDriverWait(browser, 10).until(
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
continue_button = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[3]/form/div[2]/input'))
)
continue_button.submit()

browser.implicitly_wait(30)
# Add Customer button fit for to login
addCustomer_button = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[3]/a'))
)
addCustomer_button.click()
print("Waiting for Image captcha solution by manual")

# image captcha
time.sleep(50)
# 2captcha solution for recaptcha v3
api_key = os.getenv('APIKEY_2CAPTCHA', '634fbcaa51e41ae95f54251634ffb0ba')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LfDxboZAAAAAD6GHukjvUy6lszoeG3H4nQW57b6',
        url='https://2captcha.com/demo/recaptcha-v2-invisible?level=low')

except Exception as e:
    sys.exit(e)

else:
    # sys.exit('result: ' + str(result))
    print("Captcha is solved", result)

# # trying to solve image captcha
# frames = browser.find_elements_by_id("anchor")
# # browser.switch_to.frame(frames[0])
# sleep(randint(2, 4))
#
# browser.find_element_by_xpath("/html/body/div/div[2]").click()
#
# browser.switch_to.default_content()
#
# frames = browser.find_element_by_xpath(
#     "/html/body/div/div[3]/div[1]").find_elements_by_id("checkbox")
#
# sleep(randint(2, 4))
#
# browser.switch_to.default_content()
#
# frames = browser.find_elements_by_id("checkbox")
#
# browser.switch_to.frame(frames[-1])
#
# browser.find_element_by_id("recaptcha-audio-button").click()
#
# browser.switch_to.default_content()
#
# frames = browser.find_elements_by_id("checkbox")
#
# browser.switch_to.frame(frames[-1])
#
# sleep(randint(2, 4))
# # fixed until this one all the xpath
# browser.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
#
# try:
#     src = browser.find_element_by_id("audio-source").get_attribute("src")
#     print(src)
#     urllib.request.urlretrieve(src, path+"\\audio.mp3")
#
#     sound = pydub.AudioSegment.from_mp3(
#         path+"\\audio.mp3").export(path+"\\audio.wav", format="wav")
#
#     recognizer = Recognizer()
#
#     recaptcha_audio = AudioFile(path+"\\audio.wav")
#
#     with recaptcha_audio as source:
#         audio = recognizer.record(source)
#
#     text = recognizer.recognize_google(audio, language="de-DE")
#
#     print(text)
#
#     inputfield = browser.find_element_by_id("audio-response")
#     inputfield.send_keys(text.lower())
#
#     inputfield.send_keys(Keys.ENTER)
#
#     sleep(10)
#     print("Success")
#     browser.quit()
# except NameError:
#     print("Failed")
#     print(NameError)

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
continue_button2 = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(By.XPATH, ("/html/body/div[2]/div[1]/div[3]/div[4]/form/div[2]/input"))
)
continue_button2.submit()

# add again if there is another new customer

# continue button again after get the total price of visa schedule
continue_button3 = WebDriverWait(browser, 10).until(
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
browser.close()
# Restart

# quit()
