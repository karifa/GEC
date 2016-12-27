# GEC
Gestion electronique de courrier


# Ubuntu 
sudo apt-get install python3

sudo apt-get install python3 pip

pip install virtualenv

sudo apt-get install python3-dev libpq-dev postgresql postgresql-contrib

# Windows 

You need to install:
  1- python3
  2- pip3
  3- virtualenv
  4- postgresql
  
# Virtualenv 

virtualenv <venv_name>
cd <venv_name>
source bin/activate
git clone https://github.com/karifa/GEC.git
cd GEC
pip install -r requirements.txt

# Postgresql

sudo su - postgres

psql

CREATE DATABASE gec;

CREATE USER gec WITH PASSWORD 'gec';


# Run the App

python manage.py runserver <port>


