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
