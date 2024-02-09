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

'''Funktion gibt leider auch market value der Spieler, ich weiß aber nicht wie ich die Suche "rechts hauptlink" 
ignorieren lassen kann.'''

def player_names(url):
    r = requests.get(url, headers=userAgent)
    htmlText = r.text
    htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")
    table = htmlDocument.find('table', {'class': 'items'}).find("tbody")
    players = table.find_all("td", {"class":"hauptlink"})
    for p in players:
        print(p.text)

print("1: Show available teams")
print("2: Select team and show high level information on the team")
print("3: Select team and and show all players of the team")
print("4: Stop the program")

while True:
    choice = int(input())
    if choice == 1:
        for i in range(len(teams)):
            team = teams[i]
            name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
            print(f"{i}: {name}")
    elif choice == 2:
        teamChoice = int(input("Give the index of the team you are interested in (note they start with 0)\n"))
        team = teams[teamChoice]
        name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
        info = team.find_all("td", {"class": "zentriert"})
        marketValue = team.find_all("td", {"class": "rechts"})
        squad = info[1].text
        age = info[2].text
        foreigners = info[3].text
        averageMV = marketValue[0].text
        totalMV = marketValue [1].text
        print(f"{name}: \nMembers: {squad} \nAverage age: {age} \nNumber of foreigners: {foreigners} \nAverage value: {averageMV} \nTotal value: {totalMV}")
    elif choice == 3:
        choice2 = int(input("Give the index of the team you are interested in (note they start with 0)\n"))
        if choice2 == 0:
            urlChoice = "https://www.transfermarkt.com/fc-bayern-munchen/startseite/verein/27/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 1:
            urlChoice = "https://www.transfermarkt.com/bayer-04-leverkusen/startseite/verein/15/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 2:
            urlChoice = "https://www.transfermarkt.com/rasenballsport-leipzig/startseite/verein/23826/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 3:
            urlChoice = "https://www.transfermarkt.com/borussia-dortmund/startseite/verein/16/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 4:
            urlChoice = "https://www.transfermarkt.com/vfl-wolfsburg/startseite/verein/82/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 5:
            urlChoice = "https://www.transfermarkt.com/vfb-stuttgart/startseite/verein/79/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 6:
            urlChoice = "https://www.transfermarkt.com/eintracht-frankfurt/startseite/verein/24/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 7:
            urlChoice = "https://www.transfermarkt.com/borussia-monchengladbach/startseite/verein/18/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 8:
            urlChoice = "https://www.transfermarkt.com/sc-freiburg/startseite/verein/60/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 9:
            urlChoice = "https://www.transfermarkt.com/1-fc-union-berlin/startseite/verein/89/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 10:
            urlChoice = "https://www.transfermarkt.com/tsg-1899-hoffenheim/startseite/verein/533/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 11:
            urlChoice = "https://www.transfermarkt.com/fc-augsburg/startseite/verein/167/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 12:
            urlChoice = "https://www.transfermarkt.com/1-fsv-mainz-05/startseite/verein/39/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 13:
            urlChoice = "https://www.transfermarkt.com/sv-werder-bremen/startseite/verein/86/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 14:
            urlChoice = "https://www.transfermarkt.com/1-fc-koln/startseite/verein/3/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 15:
            urlChoice = "https://www.transfermarkt.com/vfl-bochum/startseite/verein/80/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 16:
            urlChoice = "https://www.transfermarkt.com/1-fc-heidenheim-1846/startseite/verein/2036/saison_id/2023"
            player_names(urlChoice)
        if choice2 == 17:
            urlChoice = "https://www.transfermarkt.com/sv-darmstadt-98/startseite/verein/105/saison_id/2023"
            player_names(urlChoice)
    elif choice == 4:
        break
    else:
        print("Invalid Option!")








