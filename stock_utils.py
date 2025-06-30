import requests
from bs4 import BeautifulSoup

def get_nabil_price():
    # Simple example: scrape from MeroLagani or another site
    url = "https://merolagani.com/CompanyDetail.aspx?symbol=NABIL"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find(id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblPrice").text.strip()
    return price
