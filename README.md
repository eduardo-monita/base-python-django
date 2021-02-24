# base-python-django

pip install --upgrade pip
pip install virtualenv
virtualenv venv -p python3
venv/Scripts/activate

pip install -r requirements.txt

django-admin startproject main

cd app
python manage.py startapp example app

python manage.py migrate

python manage.py collectstatic
python manage.py createsuperuser

python manage.py makemigrations

python manage.py migrate

python manage.py runserver