import requests, os, time, argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-id", help="ID of the game to grab stats of!")
args = parser.parse_args()

time.sleep(4)

game = f"https://www.roblox.com/games/{args.id}/"
r  = requests.get(game)
data = r.text
soup = BeautifulSoup(data, features="lxml")
stats = soup.findAll('li', attrs={'class' : 'game-stat'})

# FINDING STATS

# FIND NAME
game_title_container = soup.find("div", attrs={'class' : "game-title-container"})
game_title = game_title_container.find('h2', attrs={'class' : 'game-name'}).text

# FIND CREATOR
creator_container = game_title_container.find('div', attrs={'class' : 'game-creator'})
creator_name = creator_container.find('a', attrs={'class' : 'text-name'}).text
creator_link = creator_container.find('a', attrs={'class' : 'text-name'})['href']

# FIND CURRENT PLAYERS
current_players = stats[0]
player_count = current_players.find("p", attrs={'class': 'text-lead font-caption-body wait-for-i18n-format-render'}).text

# FIND FAVOURITES
favourites = stats[1]
favourite_count = favourites.find('p', attrs={'class' : 'text-lead font-caption-body wait-for-i18n-format-render'}).text

# FIND VISITS

visits = stats[2]
visit_count = visits.find('p', attrs={"id" : "game-visit-count"})['title']

# FIND CREATED

created = stats[3]
created_date = created.find('p', attrs={"class" : "text-lead font-caption-body"}).text

# FIND LAST UPDATED
updated = stats[4]
updated_date = updated.find('p', attrs={"class" : "text-lead font-caption-body"}).text

print("")
print("Grabbed these stats!")
print("Name: " + game_title.encode('ascii', 'ignore').decode('ascii'))
time.sleep(0.5)
print("Creator: " + creator_name + " (" + creator_link + ")")
time.sleep(0.5)
print("Current Players: " + player_count)
time.sleep(0.5)
print("Favourites: " + favourite_count)
time.sleep(0.5)
print("Visits: " + visit_count)
time.sleep(0.5)
print("Created Date: " + created_date)
time.sleep(0.5)
print("Last Updated: " + updated_date)

print("")
print("===== CREATOR INFORMATION =====")
print("")


json_file = requests.get(f'http://api.roblox.com/users/get-by-username?username={creator_name}')
json_data = json_file.json()
userid = json_data["Id"]

req = requests.get(f'https://www.roblox.com/users/{userid}/profile').content
soup = BeautifulSoup(req, 'html.parser')

soup2 = soup.find('div', {'class': 'hidden'})

followers = soup2.get('data-followerscount')
following = soup2.get('data-followingscount')
friends = soup2.get('data-friendscount')

# FINDING DATES

req = requests.get(f'https://www.roblox.com/users/{userid}/profile').content
soup = BeautifulSoup(req, 'lxml')
dates = soup.findAll('li', attrs={'class' : 'profile-stat'})

join_date_section = dates[0]
join_date = join_date_section.find('p', attrs={'class' : 'text-lead'}).text

total_visits = dates[1]
total_place_visits = total_visits.find('p', attrs={'class' : 'text-lead'}).text

print("Username: " + creator_name)
time.sleep(0.5)
print("Followers: " + followers)
time.sleep(0.5)
print("Friends: " + friends)
time.sleep(0.5)
print("Following: " + following)
time.sleep(0.5)
print("Join Date: " + join_date)
time.sleep(0.5)
print("Total Place Visits: " + total_place_visits)




