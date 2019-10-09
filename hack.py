"""A function to deplete a heroku free tier user's dyno hours."""
import time
import urllib.request


def deplete_hours(app_links):
    while True:
        for link in app_links:
            urllib.request.urlopen(link)
            print("Called: ", link)

        print("Now sleeping for 30 minutes")
        seconds_in_30_min = 30 * 60
        time.sleep(seconds_in_30_min)


if __name__ == '__main__':
    # List the heroku app links here
    heroku_apps = [
        "https://app1.herokuapp.com/",
        "https://app2.herokuapp.com/",
        "https://app3.herokuapp.com/"
    ]

    deplete_hours(heroku_apps)
