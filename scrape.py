from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
from sys import argv

def convertToNum(text):
    if 'K' in text:
        text = text.strip('K')
        return float(text) * 1000
    if 'M' in text:
        text = text.strip('M')
        return float(text) * 1000000
    if text == '':
        return 0
    return float(text)

def main():
    subMin = int(argv[1])
    subMax = int(argv[2])

    df = pd.read_csv('creator_list.csv')
    df = df.drop(columns=df.columns[3])
    print(df)

    driver = webdriver.Chrome() 
    driver.get('https://www.youtube.com/results?search_query=ap+exam+review&sp=EgIQAQ%253D%253D')

    time.sleep(10)

    video_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    videolinks = []
    for i in video_data:
        videolinks.append(i.get_attribute('href'))
    print(len(videolinks))

    wait = WebDriverWait(driver, 10)
    names = set()
    for name in df['ch_name']:
        names.add(name)

    for x in videolinks:
        driver.get(x)
        c_data = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"text\"]/a")))
        name = c_data.text
        link = c_data.get_attribute('href')
        c_subs = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"owner-sub-count\"]")))
        subs = int(convertToNum(c_subs.text.strip(' subscribers')))

        if subs >= subMin and subs <= subMax:
            if name not in names:
                df.loc[len(df)] = [name, subs, link]
                names.add(name)
                print(subs)
    print(df)
    df.to_csv('creator_list_test.csv', index=False)

if __name__ == "__main__":
    main()