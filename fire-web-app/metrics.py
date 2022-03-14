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

# This class returns information about the company
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
