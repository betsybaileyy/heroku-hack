#!/bin/bash

# Change the app names to your Heroku app names
heroku_projects=(app-1 app-2 app-3)

for i in ${heroku_projects[@]}; do
  # Turn on maintenance mode so vistors know that the app is in "maintenance"
  heroku maintenance:on -a ${i}
  # Turn the web dyno off for each listed project above
  heroku ps:scale web=0 -a ${i}
done
