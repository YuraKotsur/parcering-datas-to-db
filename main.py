import sqlite3
from bs4 import BeautifulSoup
import requests


mouse_name = []
mouse_price = []
i = 0


response = requests.get("https://rozetka.com.ua/igrovie-mishi/c4673278/producer=razer/")
soup = BeautifulSoup(response.text, 'lxml')


con = sqlite3.connect('goods.db')
cur = con.cursor()
cur.execute("CREATE TABLE game_mouses ('mouse_name', 'mouse_price')")


for title in soup.find_all('span', class_='goods-tile__title'):
	mouse_name.append(title.text)
	
for price in soup.find_all('div', class_='goods-tile__price'):
	mouse_price.append(price.text.replace('\xa0', ''))
	

while i < len(mouse_name):
	cur.execute('INSERT INTO game_mouses VALUES (?,?)', (str(mouse_name[i]),(str(mouse_price[i]))))
	i += 1



con.commit()



