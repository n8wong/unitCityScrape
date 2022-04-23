# Unit City Scraper
Outputs unit numbers to a file from html data from city map site

## Instructions

1. Install Python
Download: https://www.python.org/downloads/
OR If using Chocolatey:
choco install python

2. Install BeautifulSoup
In Powershell/Terminal
pip install beautifulsoup4

3. Get html data from city map sites
https://maps.vancouver.ca/property/#
https://gis.burnaby.ca/burnabymap/index.html

4. Create "Process" folder in the same directory as program.

5. Save html data in a txt file in "Process" folder. Name file the same as address so the program can match the correct address if multiple addresses are in the file.
### Example: 
Process\1234 Wilson.txt

6. Run script in Powershell/Terminal
cd [folder location of app]
py unitCityScrape.py [address] --city [[V]ancouver (default) or [B]urnaby]

### Examples:
py unitCityScrape.py '1234 Wilson'
py unitCityScrape.py '5555 McKay' --city B

7. Unit numbers will be saved in "Process\Complete" folder as [address]_unit.txt