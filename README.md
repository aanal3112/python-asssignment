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

# Api 
This project has 3 api endpoints:

1. Add Repeat count
    URL: localhost:8000/add-repeat-counts/
    Method: POST
    Request param: {
        "coupon_code":"676767567",
        "per_user_weekly_repeat":10,
        "per_user_daily_repeat":3,
        "per_user_total_repeat":15,
        "global_total_repeat":100
    }
    Description: This api will take 5 request parameters
    coupon_code: this is string contain the coupon code 
    <!-- this is the repeat count configuration for coupon -->
    per_user_daily_repeat: this is the number of times user can repeat the coupon daily
    per_user_weekly_repeat: this is the number of times user can repeat the coupon weekly
    per_user_total_repeat : this is the number of times a user can repeat the coupon overall
    global_total_repeat: this is the number of times a coupon can repeat overall by all users

2. Verify Validity
    URL: localhost:8000/verify-validity/
    Method: POST
    Request param: {
        "coupon_code": "676767567"
    }
    Description: This api check the validity of the coupon if the coupon can be apply to the any user or not. it checks global_total_repeat and also coupon based on daily and weekly
    coupon_code: the code of coupon you want to check validity for

3. Apply Coupon
    URL: localhost:8000/apply-coupon/
    Method: POST
    Request param: {
        "coupon_code": "676767567"
    }
    Description: This api first check the validity of the coupon through verify-validity api and if the response is 200 it will create one objects in the RepeatCount model which contain the applied coupon. for now we have not asssign the coupon to any user just storing. This api will apply-until the verify api return 200,if it return the coupon verification failed means coupon validity exceeded.
    coupon_code: the code of coupon you want to apply


# Models
* we have created 2 Models Coupon and RepeatCount.
* Coupon: this model will store the coupon code and repeat count configuration detail.
* RepeatCount: this model will store the applied coupon and the time it created at.