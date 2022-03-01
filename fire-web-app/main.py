# Importing needed modules, packages
import os
import pytz
import json
from config import powerlink
from urllib.request import urlopen
from datetime import datetime, date
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# base URL for all queries
base_url = 'https://financialmodelingprep.com/api/v3/'

# Variables for different endpoints
profile = 'profile/'
ratiosTTM = 'ratios-ttm/'
quote = 'quote/'

# Variables for the three main indices in the US
dowjones = 'quote/%5EDJI/'
sp = 'quote/%5EGSPC/'
nasdaq = 'quote/%5EIXIC/'

# This function returns the user's chosen ticker
def users_request(ticker):
    return "Your choosen ticker: " + ticker.upper()

# This logic block dictates whether the market is closed or open. So far does not account for holidays
def market_hours():
    # Date variable
    current_time = datetime.now()

    day_of_week = datetime.strftime(current_time.astimezone(pytz.timezone('US/Eastern')), '%A')
    dt_east = int(datetime.strftime(current_time.astimezone(pytz.timezone('US/Eastern')), '%H%M'))
    if 930 <= dt_east <= 1600 and (day_of_week != 'Saturday' and day_of_week != 'Sunday'):
        return('The market is currently open!')
    else:
        return('The market is currently closed.')

# This class is responsible for the values shown on the home page
class MarketIndices:

    def DowJonesIndex(self):
        with urlopen(base_url + dowjones + powerlink) as response:
            source = response.read()
            data = json.loads(source)
        
        price = (data[0]["price"])
        return('{0:,}'.format(price))

    def DowJonesChange(self):
        with urlopen(base_url + dowjones + powerlink) as response:
            source = response.read()
            data = json.loads(source)

        change = (data[0]["change"])

        if change < 0:
            return(round(change, 2))
        else:
            return("+" + str(round(change, 2)))

    def DowJonesPercent(self):
        with urlopen(base_url + dowjones + powerlink) as response:
            source = response.read()
            data = json.loads(source)
        
        percent_change = str(round(data[0]["changesPercentage"], 2))
        return(percent_change + "%")

    def SP500Index(self):
        with urlopen(base_url + sp + powerlink) as response:
            source = response.read()
            data = json.loads(source)

        price = (data[0]["price"])
        return('{0:,}'.format(price))

    def SP500Change(self):
        with urlopen(base_url + sp + powerlink) as response:
            source = response.read()
            data = json.loads(source)

        change = (data[0]["change"])

        if change < 0:
            return(round(change, 2))
        else:
            return("+" + str(round(change, 2)))

    def SPPercent(self):
        with urlopen(base_url + sp + powerlink) as response:
            source = response.read()
            data = json.loads(source)
        
        percent_change = str(round(data[0]["changesPercentage"], 2))
        return(percent_change + "%")

    def NASDAQIndex(self):
        with urlopen(base_url + nasdaq + powerlink) as response:
            source = response.read()
            data = json.loads(source)

        price = (data[0]["price"])
        return('{0:,}'.format(price))

    def NasdaqPercent(self):
        with urlopen(base_url + nasdaq + powerlink) as response:
            source = response.read()
            data = json.loads(source)
        
        percent_change = str(round(data[0]["changesPercentage"], 2))
        return(percent_change + "%")

    def NASDAQChange(self):
        with urlopen(base_url + nasdaq + powerlink) as response:
            source = response.read()
            data = json.loads(source)

    
        change = (data[0]["change"])

        if change < 0:
            return(round(change, 2))
        else:
            return("+" + str(round(change, 2)))

class companySearch:

    # Company name function
    def check_for_company(self, company_name):
        try:
            with urlopen(base_url + profile + company_name.upper() + powerlink) as response:
                source = response.read()
                data = json.loads(source)

            company_name = (data[0]["companyName"])
            return(company_name)
        except:
            return("Company doesn\'t exist.")

    # Stock price function
    def stock_price_func(self, price):
        
        with urlopen(base_url + quote + price.upper() + powerlink) as response:
            source = response.read()
            data = json.loads(source)

        price = "$" + str((data[0]["price"]))
        return(price)

    # Price to Earnings Ratio function
    def pe_ratio_func(self, price):
        try:
            with urlopen(base_url + ratiosTTM + price.upper() + powerlink) as response:
                source = response.read()
                data = json.loads(source)

            peRatioTTM = round(data[0]["peRatioTTM"], 2)
            return(peRatioTTM)
        except:
            return("-")

    # Price to Earnings Growth Ratio function
    def peg_ratio_func(self, price):
        try:
            with urlopen(base_url + ratiosTTM + price.upper() + powerlink) as response:
                source = response.read()
                data = json.loads(source)
                
            pegRatioTTM = round(data[0]["pegRatioTTM"], 2)
            return(pegRatioTTM)
        except:
            return("-")

    # Price to Book Ratio function
    def pb_ratio_func(self, price):
        try:
            with urlopen(base_url + ratiosTTM + price.upper() + powerlink) as response:
                source = response.read()
                data = json.loads(source)

            pbRatioTTM = round(data[0]["priceToBookRatioTTM"], 2)
            return(pbRatioTTM)
        except:
            return("-")

    # Price to Sales Ratio function
    def ps_ratio_func(self, price):
        try:
            with urlopen(base_url + ratiosTTM + price.upper() + powerlink) as response:
                source = response.read()
                data = json.loads(source)
            
            psRatioTTM = round(data[0]["priceToSalesRatioTTM"], 2)
            return(psRatioTTM)
        except:
            return("-")

    # Price to Free Cash Flow function
    def pfcf_ratio_func(self, price):
        try:
            with urlopen(base_url + ratiosTTM + price.upper() + powerlink) as response:
                source = response.read()
                data = json.loads(source)
            
            pfcfRatioTTM = round(data[0]["priceToFreeCashFlowsRatioTTM"], 2)
            return(pfcfRatioTTM)
        except:
            return("-")  
 

# Routing to the home page
@app.route('/')
def home():
    return render_template("home.html")

# Routing to the search page
@app.route('/search', methods = ["GET", "POST"])
def search_page():
    if request.method == "POST":
        variable = request.form["variable"]
        return redirect(url_for("ticker_result", variable=variable))
    else:
        dow_jones_value = MarketIndices().DowJonesIndex()
        dow_jones_percent = MarketIndices().DowJonesPercent()
        dow_jones_change = MarketIndices().DowJonesChange()
        sp_value = MarketIndices().SP500Index()
        sp_percent = MarketIndices().SPPercent()
        sp_change = MarketIndices().SP500Change()
        nasdaq_value = MarketIndices().NASDAQIndex()
        nasdaq_percent = MarketIndices().NasdaqPercent()
        nasdaq_change = MarketIndices().NASDAQChange()
        return render_template(
        "index.html",
        market_status = market_hours(),
        dow_jones_value=dow_jones_value,
        dow_jones_percent=dow_jones_percent,
        dow_jones_change=dow_jones_change,
        sp_value=sp_value,
        sp_percent=sp_percent,
        sp_change=sp_change,
        nasdaq_value=nasdaq_value,
        nasdaq_percent=nasdaq_percent,
        nasdaq_change=nasdaq_change)

# Routing to the result page
@app.route('/search/result/<variable>')
def ticker_result(variable):
    dow_jones_value = MarketIndices().DowJonesIndex()
    dow_jones_percent = MarketIndices().DowJonesPercent()
    dow_jones_change = MarketIndices().DowJonesChange()
    sp_value = MarketIndices().SP500Index()
    sp_percent = MarketIndices().SPPercent()
    sp_change = MarketIndices().SP500Change()
    nasdaq_value = MarketIndices().NASDAQIndex()
    nasdaq_percent = MarketIndices().NasdaqPercent()
    nasdaq_change = MarketIndices().NASDAQChange()
    users_ticker_choice = users_request(variable)
    company = companySearch().check_for_company(variable)
    stock_price = companySearch().stock_price_func(variable)
    pe_ratio = companySearch().pe_ratio_func(variable)
    peg_ratio = companySearch().peg_ratio_func(variable)
    pb_ratio = companySearch().pb_ratio_func(variable)
    ps_ratio = companySearch().ps_ratio_func(variable)
    pfcf_ratio = companySearch().pfcf_ratio_func(variable)
    return render_template(
        "result.html",
        dow_jones_value=dow_jones_value,
        dow_jones_percent=dow_jones_percent,
        dow_jones_change=dow_jones_change,
        sp_value=sp_value,
        sp_percent=sp_percent,
        sp_change=sp_change,
        nasdaq_value=nasdaq_value,
        nasdaq_percent=nasdaq_percent,
        nasdaq_change=nasdaq_change,
        users_ticker_choice=users_ticker_choice,
        company=company,
        stock_price=stock_price,
        pe_ratio=pe_ratio,
        peg_ratio=peg_ratio,
        pb_ratio=pb_ratio,
        ps_ratio=ps_ratio,
        pfcf_ratio=pfcf_ratio)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
