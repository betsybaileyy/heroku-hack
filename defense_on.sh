#!/bin/bash

# Change the app names to your Heroku app names
heroku_projects=(app-1 app-2 app-3)

for i in ${heroku_projects[@]}; do
  # Turn the web dyno on for each listed project above
  heroku ps:scale web=1 -a ${i}
  # Turn off maintenance mode so that the app can be visited
  heroku maintenance:off -a ${i}
done
