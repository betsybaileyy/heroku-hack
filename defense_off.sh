#!/bin/bash

heroku_projects=(app1 app1 app3)

for i in ${heroku_projects[@]}; do
  heroku ps:scale web=0 -a ${i}
done
