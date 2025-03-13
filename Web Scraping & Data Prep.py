# load packages
import numpy as np
import pandas as pd
# from pandas_datareader import data as wb
# import altair as alt
import matplotlib.pyplot as plt
# import yfinance as yf
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import pyodbc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
# from thefuzz import process
# from thefuzz import fuzz
# import Levenshtein
from pathlib import Path
import shutil
import re
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# allows altair to visualize data with more than 5000 rows
# alt.data_transformers.disable_max_rows()

# set varaible for todays date
now = datetime.now()

## create driver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://stockanalysis.com/screener/etf/')
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/button').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[5]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[7]/input').click()

# continue filtering for this list of columns or the list you want. Unable to automate this process since
# checks have no name/id and xpaths are dynamically generated
# Symbol	Company Name	Asset Class	Assets	Stock Price	Volume	Sector	PE Ratio
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[13]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[17]/input').click()

# once column selections are correct run next cells
driver.find_element('xpath', '//*[@id="main"]/div[3]/nav/div/div/button').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/nav/div/div/button').click()

ETF_df = pd.DataFrame()
sym = []
comp_name = []
clas = []
assets = []
stk_price = []
vol = []
Sector = []
PE_Rat = []
count = 0
# set this vairable equal to the length of pages
pages = 144

for i in range(1, pages):
    try:
        for i in range(1, 51):
            try:
                xps = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[1]'
                xpco = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[2]'
                xpcl = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[3]'
                xpa = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[4]'
                xpst = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[5]'
                xpv = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[6]'
                xpse = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[7]'
                xpp = '//*[@id="main"]/div[3]/div[2]/table/tbody/tr[' + str(i) + ']/td[8]'

                s = (driver.find_element('xpath', xps)).text
                co = (driver.find_element('xpath', xpco)).text
                cl = (driver.find_element('xpath', xpcl)).text
                a = (driver.find_element('xpath', xpa)).text
                st = (driver.find_element('xpath', xpst)).text
                v = (driver.find_element('xpath', xpv)).text
                se = (driver.find_element('xpath', xpse)).text
                p = (driver.find_element('xpath', xpp)).text

                sym.append(s)
                comp_name.append(co)
                clas.append(cl)
                assets.append(a)
                stk_price.append(st)
                vol.append(v)
                Sector.append(se)
                PE_Rat.append(p)
            except:
                continue

        count = count + 1
        print(str(count) + '/' + str(pages) + ' pages complete ...')

        act = driver.find_element('xpath', '//*[@id="main"]/div[3]/nav/button[2]')
        # click button
        driver.execute_script("arguments[0].click();", act);
    except:
        continue

ETF_df['Ticker'] = sym
ETF_df['Company Name'] = comp_name
ETF_df['Asset Class'] = clas
ETF_df['Assets'] = assets
ETF_df['Stock Price'] = stk_price
ETF_df['Volume'] = vol
ETF_df['Sector'] = Sector
ETF_df['PE Ratio'] = PE_Rat

## save to csv
now = datetime.now()
now_str = str(now).split(' ')[0]
ETF_df_name = 'ETF_df_' + now_str + '.csv'

ETF_df.to_csv(ETF_df_name)

## Create stock Dataframe

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://stockanalysis.com/screener/stock/')
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/button').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[5]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[14]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[24]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[27]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[34]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[37]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/div/div/div[42]/input').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/button').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/nav/div/div/button').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/nav/div/div/div/button[2]').click()

Stock_df = pd.DataFrame()
sym = []
comp_name = []
mkt_cap = []
stk_price = []
industry = []
volume = []
PE_rat = []
sector = []
rating = []
PT_diff = []
emps = []
rev = []
GP = []
count = 0
# set this variable equal to the length of pages
pages = 125
for i in range(1, pages):
    try:
        for i in range(1, 51):
            try:
                xps = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[1]'
                xpc = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[2]'
                xpm = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[3]'
                xpst = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[4]'
                xpind = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[5]'
                xpv = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[6]'
                xppe = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[7]'
                xpse = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[8]'
                xpra = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[9]'
                xppt = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[10]'
                xpe = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[11]'
                xpre = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[12]'
                xpgp = '//*[@id="main"]/div[3]/div[3]/table/tbody/tr[' + str(i) + ']/td[13]'

                s = (driver.find_element('xpath', xps)).text
                c = (driver.find_element('xpath', xpc)).text
                m = (driver.find_element('xpath', xpm)).text
                st = (driver.find_element('xpath', xpst)).text
                ind = (driver.find_element('xpath', xpind)).text
                v = (driver.find_element('xpath', xpv)).text
                pe = (driver.find_element('xpath', xppe)).text
                se = (driver.find_element('xpath', xpse)).text
                ra = (driver.find_element('xpath', xpra)).text
                pt = (driver.find_element('xpath', xppt)).text
                e = (driver.find_element('xpath', xpe)).text
                re = (driver.find_element('xpath', xpre)).text
                gp = (driver.find_element('xpath', xpgp)).text

                sym.append(s)
                comp_name.append(c)
                mkt_cap.append(m)
                stk_price.append(st)
                industry.append(ind)
                volume.append(v)
                PE_rat.append(pe)
                sector.append(se)
                rating.append(ra)
                PT_diff.append(pt)
                emps.append(e)
                rev.append(re)
                GP.append(gp)
            except:
                continue
    except:
        continue

    count = count + 1
    print(str(count) + '/' + str(pages) + ' pages complete ...')

    act = driver.find_element('xpath', '//*[@id="main"]/div[3]/nav/button[2]')
    # click button
    driver.execute_script("arguments[0].click();", act);

Stock_df['Ticker'] = sym
Stock_df['Company Name'] = comp_name
Stock_df['Market Cap'] = mkt_cap
Stock_df['Stock Price'] = stk_price
Stock_df['Industry'] = industry
Stock_df['Volume'] = volume
Stock_df['P/E Ratio'] = PE_rat
Stock_df['Sector'] = sector
Stock_df['PT Diff (%)'] = PT_diff
Stock_df['Employees'] = emps
Stock_df['Revenue'] = rev
Stock_df['Gross Profit'] = GP

## save to csv
now = datetime.now()
now_str = str(now).split(' ')[0]
Stock_df_name = 'Stock_df_' + now_str + '.csv'

Stock_df.to_csv(Stock_df_name)

## create crypto df

Crypto_df = pd.DataFrame()
driver = webdriver.Chrome('chromedriver.exe')
Symbol = []
Name = []
Price = []
Mkt_Cap = []
page = 0
count = 0
for s in range(1, 102):
    driver.get('https://finance.yahoo.com/cryptocurrencies/?count=100&fr=sycsrp_catchall&offset=' + str(page))
    for i in range(1, 101):
        try:
            Symbol.append(driver.find_element('xpath', '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(
                i) + ']/td[1]').text)
            Name.append(driver.find_element('xpath', '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(
                i) + ']/td[2]').text)
            Price.append(driver.find_element('xpath', '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(
                i) + ']/td[3]').text)
            Mkt_Cap.append(driver.find_element('xpath', '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(
                i) + ']/td[6]').text)
        except:
            continue
    page = page + 100
    count = count + 100
    print(str(count) + ' out of 10100 cryptocurrencies loaded...')

Crypto_df['Symbol'] = Symbol
Crypto_df['Name'] = Name
Crypto_df['Price'] = Price
Crypto_df['Market Cap'] = Mkt_Cap

Crypto_df = Crypto_df.reset_index()
Crypto_df['index'] = Crypto_df['index'] + 1
Crypto_df = Crypto_df.rename(columns={'index': "Market Rank"})

## save dataframe to csv

now = datetime.now()
now_str = str(now).split(' ')[0]
crypto_df_name = 'Crypto_df_' + now_str + '.csv'

Crypto_df.to_csv(crypto_df_name)

## create and save materials dataframe
Materials_df = pd.DataFrame()
materials_ticks = ['GC=F', 'SI=F', 'CL=F', 'PL=F', 'Pa=F', 'KC = F', 'CC = F', 'ALI = F', 'LBR=F', 'ZC=F', '6R=F']
material_names = ['Gold', 'Silver', 'Crude Oil', 'Platinum', 'Pallidium', 'Coffee', 'Cocoa', 'Aluminum', 'Lumber',
                  'Corn', 'Russian Rubble']
Materials_df['Ticker'] = materials_ticks
Materials_df['Name'] = material_names

now = datetime.now()
now_str = str(now).split(' ')[0]
Materials_df_name = 'Materials_df_' + now_str + '.csv'

Materials_df.to_csv(Materials_df_name)

## Prep data for merge
Stock_df['Type'] = 'Stock'
ETF_df['Type'] = 'ETF'
Crypto_df['Type'] = 'Crypto Currency'
Materials_df['Type'] = 'Material'

Stock_df = Stock_df.rename(columns={'Company Name': 'Name', 'Stock Price': 'Price', 'P/E Ratio': 'PE Ratio'})
ETF_df = ETF_df.rename(columns={'Company Name': 'Name', 'Stock Price': 'Price'})
Crypto_df.rename(columns={'Symbol': 'Ticker'}, inplace=True)

merged_df = pd.concat([Stock_df, ETF_df, Crypto_df, Materials_df])
merged_df.drop(columns='Unnamed: 0', inplace=True)
merged_df.reset_index(inplace=True)
merged_df.drop(columns='index', inplace=True)

Price = []
for i in merged_df['Price']:
    if type(i) == str:
        Price.append(float(i.replace(',', '')))
    else:
        Price.append(i)
merged_df['Price_Filter'] = Price

Prat = []
for i in merged_df['PE Ratio']:
    if type(i) == str:
        if i == '-':
            Prat.append(np.nan)
        else:
            Prat.append(float(i.replace(',', '')))
    else:
        Prat.append(i)
merged_df['Prat_Filter'] = Prat

emps = []
for i in merged_df['Employees']:
    if type(i) == str:
        try:
            emps.append(int(i.replace(',', '')))
        except:
            emps.append(np.nan)
    elif type(i) == float:
        try:
            emps.append(int(i))
        except:
            emps.append(i)
merged_df['Emp_Filter'] = emps

MC = []
for cap in merged_df['Market Cap']:
    if type(cap) == str:
        cap = cap.replace(',', '')
        if cap == '-':
            MC.append(np.nan)
        if 'B' in cap:
            num = float(cap.replace('B', ''))
            MC.append(num * 1000000000)
        if 'M' in cap:
            num = float(cap.replace('M', ''))
            MC.append(num * 1000000)
        if 'k' in cap:
            num = float(cap.replace('k', ''))
            MC.append(num)
        if ('B' not in cap) & ('M' not in cap) & ('k' not in cap):
            MC.append(float(cap))
    else:
        MC.append(float(cap))
merged_df['Cap_Filter'] = MC
merged_df['Cap_Filter'] = [float(i) for i in merged_df['Cap_Filter']]

Rev = []
for r in merged_df['Revenue']:
    if type(r) == str:
        r.replace(',', '')
        if 'B' in r:
            num = float(r.replace('B', ''))
            Rev.append(num * 1000000000)
        elif 'M' in r:
            num = float(r.replace('M', ''))
            Rev.append(num * 1000000)
        elif 'K' in r:
            num = float(r.replace('K', ''))
            Rev.append(num * 1000)
        elif ('B' not in r) & ('M' not in r) & ('K' not in r):
            Rev.append(np.nan)
    else:
        Rev.append(float(r))
merged_df['Rev_Filter'] = Rev

vols = []
for i in merged_df['Volume']:
    if type(i) == str:
        try:
            vols.append(int(i.replace(',', '')))
        except:
            vols.append(np.nan)
    elif type(i) == float:
        try:
            vols.append(int(i))
        except:
            vols.append(i)
merged_df['Vol_Filter'] = vols

Ass = []
for a in merged_df['Assets']:
    if type(a) == str:
        a.replace(',', '')
        if 'B' in a:
            num = float(a.replace('B', ''))
            Ass.append(num * 1000000000)
        elif 'M' in a:
            num = float(a.replace('M', ''))
            Ass.append(num * 1000000)
        elif 'K' in a:
            num = float(a.replace('K', ''))
            Ass.append(num * 1000)
        elif ('B' not in a) & ('M' not in a) & ('K' not in a):
            Ass.append(np.nan)
    else:
        Ass.append(float(a))
merged_df['Assets_Filter'] = Ass

GP = []
for gp in merged_df['Gross Profit']:
    if type(gp) == str:
        gp.replace(',', '')
        if 'B' in gp:
            num = float(gp.replace('B', ''))
            GP.append(num * 1000000000)
        elif 'M' in gp:
            num = float(gp.replace('M', ''))
            GP.append(num * 1000000)
        elif 'K' in gp:
            num = float(gp.replace('K', ''))
            GP.append(num * 1000)
        elif ('B' not in gp) & ('M' not in gp) & ('K' not in gp):
            GP.append(np.nan)
    else:
        GP.append(float(gp))
merged_df['GP_Filter'] = GP

merged_df.drop_duplicates('Ticker', inplace=True)

now = datetime.now()
now_str = str(now).split(' ')[0]
merged_df_name = 'Merged_Assets_df_' + now_str + '.csv'

merged_df.to_csv(merged_df_name)

## example visuals
# list of stocks you want to include
group = ['GC=F', 'AMZN', 'AMZN', 'AAPL', '^GSPC', 'F', 'META', 'GOOG', 'TSLA', 'NFLX', 'YM=F', 'CL=F',
         'BTC-USD', 'ETH-USD', 'CRO-USD', 'ADA-USD']

# best performing stocks of all time
best_all_time = DF[DF['Ticker'].isin(group)].sort_values('All Time ROI', ascending=False)[
    ['Company', 'Ticker', 'All Time ROI', 'All Time Volatility', 'All Time Avg ROI', 'Start Date']]
count = 1
rank = []
for i in range(len(best_all_time)):
    rank.append(count)
    count = count + 1
best_all_time['Rank'] = rank
best_all_time = best_all_time.set_index('Rank')
best_all_time['All Time ROI'] = [str(i) + '%' for i in best_all_time['All Time ROI']]
best_all_time['All Time Avg ROI'] = [str(i) + '%' for i in best_all_time['All Time Avg ROI']]
best_all_time

# list of stocks to include in graph
group = ['GC=F', '^GSPC', 'YM=F', 'CL=F']
# all time graph
all_time_ROI = alt.Chart(main_df[main_df['Ticker'].isin(group)],
                         title='ALL TIME RETURN ON INVESTMENT').mark_line().encode(
    alt.X('Date', axis=alt.Axis(title="DATE")),
    alt.Y('scaled', axis=alt.Axis(title="ROI %")),
    tooltip='Company',
    color='Company',
    opacity=alt.value(0.78)
)
all_time_ROI

# list of stocks you want to include
group = ['GC=F', 'AMZN', 'AMZN', 'AAPL', '^GSPC', 'F', 'META', 'GOOG', 'TSLA', 'NFLX', 'YM=F', 'CL=F',
         'BTC-USD', 'ETH-USD', 'CRO-USD', 'ADA-USD']

# best performing stocks of the last 30 years
best_last_thirty_years = \
DF[(DF['Ticker'].isin(group)) & (DF['30 Year ROI'].isna() == False)].sort_values('30 Year ROI', ascending=False)[
    ['Company', 'Ticker', '30 Year ROI', '30 Year Volatility', '30 Year Avg ROI', 'Start Date']]
count = 1
rank = []
for i in range(len(best_last_thirty_years)):
    rank.append(count)
    count = count + 1
best_last_thirty_years['Rank'] = rank
best_last_thirty_years = best_last_thirty_years.set_index('Rank')
best_last_thirty_years['30 Year ROI'] = [str(i) + '%' for i in best_last_thirty_years['30 Year ROI']]
best_last_thirty_years['30 Year Avg ROI'] = [str(i) + '%' for i in best_last_thirty_years['30 Year Avg ROI']]
best_last_thirty_years