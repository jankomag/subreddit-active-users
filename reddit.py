#importing libraries
import json
import requests
import sched, time
from datetime import datetime
import matplotlib.pyplot as plt 


#get user input on which subreddit to parse

subreddit = input("What subreddit do you want to check?")

#function for getting the count

def get_active_users(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
    data = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers).json()
    active_user_count = data['data']['active_user_count']
    return active_user_count

#repeat function every hour
now = datetime.now()
current_hour = now.strftime("%H:%M")

user_per_hour = {  # defining a dictionary to store the results in
}

while len(user_per_hour) < 24:
    now = datetime.now()
    current_hour = now.strftime("%H:%M")
    time.sleep(3600)
    currently_users = get_active_users(subreddit)
    user_per_hour.update( {current_hour : currently_users} )
    print(user_per_hour)

print(user_per_hour)

#plot the result
plt.plot(*zip(*sorted(user_per_hour.items())))
plt.show()