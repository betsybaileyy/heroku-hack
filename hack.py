"""This module depletes a heroku free tier user's dyno hours."""
import time
import urllib.request


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
