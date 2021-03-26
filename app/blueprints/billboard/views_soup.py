from app import db
from flask import request, redirect, url_for, render_template, flash, Markup, Flask
from app.blueprints.billboard.models import Song
from flask_login import login_user, logout_user, current_user, login_required
from app.blueprints.billboard import bp as billboard_bp
from bs4 import BeautifulSoup
import datetime 
import requests
import time


# information on how to understand the top 100
# https://www.billboard.com/articles/columns/ask-billboard/5740625/ask-billboard-how-does-the-hot-100-work
    
# data goes from August, 4 1958 thru present
# https://www.billboard.com/articles/columns/chart-beat/6746273/first-billboard-issue-november-1-1894

@billboard_bp.route('/billboard', methods=['POST'])
def billboard_pull():
    if request.method == 'POST':
        # try:
            # changeable_date = '1958-08-03'
            # changeable_date = '1958-08-10'
            # changeable_date = '1958-08-17'
            # changeable_date = '1958-08-24'
            # changeable_date = '1958-08-31'
            changeable_date = '1958-09-07'
            # changeable_date = '1958-09-14'
            # changeable_date = '1958-09-21'
            # changeable_date = '1958-09-28'
            # changeable_date = '1958-10-05'


            URL = f'https://www.billboard.com/charts/hot-100/{changeable_date}'

            page = requests.get(URL)
            time.sleep(6)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find("ol", class_="chart-list__elements")
            song_elements_listed = results.find_all('li', class_='chart-list__element')

            initial_data = {}
            for i in song_elements_listed:
                song_name = i.find('span', class_='chart-element__information__song').get_text()
                song_rank = i.find('span', class_='chart-element__rank__number').get_text()
                song_artist = i.find('span', class_='chart-element__information__artist').get_text()

                song_this_week = i.find('span', class_='chart-element__rank__number').get_text()
                song_last_week = i.find('span', class_='text--last').get_text()
                song_artist_peak_rank = i.find('span', class_='text--peak').get_text()
                song_artist_weeks_on_chart = i.find('span', class_='text--week').get_text()

                # song_picture_pull = str(i.find('span', class_='chart-element__image'))
                # song_picture_pull2 = song_picture_pull.split('url(')

                # if len(song_picture_pull2) > 1:
                #         song_picture_pull3 = song_picture_pull2[1]
                # else:

                #     song_picture_pull3 = song_picture_pull2[0]

                # song_picture_pull4 = song_picture_pull3.split(');"')
                # song_picture = song_picture_pull4[0]

                song_picture_pull = str(i.find('span', class_='chart-element__image'))
                song_picture_pull2 = str(song_picture_pull)
                front = song_picture_pull2.find('url(')
                back = song_picture_pull2.find(');">')
                song_picture = song_picture_pull2[front+5:back-1]

                start_of_week_date = datetime.datetime(int(changeable_date[0:4]), int(changeable_date[5:7]), int(changeable_date[-2:]))
                song_name_artist_combined = (song_name+song_artist).replace(" ", "")

                if None in (song_name, song_rank, song_artist, song_this_week, song_last_week, song_artist_peak_rank, song_artist_weeks_on_chart, song_picture, start_of_week_date, song_name_artist_combined):
                    continue

                s = Song(song_name, song_rank, song_artist, song_this_week, song_last_week, song_artist_peak_rank, song_artist_weeks_on_chart, song_picture, start_of_week_date, song_name_artist_combined)
                db.session.add(s)
                db.session.commit()
        # except:
        #     flash('There was an error creating your billboard data. Try again.', 'danger')
    return redirect(url_for('main.explore'))


@billboard_bp.route('/billboard/redirect', methods=['POST'])
def billboard_pull_redirect():
    if request.method == 'POST':
        return redirect(url_for('main.explore'))

@billboard_bp.route('/billboard/redirect/analysis', methods=['POST'])
def billboard_pull_redirect_analysis():
    if request.method == 'POST':
        return redirect(url_for('main.analysis'))



