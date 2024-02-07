import requests
import bs4
userAgent = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

url ="https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"

r = requests.get(url, headers=userAgent)
htmlText = r.text
htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")

table = htmlDocument.find('table', {'class': 'items'}).find('tbody')
teams = table.find_all('tr')

for i in range(len(teams)):
    team = teams[i]
    name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
    info = team.find_all("td", {"class": "zentriert"})
    squad = info[1].text
    age = info[2].text
    print(f"{i}:{name} {squad} {age}")


    
team = teams[0]
info = team.find_all("td", {"class": "zentriert"})
squad = info[1].text
age = info[2].text