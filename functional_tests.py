__author__ = 'nick'

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:5000')

assert 'Django' in browser.title
