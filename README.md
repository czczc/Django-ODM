# Offline Data Monitor

This version is developed under the [Django](https://www.djangoproject.com/) framework.

## Install

It's best to start in a new virtualenv (I recommend using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)) session

    mkvirtualenv odm
    workon odm
    git clone https://github.com/czczc/Django-ODM.git
    cd odm
    pip install -r requirements.txt

Take a look at the odm.conf.example file, change the content accordingly, and rename it as odm.conf

You should be able to start the local server now:
    
    python manage.py runserver 
