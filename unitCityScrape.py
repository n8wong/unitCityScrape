######################
# Unit City Scraper
## Outputs unit numbers to a file from html data from city map site
######################
# Instructions
######################

# 1. Install Python
## Download: https://www.python.org/downloads/
## OR If using Chocolatey:
## choco install python

# 2. Install BeautifulSoup
## In Powershell/Terminal
## pip install beautifulsoup4

# 3. Get html data from city map sites
## https://maps.vancouver.ca/property/#
## https://gis.burnaby.ca/burnabymap/index.html

# 4. Save html data in a txt file
## 1234WilsonSt.txt

# 5. Run script in Powershell/Terminal
## cd [folder location of app]
## py unitCityScrape.py [path/filename.txt] --city [[V]ancouver (default) or [B]urnaby]

# 6. Unit numbers will output to [filename]_unit.txt

import argparse
import io
import os

from bs4 import BeautifulSoup

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A utility to scrape units from Vancouver/Burnaby City Maps')
    parser.add_argument('infile_path', help='Input File Path')
    parser.add_argument('--city', help='City ([V]ancouver or [B]urnaby)')
    parser.add_argument('--address', help='Specify Address')
    args = parser.parse_args()
    
    infile = io.open(args.infile_path, mode="r", encoding="utf-8-sig")
    file = os.path.splitext(os.path.basename(args.infile_path))
    outfile = io.open(file[0] + '_units' + file[1], mode="w", encoding="utf-8-sig")
    
    html_doc = infile.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print(soup.prettify())

    city = args.city and args.city.upper() or args.city
    address = args.address and args.address.upper() or ''

    print(address)

    prevUnit = ""	
    address2 = ""
	
    #Vancouver (Default)
    if city == 'V' or city == None:
        items = soup.find_all("li", id=lambda value: value.split('-')[0].strip().isdigit())
        #ids = [tag['id'] for tag in soup.select('div[id]')]
        items.sort(key=lambda e: int(e['id'].split('-')[0].strip()))

        for i in items:
            # print(i)
            line = i['id'].split('-')
            unit = line[0].strip()
            
            if address != "":
                address2 = line[1].strip().upper()
                #print(address2)

            if prevUnit != unit and address in address2:				
                print(unit + " - " + address2)
                outfile.write(unit + '\n')
            prevUnit = unit 

    #Burnaby
    elif city == 'B':
        
        items = soup.find_all("a", string=lambda value: value.endswith('(Alias)'))
        x = 2
        if len(items) == 0:
            items = soup.find_all("a")
            x = 1
        
        items.sort(key=lambda e: int(e.string.split()[len(e.string.split())-x]))

        for i in items:
            # print(i)
            line = i.string.split()
            unit = line[len(line)-x]
            print(unit)
            outfile.write(unit + '\n')

    print('Done!')