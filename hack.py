import time
import urllib.request

# List the heroku app links here
heroku_apps = [
    "https://app1.herokuapp.com/",
    "https://app2.herokuapp.com/",
    "https://app3.herokuapp.com/"
]

while True:
    for app in heroku_apps:
        urllib.request.urlopen(app)
        print("Called: ", app)

    print("Now sleeping for 30 minutes")
    seconds_in_30_min = 30 * 60
    time.sleep(seconds_in_30_min)
