from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
from time import sleep
import requests
import ctypes
import os


def checkNet():
    try:
        resp = requests.get('https://google.com')
        resp.raise_for_status
        return False
    except Exception as e:
        return True

def clearTitle(title):
    newTitle = ''
    for l in title:
        if l in '|<>:*?"\\/': continue
        newTitle += l
        if len(newTitle)>50: break

    return newTitle

def booksc(searchWord):
    try: os.makedirs('./books')
    except FileExistsError: pass
    try: os.makedirs('./books/cache')
    except FileExistsError: pass
    if checkNet(): return ['NoNet']

    ctypes.windll.kernel32.SetFileAttributesW('./books/cache', 2)
    options = ChromeOptions()
    options.headless = True
    args = ["hide_console", ]
    driver = webdriver.Chrome(
        service_args=args,
        options=options
        )
    driver.get('https://1lib.ma/s/%s' % searchWord)
    sleep(1)
    books = []
    for div_num in [i for i in range(1, 21) if i%2==0]:
        try:
            xpath = f'//*[@id="searchResultBox"]/div[{div_num}]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a'
            book = driver.find_element_by_xpath(xpath).get_attribute('href')
            books.append(book)
        except: break

    books_data = []
    for book in books:
        driver.get(book)
        try:
            driver.find_element_by_xpath('//*[@id="dbx_11208786"]')
        except:

            title = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[1]/div[2]/h1').text
            try:
                src = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[1]/div[1]/div/a/div/img').get_attribute('src')
        
                req = requests.get(src)
                img = req.content
            except:
                with open('./cache/26892f227e0e825d64d6d42829816392c25859477f708730fbf5d64c55e2bf0d', 'rb')\
                    as f:
                    img = f.read()
                    
            img_path = 'books/cache/' + clearTitle(title)
            with open(img_path, 'wb') as f:
                f.write(img)    
            books_data.append([title, img_path, book])

    driver.quit()

    return books_data

def getVpn():
    options = ChromeOptions()
    options.add_extension('./cache/24376bcf01e4df0dc1b96004e143ba36f838c1d402dc6d8c4a03367d2b1f9c6b')
    options.headless = True
    args = ["hide_console", ]
    prefs = {
            "download.default_directory" : os.getcwd() + '\\books',
            'safebrowsing.enabled': 'false'
            }
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(
        service_args=args,
        options=options
        )
    driver.find_elements_by_tag_name('button')[1].click()
    sleep(2)
    driver.find_elements_by_tag_name('input')[0].send_keys('zahirzero')
    pwd = driver.find_elements_by_tag_name('input')[1]
    pwd.send_keys('Test@@22')
    pwd.submit()
    sleep(2)
    driver.find_elements_by_tag_name('button')[4].click()
    return driver

def download(url, vpn=False):
    books = set(os.listdir('./books'))
    if checkNet(): return ['NoNet']
    if vpn:
        try: driver = getVpn()
        except Exception as e: print(e); return [False]
    else:
        options = ChromeOptions()
        options.headless = True
        args = ["hide_console", ]
        prefs = {
            "download.default_directory" : os.getcwd() + '\\books',
            'safebrowsing.enabled': 'false'
            }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(
            service_args=args,
            options=options
            )
    
    driver.get(url)
    sleep(2)
    driver.find_element_by_class_name('addDownloadedBook').click()
   
    book = list(set(os.listdir('./books')) - books)
    while True:
        if book and 'crdownload' not in book[0]:
            os.rename('.\\books\\' + book[0], '.\\books\\' + book[0].replace('z-lib.org', 'ZAHIR'))
            driver.quit()
            return [True, book[0].split('.')[-1]]
        
        else:
            try:
                driver.find_element_by_xpath('html/body/table/tbody/tr[2]/td/div/div/div/div[1]/div/div').text
                break
            except:
                sleep(1)
                book = list(set(os.listdir('./books')) - books)

    driver.quit()
    if not vpn:
        return download(url, True)

    return [False]

def checkUpdate():
    if checkNet(): return ['NoNet']
    resp = requests.get('https://justpaste.it/5rd3t')
    soup = BeautifulSoup(resp.text, features="html.parser")
    data = soup.select('p')[0].text
    return [data[:4], data[4:]]
