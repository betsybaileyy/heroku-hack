#!/bin/bash

heroku_projects=(app-1 app-2 app-3)

for i in ${heroku_projects[@]}; do
  heroku ps:scale web=0 -a ${i}
done
