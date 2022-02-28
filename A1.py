from hashlib import new
from turtle import clear
from mechanize import Browser
from selenium import webdriver
import time
import smtplib, ssl
import os
import time
import getpass


#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'


#SCRIPT MADE BY RIP-Network
web = webdriver.Firefox()
web.get('http://instagram.com')
time.sleep(5)


acceptCookies = web.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()
time.sleep(5)
user = "bot_7626"
paswd = "44126026c"
inputUser = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
inputUser.send_keys(user)
inputPass = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
inputPass.send_keys(paswd)
loginButton = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()

def open_followers(account_instagram):
   web.get("https://www.instagram.com/" + account_instagram)
   time.sleep(5)


sources = ["ripnetwork_ofc"]
for account in sources:
    time.sleep(5)
    open_followers(account)
    time.sleep(5)
