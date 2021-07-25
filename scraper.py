import requests, re
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook

url = "http://kmpdc.go.ke/Registers/H-Facilities.php"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})

soup = BeautifulSoup(response.content, "html.parser")
facility_list = []
new_space = []

for item in soup.find_all("tr"):
    facility = item.get_text("td")
    new_string = re.sub(r'td', "", facility)
    facility_list.append(new_string.split('\n'))

facility_table = pd.DataFrame(facility_list)

facility_table.to_excel("Registered Facilites.xlsx")