# load packages
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# load Data
Data = pd.read_csv('Merged_Assets_df_2022-08-18.csv')

Data.drop(columns='Unnamed: 0', inplace=True)

# set timeframes
now = datetime.now()
minus_one_week = now + relativedelta(weeks=-1)
minus_one_month = now + relativedelta(months=-1)
minus_three_months = now + relativedelta(months=-3)
minus_six_months = now + relativedelta(months=-6)
minus_one_year = now + relativedelta(years=-1)
minus_three_years = now + relativedelta(years=-3)
minus_five_years = now + relativedelta(years=-5)
minus_ten_years = now + relativedelta(years=-10)
minus_thirty_years = now + relativedelta(years=-30)

DF = pd.DataFrame()
avg_all_time = []
all_time = []
avg_ten_year = []
thirty_year = []
avg_thirty_year = []
ten_year = []
avg_five_year = []
five_year = []
avg_three_year = []
three_year = []
avg_one_year = []
one_year = []
avg_six_months = []
six_months = []
avg_three_months = []
three_months = []
avg_one_month = []
one_month = []
avg_one_week = []
one_week = []
all_time_vol = []
thirty_year_vol = []
ten_year_vol = []
five_year_vol = []
three_year_vol = []
one_year_vol = []
sds = []

Tick = []
counter = 0

keep_cols = ['Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close',
             'scaled', 'Ticker', 'log_close', 'log_return', 'scaled_30y',
             'scaled_10y', 'scaled_5y', 'scaled_3y', 'scaled_1y',
             'scaled_6m', 'scaled_3m', 'scaled_1m', 'scaled_1w']

main_df = pd.DataFrame(columns=keep_cols)

for i in Data['Ticker']:
    try:
        Stock = wb.DataReader(i, data_source='yahoo', start='1970-1-1')
        Stock['simple_return'] = (Stock['Adj Close'] / Stock['Adj Close'].shift(1)) - 1
        Stock['scaled'] = [round((i / Stock['Adj Close'][0]) * 100 - 100, 2) for i in Stock['Adj Close']]
        Stock['Ticker'] = i
        Stock['log_close'] = np.log(Stock['Adj Close'])
        Stock['log_return'] = (Stock['log_close'] - Stock['log_close'].shift(1))
        Stock['Volatility'] = abs(Stock['log_return'])
        Stock = Stock.reset_index()
        Stock['scaled_30y'] = [
            round((i / Stock[Stock['Date'] > minus_thirty_years]['Adj Close'].iloc[0]) * 100 - 100, 2) for i in
            Stock['Adj Close']]
        Stock['scaled_10y'] = [round((i / Stock[Stock['Date'] > minus_ten_years]['Adj Close'].iloc[0]) * 100 - 100, 2)
                               for i in Stock['Adj Close']]
        Stock['scaled_5y'] = [round((i / Stock[Stock['Date'] > minus_five_years]['Adj Close'].iloc[0]) * 100 - 100, 2)
                              for i in Stock['Adj Close']]
        Stock['scaled_3y'] = [round((i / Stock[Stock['Date'] > minus_three_years]['Adj Close'].iloc[0]) * 100 - 100, 2)
                              for i in Stock['Adj Close']]
        Stock['scaled_1y'] = [round((i / Stock[Stock['Date'] > minus_one_year]['Adj Close'].iloc[0]) * 100 - 100, 2) for
                              i in Stock['Adj Close']]
        Stock['scaled_6m'] = [round((i / Stock[Stock['Date'] > minus_six_months]['Adj Close'].iloc[0]) * 100 - 100, 2)
                              for i in Stock['Adj Close']]
        Stock['scaled_3m'] = [round((i / Stock[Stock['Date'] > minus_three_months]['Adj Close'].iloc[0]) * 100 - 100, 2)
                              for i in Stock['Adj Close']]
        Stock['scaled_1m'] = [round((i / Stock[Stock['Date'] > minus_one_month]['Adj Close'].iloc[0]) * 100 - 100, 2)
                              for i in Stock['Adj Close']]
        Stock['scaled_1w'] = [round((i / Stock[Stock['Date'] > minus_one_week]['Adj Close'].iloc[0]) * 100 - 100, 2) for
                              i in Stock['Adj Close']]
        Stock['Avg Daily All Time Return'] = round(Stock['simple_return'].mean() * 100, 2)
        Stock['Avg Daily Thirty Year Return'] = round(
            Stock[Stock['Date'] > minus_thirty_years]['simple_return'].mean() * 100, 2)
        Stock['Avg Daily Ten Year Return'] = round(Stock[Stock['Date'] > minus_ten_years]['simple_return'].mean() * 100,
                                                   2)
        Stock['Avg Daily Five Year Return'] = round(
            Stock[Stock['Date'] > minus_five_years]['simple_return'].mean() * 100, 2)
        Stock['Avg Daily Three Year Return'] = round(
            Stock[Stock['Date'] > minus_three_years]['simple_return'].mean() * 100, 2)
        Stock['Avg Daily One Year Return'] = round(Stock[Stock['Date'] > minus_one_year]['simple_return'].mean() * 100,
                                                   2)
        Stock['Avg Daily Six Month Return'] = round(
            Stock[Stock['Date'] > minus_six_months]['simple_return'].mean() * 100, 2)
        Stock['Avg Daily Three Month Return'] = round(
            Stock[Stock['Date'] > minus_three_months]['simple_return'].mean() * 100, 2)
        Stock['Avg Daily One Month Return'] = round(
            Stock[Stock['Date'] > minus_one_month]['simple_return'].mean() * 100, 2)
        Stock['Avg Daily One Week Return'] = round(Stock[Stock['Date'] > minus_one_week]['simple_return'].mean() * 100,
                                                   2)
        last_week = Stock[Stock['Date'] > minus_one_week]
        last_one_month = Stock[Stock['Date'] > minus_one_month]
        last_three_months = Stock[Stock['Date'] > minus_three_months]
        last_six_months = Stock[Stock['Date'] > minus_six_months]
        last_year = Stock[Stock['Date'] > minus_one_year]
        last_three = Stock[Stock['Date'] > minus_three_years]
        last_five = Stock[Stock['Date'] > minus_five_years]
        last_ten = Stock[Stock['Date'] > minus_ten_years]
        last_thirty = Stock[Stock['Date'] > minus_thirty_years]
        Tick.append(i)
        start = min(Stock['Date'])
        sds.append(str(start).split(' 00')[0])
        # all time returns
        all_time.append(round(Stock.iloc[-1, 6] / Stock.iloc[0, 6] * 100 - 100, 2))
        avg_all_time.append(round(Stock['simple_return'].mean() * 100, 2))
        all_time_vol.append(round(Stock['Volatility'].mean() * 100, 2))

        # 30 year returns
        if start > minus_thirty_years:
            thirty_year.append(np.nan)
            avg_thirty_year.append(np.nan)
            thirty_year_vol.append(np.nan)
        else:
            thirty_year.append(round(last_thirty.iloc[-1, 6] / last_thirty.iloc[0, 6] * 100 - 100, 2))
            avg_thirty_year.append(round(last_thirty['simple_return'].mean() * 100, 2))
            thirty_year_vol.append(round(last_thirty['Volatility'].mean() * 100, 2))
        # 10 year returns
        if start > minus_ten_years:
            ten_year.append(np.nan)
            avg_ten_year.append(np.nan)
            ten_year_vol.append(np.nan)
        else:
            ten_year.append(round(last_ten.iloc[-1, 6] / last_ten.iloc[0, 6] * 100 - 100, 2))
            avg_ten_year.append(round(last_ten['simple_return'].mean() * 100, 2))
            ten_year_vol.append(round(last_ten['Volatility'].mean() * 100, 2))

        # 5 year returns
        if start > minus_five_years:
            five_year.append(np.nan)
            avg_five_year.append(np.nan)
            five_year_vol.append(np.nan)
        else:
            five_year.append(round(last_five.iloc[-1, 6] / last_five.iloc[0, 6] * 100 - 100, 2))
            avg_five_year.append(round(last_five['simple_return'].mean() * 100, 2))
            five_year_vol.append(round(last_five['Volatility'].mean() * 100, 2))
        # 3 year returns
        if start > minus_three_years:
            three_year.append(np.nan)
            avg_three_year.append(np.nan)
            three_year_vol.append(np.nan)
        else:
            three_year.append(round(last_three.iloc[-1, 6] / last_three.iloc[0, 6] * 100 - 100, 2))
            avg_three_year.append(round(last_three['simple_return'].mean() * 100, 2))
            three_year_vol.append(round(last_three['Volatility'].mean() * 100, 2))
        # 1 year returns
        if start > minus_one_year:
            one_year.append(np.nan)
            avg_one_year.append(np.nan)
            one_year_vol.append(np.nan)
        else:
            one_year.append(round(last_year.iloc[-1, 6] / last_year.iloc[0, 6] * 100 - 100, 2))
            avg_one_year.append(round(last_year['simple_return'].mean() * 100, 2))
            one_year_vol.append(round(last_year['Volatility'].mean() * 100, 2))

        # 6 months returns
        if start > minus_six_months:
            six_months.append(np.nan)
            avg_six_months.append(np.nan)
        else:
            six_months.append(round(last_six_months.iloc[-1, 6] / last_six_months.iloc[0, 6] * 100 - 100, 2))
            avg_six_months.append(round(last_six_months['simple_return'].mean() * 100, 2))

        # three months returns
        if start > minus_three_months:
            three_months.append(np.nan)
            avg_three_months.append(np.nan)
        else:
            three_months.append(round(last_three_months.iloc[-1, 6] / last_three_months.iloc[0, 6] * 100 - 100, 2))
            avg_three_months.append(round(last_three_months['simple_return'].mean() * 100, 2))

        # one month returns
        if start > minus_one_month:
            one_month.append(np.nan)
            avg_one_month.append(np.nan)
        else:
            one_month.append(round(last_one_month.iloc[-1, 6] / last_one_month.iloc[0, 6] * 100 - 100, 2))
            avg_one_month.append(round(last_one_month['simple_return'].mean() * 100, 2))

        # one week returns
        if start > minus_one_week:
            one_week.append(np.nan)
            avg_one_week.append(np.nan)
        else:
            one_week.append(round(last_one_month.iloc[-1, 6] / last_one_month.iloc[0, 6] * 100 - 100, 2))
            avg_one_week.append(round(last_week['simple_return'].mean() * 100, 2))

        main_df = main_df.merge(Stock[keep_cols], on=keep_cols, how='outer')
        counter += 1
        print(str(counter) + '/' + str(len(Data['Ticker'])) + ' ' + "stocks complete...")
    except:
        counter += 1
        print(str(counter) + '/' + str(len(Data['Ticker'])) + ' ' + "stocks complete...")

DF['Ticker'] = Tick
DF['ROI Since 1970'] = all_time
DF['30 Year ROI'] = thirty_year
DF['10 Year ROI'] = ten_year
DF['5 Year ROI'] = five_year
DF['3 Year ROI'] = three_year
DF['1 Year ROI'] = one_year
DF['6 Month ROI'] = six_months
DF['3 Month ROI'] = three_months
DF['1 Month ROI'] = one_month
DF['1 Week ROI'] = one_week

DF['Avg ROI Since 1970'] = avg_all_time
DF['30 Year Avg ROI'] = avg_thirty_year
DF['10 Year Avg ROI'] = avg_ten_year
DF['5 Year Avg ROI'] = avg_five_year
DF['3 Year Avg ROI'] = avg_three_year
DF['1 Year Avg ROI'] = avg_one_year
DF['6 Month Avg ROI'] = avg_six_months
DF['3 Month Avg ROI'] = avg_three_months
DF['1 Month Avg ROI'] = avg_one_month
DF['1 Week Avg ROI'] = avg_one_week

DF['Volatility Since 1970'] = all_time_vol
DF['30 Year Volatility'] = thirty_year_vol
DF['10 Year Volatility'] = ten_year_vol
DF['5 Year Volatility'] = five_year_vol
DF['3 Year Volatility'] = three_year_vol
DF['1 Year Volatility'] = one_year_vol

DF['Listing Date'] = sds
DF['Listing Date'] = ['Before 1970' if d == '1970-01-02' else d for d in DF['Listing Date']]

main_df2 = main_df.merge(Data, how='inner', on='Ticker')
DF2 = DF.merge(Data, how='inner', on='Ticker')

## example visual
import altair as alt

# allows altair to visualize data with more than 5000 rows
alt.data_transformers.disable_max_rows()

group = e
# all time graph
ten_Y_ROI = alt.Chart(main_df2[(main_df2['Ticker'].isin(group)) & (main_df2['Date'] > minus_three_years)],
                      title='3 YEAR RETURN ON INVESTMENT').mark_line().encode(
    alt.X('Date', axis=alt.Axis(title="DATE")),
    alt.Y('scaled_3y', axis=alt.Axis(title="ROI %")),
    tooltip='Name',
    color='Name',
    opacity=alt.value(0.78)
)
ten_Y_ROI