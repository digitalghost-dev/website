# minimalfire.app
***DISCLAIMER:*** I am not a financial advisor, this program is for educational purposes, and should not be taken as investment advice.

***NOTE:*** This README.md is split into two parts: The **Jupyter Notebook** version and the **Python Web App** version.

Check out the [wiki](https://github.com/SquareHammer89/stock-data/wiki) for version history and more details.

## Jupyter Notebooks
The project first started with Jupyter Notebooks to practice web-scraping and certain Python libraries such as pandas ant matplotlib. 

View the **Stock Quotes.ipynb** file to browse the code.

### Functionalities of this Program

- Displays current date.
- Displays local time for EST which matches the US market hours.
- Displays whether the US market is open or closed. Does not account for US holidays as of yet.
- Returns the full company name and its sector.
- Returns the P/E, PEG, P/B, P/FCF, Dividend, Dividend %, ROE, and Year-to-Date Performance on given company.
- Shows a graph displaying EPS history for the last 8 quarters.
- If the company pays a dividend, it will also calculate how many shares of the given company you will need in order to buy a whole new share each quarter with only dividends being invested.

#### Libraries Used:
- pytz
- requests
- pandas
- BeautifulSoup
- matplotlib
- datetime

## Python Web App
I'm currently working on a web app version of the program. This will be a full-feature website that will be worked on constantly.

This project is focused on providing financial information for companies listed on major U.S. stock markets.

I use Google Cloud Platform to host the web app and Flask as the framework.
View the **google-cloud-app** folder to view the files used to build the web app.
