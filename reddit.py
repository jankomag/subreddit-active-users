import json
import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt 

subreddit = input("What subreddit do you want to check?")

#function for getting the count of active users
def get_active_users(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
    data = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers).json()
    active_user_count = data['data']['active_user_count']
    return active_user_count

#specify the timeframe
number_of_inputs = int(input("How many measurments do you want?"))
time_interval = int(input("What do you want the time interval to be? (60 = one minute)"))

# run the function repeatedly over the specified timeframe
now = datetime.now()
current_hour = now.strftime("%H:%M:%S")

user_per_hour = {  # defining a dictionary to store the results in
}

while len(user_per_hour) < number_of_inputs:
    now = datetime.now()
    current_hour = now.strftime("%H:%M:%S")
    time.sleep(time_interval)
    currently_users = get_active_users(subreddit)
    user_per_hour.update( {current_hour : currently_users} )
    print(user_per_hour)

print(user_per_hour)


#plot the result
plt.plot(*zip(*sorted(user_per_hour.items())))
plt.tight_layout()
plt.xticks(rotation=90)
plt.title(f"Active users on r/{subreddit}", loc='center')
plt.xlabel('Time')
plt.ylabel('Active Users')
plt.gcf().subplots_adjust(bottom=0.2, top=0.9, left=0.1) # adjusting the plotting area
plt.savefig(f"{subreddit}_users_graph.png")
plt.show()
