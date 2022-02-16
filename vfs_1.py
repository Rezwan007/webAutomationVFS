import time
import csv
import pytesseract

from selenium import webdriver

from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys

from PIL import Image
from selenium import webdriver
from PIL import Image, ImageFilter
import selenium.common.exceptions as SeleniumExceptions

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# web driver import with path
browser = webdriver.Chrome("../../Documents/Python_Scripts/chromedriver.exe")
browser.get(
    "https://row1.vfsglobal.com/GlobalAppointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/EpJs2NIweLgQQ8d+rbZm2FGx5CHm/l3tpvUMzs2dkBUvzmr37Un+1CH0C4/6fHwqQ==")
wait = WebDriverWait(browser, 600)

# Assign the value in the field
username_textbox = browser.find_element_by_id("EmailId")
username_textbox.send_keys("utsha1234@gmail.com")

password_textbox = browser.find_element_by_id("Password")
password_textbox.send_keys("Rezwan@007")

time.sleep(5)
# browser.switch_to.frame("main")

def get_captcha(driver, element, path):
    imageCaptcha = browser.find_element_by_id("CaptchaImage")
    time.sleep(2)
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = imageCaptcha.location
    size = imageCaptcha.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']-5
    top = location['y']+10
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'png')  # saves new cropped image

    captcha = pytesseract.image_to_string(image)
    captcha = captcha.replace(" ", "").strip()
    print(captcha)

    # download image/captcha
    img = browser.find_element_by_id("CaptchaInputText")
    # img.send_keys(captcha)
    get_captcha(browser, img, "captcha.png")

# except:
#     captch = input("Enter the catch number: ")
#     captch_textbox = browser.find_element_by_id("CaptchaInputText")
#     captch_textbox.send_keys(captch)


time.sleep(50)
# Final button fit for to login
login_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div/form/div[4]/input")
login_button.submit()

print("login Successful")

time.sleep(10)

# Click link for to go search
link = browser.find_element_by_link_text('Schedule Appointment')
link.click()
print("Waiting for reload the page")

time.sleep(10)
# click dropdown by values
LocationId = browser.find_element_by_name("LocationId")
LocationIdDD = Select(LocationId)
LocationIdDD.select_by_value('217')
print("waiting for relaod the drop-down")

time.sleep(10)
# click second dropdown by index
VisaCategoryId = browser.find_element_by_name('VisaCategoryId')
VisaCategoryIdDD = Select(VisaCategoryId)
VisaCategoryIdDD.select_by_value('3437')
print("Waiting for earliest date of visa schedule")

time.sleep(10)
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

time.sleep(5)
# print some text of update work
print("Now final click for the schedule")
continue_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[3]/form/div[2]/input")
continue_button.submit()

time.sleep(10)
# Add Customer button fit for to login
addCustomer_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[3]/a")
addCustomer_button.click()

time.sleep(5)
# Web automation from CSV
print("Wait couple of min")

time.sleep(5)
with open('Add_New_Customer.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    try:
        for line in csv_reader:
            # Passport Number
            passport_number = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[1]/div[2]/input')
            passport_number.send_keys(line[0])
            time.sleep(2)

            # Date of Birth
            DOB = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/form/div[2]/div[2]/input')
            DOB.send_keys(line[1])
            time.sleep(2)

            # Passport Expiry date
            Passport_Expiry_Date = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[3]/div[2]/input')
            Passport_Expiry_Date.send_keys(line[2])
            time.sleep(2)

            # Nationality Select
            NationalityId = browser.find_element_by_name('NationalityId')
            NationalityIdDD = Select(NationalityId)
            NationalityIdDD.select_by_value('11')
            time.sleep(2)

            # Fiirst name
            First_name = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[5]/div[2]/input').clear()
            # First_name.clear()
            time.sleep(2)
            # First_name.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
            First_name = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[5]/div[2]/input')
            First_name.send_keys(line[4])
            # First_name.sendKeys(Keys.chord(Keys.CONTROL, "a"), [4]);
            time.sleep(2)

            # Last Name
            Last_name = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[6]/div[2]/input').clear()
            # Last_name.clear()
            time.sleep(2)
            # Last_name.sendKeys(Keys.chord(Keys.CONTROL, "a"), line[5]);
            Last_name = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/form/div[6]/div[2]/input')
            Last_name.send_keys(line[5])
            time.sleep(2)

            # Select Gender
            GenderId = browser.find_element_by_name('GenderId')
            GenderIdDD = Select(GenderId)
            GenderIdDD.select_by_value('1')
            time.sleep(2)

            # Country Code
            Country_code = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[1]').clear()
            # Country_code.clear()
            time.sleep(2)
            # Country_code.send_keys(Keys.chord(Keys.SHIFT, "="), line[7]);
            Country_code = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[1]')
            Country_code.send_keys("+88")
            time.sleep(2)

            # Mobile Number Without 0
            Mobile_Number = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[2]').clear()
            # Mobile_Number.clear()
            time.sleep(2)
            # Mobile_Number.sendKeys(Keys.chord(Keys.CONTROL, "a"), [9]);
            Mobile_Number = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[8]/div[2]/input[2]')
            Mobile_Number.send_keys(line[9])

            # Email address
            Email = browser.find_element_by_xpath(
                '/html/body/div[2]/div[1]/div[3]/div[4]/form/div[9]/div[2]/input').clear()
            time.sleep(2)
            Email = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/form/div[9]/div[2]/input')
            Email.send_keys(line[8])
            time.sleep(2)

            # Click for final submit button
            print("Click for submit button")
            submit_button = browser.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div[3]/div[4]/form/div[12]/input[2]")
            submit_button.submit()

            time.sleep(20)
    except:
        browser.start_client()

time.sleep(20)
# exit
browser.close()
# Restart

# quit()
