# Welcome to Heroku Hacks!
===========================
Heroku logs can't save you now
------------------------------

#### The goal of this application is to toy with people's "free" hours on Heroku and use up all 100 "free" hours of web hosting time within a matter of days.

##### We would never actually do this, of course.........

### STEPS TO ACHIEVE GOAL of HEROKU HACK:
1. Find addresses of the websites we want to ping.
    a. Verify that they are hosted on Heroku and using the "free" 100 hours of web hosting time.
2. We know that a "free" Heroku app goes to sleep after 30 minutes of inactivity. So, we will write a script that pings or "wakes up" the said webiste every 30 minutes.

### Only two steps, pretty straight forward!

Here is a table with how fast you can deplete someone's free hours, and the percent out of 30 days their apps will be down. As you can see, you must find at least 2 free tier apps made by the same person to cause downtime for all of their free apps.

| App Count | Time to Deplete      | Percent of 30 days down |
|-----------|----------------------|-------------------------|
| 1         | 41 days 16 hours     | 0%                      |
| 2         | 20 days 20 hours     | 30.56%                  |
| 3         | 13 days 21.333 hours | 53.70%                  |
| 4         | 10 days 10 hours     | 65.28%                  |
| 5         | 8 days 8 hours       | 72.22%                  |
| 6         | 6 days 22.666 hours  | 76.85%                  |
| 7         | 5 days 22.857 hours  | 80.16%                  |
| 8         | 5 days 5 hours       | 82.64%                  |
| 9         | 4 days 15.111 hours  | 84.57%                  |
| 10        | 4 days 4 hours       | 86.11%                  |

For learning purposes, we created a simple python script to show how easy it is to drain someone's Heroku hours.

```
$ python3 hack.py
```

The script will run indefinitely, and can be ran on any hardware with an internet connection and Python 3.

Now, how can you prevent our super sophisticated hack from impacting your precious Heroku hours? Lets take a look.

STEPS TO PREVENT the HEROKU HACK:
1. Heroku uses "dynos"

If you ever find that you are under this attack, or you just want to have your app running at certain times, we also created a couple bash scripts that can be ran manually, or with `crontab`, to turn on and off your heroku apps.

Running `defense_off.sh` manually:
```
$ bash ./defense_off.sh
```
or with `crontab` (should already be installed on Mac and Linus machines) every night at 11 PM
```
0 23 * * * ./defense_off.sh
```
will turn the heroku web dynos off.

Running `defense_on.sh` manually:
```
$ bash ./defense_on.sh
```
or with `crontab` (should already be installed on Mac and Linus machines) every night at 8 AM
```
0 8 * * * ./defense_on.sh
```
will turn the heroku web dynos back on.
