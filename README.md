The clean, fast and right way to start a new Django `4.2.8` powered website.

## Versions
Python 3.8.10
Django == 4.2.8
djangorestframework==3.14.0

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r requirements.txt

$ cd api/
# Make sure add database cradentials inside settings.py file before execute migrate commad.
$ python manage.py migrate

$ python manage.py createsuperuser
# When prompted, type your username (lowercase, no spaces), email address, and password. Don't worry that you can't see the password you're typing in – that's how it's supposed to be. Type it in and press enter to continue. The output should look like this (where the username and email should be your own ones):
# Username: <USERNAME>
# Email address: <EMAIL_ID>
# Password:
# Password (again):
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.
