import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

startTime = datetime.now()


chrome_path = r"C:\Users\Asdar\Desktop\My_Phyton\AiTeguh\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(chrome_path, options=chrome_options,keep_alive=False)
url = "https://www.insidearbitrage.com/insider-sales/?desk=yes"
driver.get(url)

tickerlist=[]
relationshiplist=[]
datelist=[]
costlist=[]
shareslist=[]
sharesheldlist=[]

for i in range(2,103):
    tickerpath = f"""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[{i}]/td[1]"""
    ticker = driver.find_element_by_xpath(tickerpath)
    tickerlist.append(ticker.text)

    relationshippath = f"""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[{i}]/td[4]"""
    relationship = driver.find_element_by_xpath(relationshippath)
    relationshiplist.append(relationship.text)

    datepath = f"""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[{i}]/td[5]"""
    date = driver.find_element_by_xpath(datepath)
    datelist.append(date.text)

    costpath = f"""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[{i}]/td[6]"""
    cost = driver.find_element_by_xpath(costpath)
    costlist.append(cost.text)

    sharespath = f"""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[{i}]/td[7]"""
    shares = driver.find_element_by_xpath(sharespath)
    shareslist.append(shares.text)

    sharesheldpath = f"""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[{i}]/td[9]"""
    sharesheld = driver.find_element_by_xpath(sharesheldpath)
    sharesheldlist.append(sharesheld.text)


allinfo = list(zip(tickerlist,relationshiplist,datelist,costlist,shareslist,sharesheldlist))

df = pd.DataFrame(allinfo,columns = ["Ticker","Position","Date","Share Cost","Shares Sold","Shares Held"])
print(df)

df.to_csv('insider.csv',index=False)

print(f"""Execution Time: {datetime.now() - startTime}""")