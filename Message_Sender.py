# Whatsapp bot! [Message Sender]

# Mohammadreza.D
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Python Version : 3.9.6
# Selenium Version : 21.2.4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
# Developer name : *_* Every Developer *_*
# Github >>>...  https://github.com/Every-Developer
# _________________________________________________________#


from selenium import webdriver

import time


# INPUT YOUR INFORMATIONS
Contacts = input('Enter Contacts names [Separate with a comma(,) ] : ')
one_name = Contacts.split(',')

Contacts = list(one_name)
# __________________________________________

message = input('Type a text message : ')

count = int(input('How many time ??? : '))

input('Enter Anything ... /')

# The interval between sending messages
stop = 0.2

# Open Microsoft Edge Driver
driver = webdriver.Edge()

driver.get('https://web.whatsapp.com/')

time.sleep(12)

# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

for Contact_name in Contacts:

    # CONTACTS INFO
    User_name = driver.find_element_by_xpath(
            f'//span[@title="{Contact_name}"]')  # //*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div[2]/div[1]/div[1]/span/span

    time.sleep(1)
    User_name.click()

    Text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')

    for i in range(count):

        Text_box.send_keys(message)

        Send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

        time.sleep(stop)
        Send_button.click()


# END OF BOT