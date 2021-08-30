# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:30:02 2020

@author: AfifNF4
"""

from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import tanggal

#binary = FirefoxBinary('path/to/installed firefox binary')
browser = webdriver.Chrome('D:\chromedriver') #Starting Firefox Browser
url="https://www.idx.co.id/data-pasar/ringkasan-perdagangan/ringkasan-saham/"

browser.get(url) 

time.sleep(60)

for x in tanggal.tgl2:

    tgl = browser.find_element_by_xpath("//input[@id='dateFilter']")
    browser.execute_script('document.getElementById("dateFilter").removeAttribute("readonly")')
    tgl.clear()
    tgl.send_keys(x)
    time.sleep(5)     

    cari = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[5]/button[1]")
    cari.click()
    time.sleep(5)

    unduh = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[2]/div[1]/div[3]/a[1]")
    print("yes")
    unduh.click()
    time.sleep(5)
    



time.sleep(5)
print("get data selesai")
browser.close()