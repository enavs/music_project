# https://beshaimakes.com/js-scrape-data#write-a-nodejs-script-to-scrape-the-page

import requests
from bs4 import BeautifulSoup
import datetime 
import re
import time

changeable_date = '1958-08-03'

URL = f'https://www.billboard.com/charts/hot-100/{changeable_date}'

time.sleep(5)


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("ol", class_="chart-list__elements")
song_elements_listed = results.find_all('li', class_='chart-list__element')

initial_data = {}
for i in song_elements_listed:
    # data = {}

    song_name = i.find('span', class_='chart-element__information__song').get_text()

    # data["song_name"] = song_name
    # initial_data.add(data)
# print(initial_data)

    song_rank = i.find('span', class_='chart-element__rank__number').get_text()
    song_artist = i.find('span', class_='chart-element__information__artist').get_text()

    song_this_week = i.find('span', class_='chart-element__rank__number').get_text()
    song_last_week = i.find('span', class_='text--last').get_text()
    song_artist_peak_rank = i.find('span', class_='text--peak').get_text()
    song_artist_weeks_on_chart = i.find('span', class_='text--week').get_text()

    # song_picture_pull = i.find('span', class_='chart-element__image')
    # <span class="chart-element__image flex--no-shrink" style="background-image: url(&quot;https://charts-static.billboard.com/img/1958/08/duane-eddy-vt9-155x155.jpg&quot;);"></span>

    # song_picture_pull2 = str(song_picture_pull)
    # song_picture_pull2 = song_picture_pull.split('url(')

    # if len(song_picture_pull2) > 1:
    #     song_picture_pull3 = song_picture_pull2[1]
    # else:
    #     song_picture_pull3 = song_picture_pull2[0]

    # song_picture_pull4 = song_picture_pull3.split(');"')

    # if song_picture_pull == '<span class="chart-element__image flex--no-shrink" style=""></span>':
    #     song_picture = 'https://www.billboard.com/assets/1615852063/images/charts/bb-placeholder-new.jpg?09e28abc0eae1b8efc3f'
    # else:
    #     song_picture = song_picture_pull4[0]

    # song_picture_pull = i.find('span', class_='chart-element__image')
    # song_picture_pull2 = str(song_picture_pull)
    # front = song_picture_pull2.find('url(')
    # back = song_picture_pull2.find(');">')
    # song_picture = song_picture_pull2[front+5:back-1]

    strings = str(i)
    # song_picture_pull = re.search('http', strings)
    # song_picture_pull2 = re.search('.jpg', strings)
    # front = song_picture_pull.span()
    # back = song_picture_pull2.span()
    # song_picture = strings[front[0]:back[1]]

    start_of_week_date = datetime.datetime(int(changeable_date[0:4]), int(changeable_date[5:7]), int(changeable_date[-2:]))

    # if None in (song_name, song_rank, song_artist, song_this_week, song_last_week, song_artist_peak_rank, song_artist_weeks_on_chart, song_picture, start_of_week_date):
    #     continue
    # print(song_name, song_rank, song_artist, song_this_week, song_last_week, song_artist_peak_rank, song_artist_weeks_on_chart, song_picture, start_of_week_date)

    # print(song_name)
    # print(song_rank)
    # print(song_picture_pull)
    # print(song_picture_pull2)
    # print(song_picture_pull3)
    # print(song_picture_pull4)
    # print(song_picture)
    # print()

    print(song_name)
    print(song_rank)
    print(strings)
    # print(song_picture_pull)
    # print(song_picture_pull2)
    # print(front)
    # print(back)
    # print(song_picture)
    # print()