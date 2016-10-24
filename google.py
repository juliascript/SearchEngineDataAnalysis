import time
from splinter import Browser

browser = Browser('chrome')

url = 'https://www.google.com'
searchTerm = 'waddup'

browser.visit(url)

browser.find_by_id('lst-ib').fill(searchTerm)
print browser.find_by_css('input[class^="g"]')




time.sleep(3)
browser.quit()