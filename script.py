from selenium import webdriver
from selenium.webdriver.common.by import By
import login
import message
import email_list

fireFox= webdriver.Firefox()

fireFox.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=163&ct=1729266350&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26culture%3den-us%26country%3dus%26RpsCsrfState%3d82bdd07e-d4df-cb4c-d4a0-58147fa134dc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")

def loginFunc(xpath1, xpath2, user_info):
    fireFox.implicitly_wait(30)
    login_input= fireFox.find_element(By.XPATH, xpath1)
    login_input.send_keys(user_info)
    login_btn= fireFox.find_element(By.XPATH, xpath2)
    login_btn.click()


#email & password input
loginFunc('//*[@id="i0116"]', '//*[@id="idSIButton9"]', login.email)
loginFunc('//*[@id="i0118"]', '//*[@id="idSIButton9"]', login.password)

#confirmation
conf= fireFox.find_element(By.XPATH, '//*[@id="acceptButton"]')
conf.click()

#send email
def sendEmail(user, subject, content):
    #new email button:
    newEmail_btn= fireFox.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/span/button[1]')
    newEmail_btn.click()

    #email subject
    subject_input= fireFox.find_element(By.XPATH, '//input[@aria-label="Add a subject"]')
    subject_input.click()
    subject_input.send_keys(subject)

    # #email content
    content_input= fireFox.find_element(By.XPATH, "//div[@role='textbox' and @aria-label='Message body, press Alt+F10 to exit']")
    content_input.click()
    content_input.send_keys(content)

    #send to:
    user_input= fireFox.find_element(By.XPATH, '//div[@role="textbox" and @aria-label="To"]')
    user_input.send_keys(user)
    subject_input.click()

    #send email
    sendBtn= fireFox.find_element(By.CSS_SELECTOR, ".ms-Button--primary")
    sendBtn.click()

    fireFox.implicitly_wait(30)



for email in email_list.emails:
    sendEmail(email, message.subject, message.content)


fireFox.quit()