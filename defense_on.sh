#!/bin/bash

# Change the app names to your Heroku app names
heroku_projects=(app-1 app-2 app-3)

# Turn the web dyno on for each listed project above
for i in ${heroku_projects[@]}; do
  heroku ps:scale web=1 -a ${i}
done
