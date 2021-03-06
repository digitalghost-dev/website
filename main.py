# Importing needed modules, packages
import os
import pytz
from config import powerlink2
from market import MarketIndices
from metrics import CompanySearch
from urllib.request import urlopen
from datetime import datetime, date
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

def key_to_all():
    return powerlink2

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
 
# Routing to the home page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def project():
    return render_template("projects.html")

# Routing to the search page
@app.route('/projects/search', methods = ["GET", "POST"])
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
        "search.html",
        market_status = market_hours(),
        powerlink2 = key_to_all(),
        dow_jones_value = dow_jones_value,
        dow_jones_percent = dow_jones_percent,
        dow_jones_change = dow_jones_change,
        sp_value = sp_value,
        sp_percent = sp_percent,
        sp_change = sp_change,
        nasdaq_value = nasdaq_value,
        nasdaq_percent = nasdaq_percent,
        nasdaq_change = nasdaq_change)

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
    company = CompanySearch().check_for_company(variable)
    stock_price = CompanySearch().stock_price_func(variable)
    pe_ratio = CompanySearch().pe_ratio_func(variable)
    peg_ratio = CompanySearch().peg_ratio_func(variable)
    pb_ratio = CompanySearch().pb_ratio_func(variable)
    ps_ratio = CompanySearch().ps_ratio_func(variable)
    pfcf_ratio = CompanySearch().pfcf_ratio_func(variable)
    return render_template(
        "result.html",
        dow_jones_value = dow_jones_value,
        dow_jones_percent = dow_jones_percent,
        dow_jones_change = dow_jones_change,
        sp_value = sp_value,
        sp_percent = sp_percent,
        sp_change = sp_change,
        nasdaq_value = nasdaq_value,
        nasdaq_percent = nasdaq_percent,
        nasdaq_change = nasdaq_change,
        users_ticker_choice = users_ticker_choice,
        company = company,
        stock_price = stock_price,
        pe_ratio = pe_ratio,
        peg_ratio = peg_ratio,
        pb_ratio = pb_ratio,
        ps_ratio = ps_ratio,
        pfcf_ratio = pfcf_ratio)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
