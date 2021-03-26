# NEW YORK TIMES
# https://www.thisismetis.com/made-at-metis
# https://pgr-me.github.io/Marijuana/?_ga=2.204741207.691523129.1615838692-1501198656.1615838692
# https://github.com/pgr-me/metis_projects/blob/master/04-marijuana/library/utilities.py

# https://medium.com/@danalindquist/using-new-york-times-api-and-jq-to-collect-news-data-a5f386c7237b

import requests

your_key = 'VYuGvKX4CjjkpouRBYB36uajLID6et1V'

url = 'http://api.nytimes.com/svc/archive/v1/2018/12.json?&api-key='+your_key
r = requests.get(url)
jason_data = r.json()
print(jason_data)

# for d in jason_data:
#     print(d)
#     break







