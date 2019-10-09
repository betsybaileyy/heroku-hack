"""This module depletes a heroku free tier user's dyno hours."""
import time
import urllib.request
from datetime import datetime


def deplete_hours(app_links):
    """
    Pings the same user's heroku apps to deplete their hours.

    This function runs until the user manually stops it. It
    makes requests to the apps every 30 minutes to keep the
    apps awake.

    Args:
        app_links (arr): An array of strings which contain
            the urls for heroku apps.

    """
    while True:
        for link in app_links:
            urllib.request.urlopen(link)
            print("Called: ", link)

        now = datetime.now()
        h = now.hour
        m = now.minute
        print(f"Now sleeping for 30 minutes starting at: {h}:{m}")
        seconds_in_30_min = 30 * 60
        time.sleep(seconds_in_30_min)


if __name__ == '__main__':
    # List the heroku app links here
    heroku_apps = [
        "https://google.com",
        "https://apple.com",
        "https://facebook.com"
    ]

    deplete_hours(heroku_apps)
