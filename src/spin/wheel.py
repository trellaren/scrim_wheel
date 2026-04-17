from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def populateWheelOfNames(playersToRollOutList):
    browser = webdriver.Firefox()
    browser.get(f"https://www.wheelofnames.com/")

    wheelNames = element = browser.find_element(By.CSS_SELECTOR, "[role='textbox']")
    wheelNames.clear()
    for player in playersToRollOutList:
        wheelNames.send_keys(player)
        wheelNames.send_keys("\n")
    
def closeBrowser():
    browser.Close()