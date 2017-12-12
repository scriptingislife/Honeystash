# CloudsOfHoney

## Config setup
0. set variables group_vars/all

## Deploy
0. ansible-playbook -i hosts deploy_management_server.yml -u root

## Front-end
### Flask web application
#### Development
0. cd server/webapp
0. python run.py
   0. Be aware debugging is ENABLED
   0. Flask app listens on port 5000

#### Production


## Backend
### Elasticsearch


### MariaDB


###


## Docker


## To do
* email notifications
* Slack notifications
* logstash network filter
* implement CSRF
