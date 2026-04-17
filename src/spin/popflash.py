from typing import final

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# TODO: Refactor - headless
# TODO: Refactor element finder


name = "fragworks"

browser = webdriver.Firefox()
browser.get(f"https://www.popflash.site/-/{name}/scrim")

def getActivePlayers(name):
    browser.get(f"https://www.popflash.site/-/{name}/scrim")
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/user/')]"))
        )
    finally:
        pass
    player_names = browser.find_elements(By.CSS_SELECTOR, "[class*='min-h-[48px]'")
    players = [player.get_attribute("innerText") for player in player_names if player.get_attribute("innerText")]
    uniquePlayers = []
    for player in players:
        pl = player.partition('\n')[0]
        if pl not in uniquePlayers:
            uniquePlayers.append(pl)
        if pl == 'Join GOTV Spectators':
            uniquePlayers.remove(pl)
    return uniquePlayers


def getLastMatch(name):
    lastMatchPlayers = []
    browser.get(f"https://www.popflash.site/-/{name}/matches")
    lastMatchLink = browser.find_element(By.XPATH, "//a[contains(@href, '/match/')]").get_attribute("href")
    # lastMatchID = browser.find_element(By.XPATH, "//div[contains(., 'Match #')]")
    return lastMatchLink

def getLastMatchPlayerNames(lastMatchLink):
    browser.get(lastMatchLink)
    playerNames = browser.find_elements(By.XPATH, "//a[contains(@href, '/user/')]")
    players = [player.get_attribute("innerText") for player in playerNames if player.get_attribute("innerText")]
    uniquePlayers = []
    for player in players:
        if player not in uniquePlayers:
            uniquePlayers.append(player)
    return uniquePlayers


def getLastMatchPlayerURLs(lastMatchLink):
    browser.get(lastMatchLink)
    link_elems = browser.find_elements(By.XPATH, "//a[contains(@href, '/user/')]")
    links = [link.get_attribute("href") for link in link_elems if link.get_attribute("href")]
    uniqueUrls = []
    for player in links:
        if player not in uniqueUrls:
            uniqueUrls.append(player)
    return uniqueUrls

def moveIdiot(player, action):
    ### Would need to authenticate with steam login to make this functional... and I don't wanna...
    browser.get(f"https://www.popflash.site/-/{name}/scrim")
    wait = WebDriverWait(browser, 10)

    # TODO Click hamburger button
    idiot = wait.until(
        EC.presence_of_element_located(
            browser.find_element(
                By.XPATH, "//a[contains(@href), 'user/33896']"
        )))
    print("Hamburger")
    # TODO from dropdown perform action (either swapteams, or move to waiting room)
    dropdownButton = idiot.find_element(By.TAG_NAME, "svg").get_attribute("outerHTML")
    dropdownButton.click()
    # TODO check if waiting room hamburger is different
    pass

def rollOutPlayers(newPlayersList, OldPlayersList):
    # TODO Get Count of newplayers
    # TODO iterate list of oldplayers (len(newPLayersList)) and select someone randomly to be rolled out
    pass

def closeBrowser():
    browser.close()