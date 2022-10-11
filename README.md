# Fsbmcours - Bibliothèque on Ligne

Fsbmcours is a Bibliothèque on Ligne , that give a archives (course and traveux d) for students , Because through my previous experience in which i studeied at the university , most of the time we suffer from references of my faculte, the main idea is to solve this problem

<h1>etting Started</h1>
<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>


## Prerequisites
* asgiref==3.4.1 
* cffi==1.15.0 
* cryptography==35.0.0 
* Django==3.2.8
* django-cors-headers==3.8.0
* Pillow==8.4.0
* pycparser==2.20
* PyMySQL==1.0.2
* pytz==2021.3
* sqlparse==0.4.2
* whitenoise==5.3.0
<br>
## Setup Commands
<pre>open terminal and type</pre>

1. clone this project 
```
$ git clone https://github.com/mmasstou/Fsbmcours.git
```
<h4>or simply download using the url below</h4>
<code>https://github.com/mmasstou/Fsbmcours.git</code><br>


 For database i use Mysql </h2>
1. After install mysql, Create Databasein mysql shell using these commands
    1. `CREATE DATABASE db_fsbmcours ;`
    2. `CREATE USER fsbmcours_user with PASSWORD 'password' ;`
    3. `GRANT ALL PRIVILEGES ON DATABASE db_fsbmcours TO fsbmcours_user ;`

2. and fill **database name** , **database password** and **user** in `settings.py` like
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_fsbmcours',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'fsbmcours_user',
        'PASSWORD': 'password',
    }
}
```

3.  Create Environment using :  `python3 -m venv .env`
4. activate this **.env** using `source .env/bin/activate` 
5. install the requirements file using `pip3 install -r requirements.txt`

6. To migrate the database open terminal in project directory and type
```
    python manage.py makemigrations
    python manage.py migrate
```
7. then , simply run the server using this command :
```
python manage.py runserver
```
## demo image
<div align="center">
    <img src="https://github.com/mmasstou/Fsbmcours/blob/main/demo_img/home_page.png" width="100%">
</div>