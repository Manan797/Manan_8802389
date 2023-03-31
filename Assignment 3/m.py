# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Royal Paan homepage
driver.get("https://royalpaan.com/")
driver.maximize_window()  # Maximizing the browser window
time.sleep(5)

# Clicking on the "Menu" link on the header
Menu_link = driver.find_element("xpath","/html/body/div[1]/header/div/div/div/section/div/div/div[2]/div/div/div/div/div/nav/ul/li[2]/a")
Menu_link.click()

# Waiting for the page to load
time.sleep(5)

# Clicking on Street Food Bar link
Street_food_Bar_link = driver.find_element("xpath","/html/body/div[1]/section[2]/div[1]/div/div/div/div/div[1]/div/div[1]/ul/li[3]/a/span")
Street_food_Bar_link.click()

# Waiting for the page to load
time.sleep(5)

# # Clicking on Discover Entire Menu
# # Product_link = driver.find_element_by_css_selector("span[data-component-type='s-product-image'] a")
menu_link = driver.find_element("xpath","/html/body/div[1]/section[2]/div[1]/div/div/div/div/div[2]/a")
# # Product_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
menu_link.click()
#
#
# # Waiting for the product details page to load
time.sleep(5)


# Clicking on the Online Order button
order_online_button = driver.find_element("xpath", "/html/body/app-root/app-outlets/div/div[1]/div/div[2]/div/a")
order_online_button.click()

# Waiting for the size selection to take effect
time.sleep(5)

#
# # # Clicking on okay button
Close_button = driver.find_element("xpath","/html/body/div[2]/div[2]/div/mat-dialog-container/sceduledeliverydialog/div/mat-drawer-container/mat-drawer-content/mat-tab-group/div/mat-tab-body/div/div/button")
Close_button.click()
# time.sleep(5)
#
# # # Clicking on the login button
# Login_button = driver.find_element("xpath","/html/body/div[2]/div[2]/div/mat-dialog-container/sceduledeliverydialog/div/mat-drawer-container/mat-drawer-content/mat-tab-group/div/mat-tab-body/div/div/button")
# Login_button.click()
# time.sleep(5)
#
#
# # Closing the webdriver
# driver.quit()
