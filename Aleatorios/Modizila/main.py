from selenium import webdriver
import webbrowser
from termcolor import colored as corzinha
 
import time
 
url_whats = "https://web.whatsapp.com/"

firefox = webbrowser.Mozilla("C:/Program Files/Mozilla Firefox/firefox.exe")

firefox.open(url_whats)

input(corzinha("Aperte Enter apos escanear o QR Code", "yellow"))

