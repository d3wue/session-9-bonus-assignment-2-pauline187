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
    elif choice == 4:
        break
    else:
        print("Invalid Option!")

#for i in range(len(teams)):
#    team = teams[i]
#    name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
#    info = team.find_all("td", {"class": "zentriert"})
#    squad = info[1].text
#    age = info[2].text
#    foreigners = info[3].text
#    marketValue = team.find_all("td", {"class": "rechts"})
#    averageMV = marketValue[0].text
#    totalMV = marketValue [1].text
#    print(f"{i}:{name} {squad} {age} {foreigners} {averageMV} {totalMV}")

url = f"https://www.transfermarkt.com/{name}/startseite/verein/saison_id/20232"