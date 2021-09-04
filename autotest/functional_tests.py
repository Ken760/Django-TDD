from selenium import webdriver
browser = webdriver.Chrome(executable_path="driver./chromedriver")

browser.get('http://localhost:8000')

assert 'Django' in browser.title