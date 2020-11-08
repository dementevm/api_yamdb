## api_yamdb
API part for YamDB project, that allows to get data of users, titles, rewievs and comments.
## Prerequisites
Download and Install [Docker](https://www.docker.com/).
```
sudo apt update
```
```
sudo sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
```
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
```
```
sudo apt update 
```
```
sudo apt install docker-ce -y 
```
Download and install [Docker-compose](https://docs.docker.com/compose/install/)
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```
## Deployment
1. Download repository via github, or clone repository ```git clone https://github.com/dementevm/api_yamdb```
2. Navigate to project folder.
3. Execute command ```docker-compose up```

### Django commands
To use django commands via terminal from container follow next steps:
1. Get project container id - ```docker-container ls```
2. Enter container terminal - ``` docker exec -it <CONTAINER ID> bash```
Create superuser command - ```python manage.py createsuperuser```
Fillful database with test data - ``` python manage.py loaddata fixtures.json```

### Built With
[Django](https://www.djangoproject.com/) - web framework.

[Django REST Framework](https://www.django-rest-framework.org/) - toolkit for building Web APIs.

[Gunicorn](https://gunicorn.org/) - a Python WSGI HTTP Server for UNIX.

[Docker](https://www.docker.com/) - an open platform for developing, shipping, and running applications.

[Python](https://www.python.org/) - 🐍
