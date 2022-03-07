# minimalfire.app
***DISCLAIMER:*** I am not a financial advisor, this program is for educational purposes, and should not be taken as investment advice.

This repository holds the code for my web app, my first ever coding project.

This web app's backend is built with Python, the first language I started to learn. The **Jupyter Notebook** file in this repository is where this project first started to take shape and lay the foundation for the web app. It also was a way for me to practice data scraping.

The **Jupyter Notebook** file has the following functionlites:
* Prints today's date
* Prints the current time on the East Coast (matches market hours)
* Prints whether the market is open or not
* Allow user input of a ticker symbol only
* Prints the company name
* Prints the sector of the company
* Returns the following metrics: current price, P/E, PEG, P/B, P/FCF, dividend, dividend %, ROE, YTD performance
* Displays a matplotlib chart of the EPS history for the last eight quarters
* Calculates how many shares you will need to buy a whole new share with only dividend reinvesment

With creating the web app, I couldn't data scrap my way through it so using [Financial Modeling Prep](https://site.financialmodelingprep.com/developer)'s API, I set out to pull and display the same (eventually more) information about a certain company, just like the **Jupyter Notebook**.

This web app is now taking shape to become my personal website with these features (and more to be added in the future) instead of having two different websites.

Read the wiki