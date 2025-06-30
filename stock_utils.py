import requests
from bs4 import BeautifulSoup

def import requests
from bs4 import BeautifulSoup

def get_nabil_price():
    url = "https://www.nepalstock.com.np/company/show/140"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.prettify())  # 👈 Add this

    price = soup.find(id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblPrice").text.strip()
    return price

