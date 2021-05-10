import urllib.request
import os
from bs4 import BeautifulSoup
import lxml

# Download latest cab file
url = "http://downloads.dell.com/catalog/DriverPackCatalog.cab"
## urllib.request.urlretrieve(url, "DriverPackCatalog.cab")

# Extract cab file
## os.system("expand *.cab -F:* -I")

with open('DriverPackCatalog.xml', 'r') as f:
    data = f.read()
    bs_data = BeautifulSoup(data, "lxml")


b_driverpackage = bs_data.find_all('Model')

#print(bs_data)

print(b_driverpackage)