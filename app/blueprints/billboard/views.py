from app import db
from flask import request, redirect, url_for, render_template, flash, Markup, Flask
from app.blueprints.billboard.models import Song
from flask_login import login_user, logout_user, current_user, login_required
from app.blueprints.billboard import bp as billboard_bp
import datetime 
import requests
import time
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from time import sleep
import pandas as pd
import sqlalchemy


# information on how to understand the top 100
# https://www.billboard.com/articles/columns/ask-billboard/5740625/ask-billboard-how-does-the-hot-100-work
    
# data goes from August, 4 1958 thru present
# https://www.billboard.com/articles/columns/chart-beat/6746273/first-billboard-issue-november-1-1894

@billboard_bp.route('/billboard', methods=['POST'])
def billboard_pull():
    if request.method == 'POST':
        # THIS WILL PULL DATABASE AND SEE WHAT DATES ALREADY EXIST
        engine = sqlalchemy.create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
        sql_data = pd.read_sql_table('song',engine)
    
        dates_dataset = sql_data[['start_of_week_date']]
        dates_dataset.drop_duplicates(inplace=True)
        dates_dataset['new_date'] = dates_dataset['start_of_week_date'].astype(str)

        num_dates_listed = pd.unique(dates_dataset['new_date'])
        print("-"*100)
        print(f'List of dates: {num_dates_listed}')
        num_dates_total_count = len(num_dates_listed)
        print(f'Total counts of dates: {num_dates_total_count}')
        print("-"*100)
        
        # THIS WILL CREATE DATES TO BE USED
        starter_date = datetime.datetime(1958, 8, 1)
        days = 365
        years = 63
        # days_times_years = days*years
        days_times_years = 820

        list_for_billboards = []
        string_dates_for_billboards = []
        for i in range(1, days_times_years):
            starter_date = starter_date + datetime.timedelta(days=1)
            day_of_week = starter_date.strftime("%u")
            if day_of_week == '7':
                string_output = str(starter_date.year)+"-"+str("{:02d}".format(starter_date.month))+"-"+str("{:02d}".format(starter_date.day))
                list_for_billboards.append(string_output)
        print("+"*100)
        print(f"This is the min value: {min(list_for_billboards)} and this is the max value {max(list_for_billboards)}")
        print(string_dates_for_billboards[0:20])
        print("+"*100)

        list_changeable_date = list_for_billboards

            
        # driver = webdriver.Chrome('/Users/enavs/Desktop/coding_temple/class/capstone_project/billboard_flask_version_V4/chromedriver')
        # driver.get(f'https://www.billboard.com/charts/hot-100/{changeable_date}')

        for date in list_changeable_date:
            if date in num_dates_listed:
                pass
            else:
                driver = webdriver.Chrome('/Users/enavs/Desktop/coding_temple/class/capstone_project/billboard_flask_version_V4/chromedriver')
                url_pull = f'https://www.billboard.com/charts/hot-100/{date}'
                print(f'Here is the URL: {url_pull}')

                driver.get(f'{url_pull}')

                driver.execute_script("window.scrollTo(0, 500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(500, 1000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(1000, 1500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(1500, 2000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(2000, 2500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(2500, 3000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(3000, 3500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(3500, 4000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(4000, 4500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(4500, 5000)") # goes through 40
                time.sleep(0.5)

                driver.execute_script("window.scrollTo(5000, 5500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(5500, 6000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(6000, 6500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(6500, 7000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(7000, 7500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(7500, 8000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(8000, 8500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(8500, 9000)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(9000, 9500)") 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(9500, 10000)") # goes through 80
                time.sleep(0.5)

                driver.execute_script("window.scrollTo(10000, 10500)") # goes through 84
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(10500, 11000)") # goes through 87-90
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(11000, 11500)") # 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(11500, 12000)") # 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(12000, 12500)") # 
                time.sleep(0.5)
                driver.execute_script("window.scrollTo(12500, 13000)") # 
                time.sleep(0.5)


                song_names = driver.find_elements_by_xpath('//span[@class="chart-element__information__song text--truncate color--primary"]')
                song_artists = driver.find_elements_by_xpath('//span[@class="chart-element__information__artist text--truncate color--secondary"]')
                song_rankings = driver.find_elements_by_xpath('//span[@class="chart-element__rank flex--column flex--xy-center flex--no-shrink"]')
                song_pictures = driver.find_elements_by_xpath('//span[@class="chart-element__image flex--no-shrink"]')

                song_name_list = []
                for s in range(len(song_names)):
                    song_name_list.append(song_names[s].text)
                # print(f'This is the song name: {song_name_list}')

                song_artist_list = []
                for a in range(len(song_artists)):
                    song_artist_list.append(song_artists[a].text)
                # print(f'This is the song artist: {song_artist_list}')

                song_rankings_list = []
                for r in range(len(song_rankings)):
                    r_element = song_rankings[r].text
                    r_text = r_element.split('\n')
                    r_int = int(r_text[0])
                    song_rankings_list.append(r_int)
                # print(f'This is the song artist: {song_rankings_list}')

                def parse_style_attribute(style_string):
                    if 'background-image' in style_string:
                        style_string = style_string.split(' url("')[1].replace('");', '')
                        return style_string
                    return None

                song_pictures_list = []
                count = 0
                for p in song_pictures:
                    count+=1
                    x = p.find_elements_by_xpath('//a[@style]')
                    o = p.get_attribute('style')
                    song_pictures_list.append(parse_style_attribute(o))
                    # print(f'This is count: {count} & this is the URL: {parse_style_attribute(o)}')
                song_pictures_list = [link for link in song_pictures_list]

                driver.close()

                data_tuples = list(zip(song_name_list[0:],song_rankings_list[0:],song_artist_list[0:],song_pictures_list[0:]))
                print(f'Here is the data_tuples list first 5: {data_tuples[0:5]}')


                for p in data_tuples:
                    song_name = p[0]
                    song_rank = p[1]
                    song_artist = p[2]
                    song_picture = p[3]

                    # start_of_week_date = datetime.datetime(int(changeable_date[0:4]), int(changeable_date[5:7]), int(changeable_date[-2:]))
                    start_of_week_date = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[-2:]))
                    song_name_artist_combined = (song_name+song_artist).replace(" ", "")

                    s = Song(song_name, song_rank, song_artist, song_picture, start_of_week_date, song_name_artist_combined)
                    db.session.add(s)

                db.session.commit()
    return redirect(url_for('main.explore'))


@billboard_bp.route('/billboard_song_date_pull', methods=['POST'])
def billboard_song_date_pull():
    if request.method == 'POST':
        # THIS WILL PULL DATABASE AND SEE WHAT DATES ALREADY EXIST
        engine = sqlalchemy.create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
        sql_data = pd.read_sql_table('song',engine)
    
        dates_dataset = sql_data[['start_of_week_date']]
        dates_dataset.drop_duplicates(inplace=True)
        dates_dataset['new_date'] = dates_dataset['start_of_week_date'].astype(str)

        num_dates_listed = pd.unique(dates_dataset['new_date'])
        print("-"*100)
        print(f'List of dates: {num_dates_listed}')
        num_dates_total_count = len(num_dates_listed)
        print(f'Total counts of dates: {num_dates_total_count}')
        print("-"*100)
        
        # THIS WILL CREATE DATES TO BE USED
        starter_date = datetime.datetime(1958, 8, 1)
        days = 365
        years = 63
        # days_times_years = days*years
        days_times_years = 820

        list_for_billboards = []
        string_dates_for_billboards = []
        for i in range(1, days_times_years):
            starter_date = starter_date + datetime.timedelta(days=1)
            day_of_week = starter_date.strftime("%u")
            if day_of_week == '7':
                string_output = str(starter_date.year)+"-"+str("{:02d}".format(starter_date.month))+"-"+str("{:02d}".format(starter_date.day))
                list_for_billboards.append(string_output)
        print("+"*100)
        print(f"This is the min value: {min(list_for_billboards)} and this is the max value {max(list_for_billboards)}")
        print(string_dates_for_billboards[0:20])
        print("+"*100)

        list_changeable_date = list_for_billboards
        print("_"*100)
        print(list_changeable_date[0:20])
        print("_"*100)

    return redirect(url_for('main.analysis'))


@billboard_bp.route('/billboard/redirect', methods=['POST'])
def billboard_pull_redirect():
    if request.method == 'POST':
        return redirect(url_for('main.explore'))

@billboard_bp.route('/billboard/redirect/analysis', methods=['POST'])
def billboard_pull_redirect_analysis():
    if request.method == 'POST':
        return redirect(url_for('main.analysis'))



