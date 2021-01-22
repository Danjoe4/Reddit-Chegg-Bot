# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:51:05 2020

@author: Daniel Broderick
"""
from selenium import webdriver
import yaml
import time


conf = yaml.full_load(open("hidden.yml"))
#  vars for the log in
CheggID = conf["Chegg_main"]["id"]
CheggPassword = conf["Chegg_main"]["password"]

chromeOptions = webdriver.ChromeOptions()
prefs = {'safebrowsing.enabled': 'false'}
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome()
#driver = webdriver.Chrome(chrome_options=chromeOptions,
 #                         executable_path=r"C:\Windows\1- PROJECT RESOURCES (in path)\chromedriver.exe")




def login_chegg(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()
    try:
        driver.find_element_by_id("MainContent_RptrAthleteForms_rblYesCHecked_1_1_1")
    except:
        driver.find_element_by_id("cmdScreening").click()



login_chegg("http://chegg.com/auth?action=login", "emailForSignIn", 
            CheggID, "passwordForSignIn", CheggPassword, "cmdLogin")



if __name__ == "__main__":
