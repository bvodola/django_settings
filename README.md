# bvodola/django_settings

This is my approach to the django development/production settings issue.

Instructions

1. Clone this repo

  `git clone https://github.com/bvodola/django_settings.git`
  
2. Paste the settings_* files in the same directory as settings.py. You should have something like this:
  
  - myproject
    - myproject
      - settings.py
      - settings_dev.py
      - settings_env.py
      - settings_prod.py
  

3. Inside **settings.py**, delete the DEBUG, ALLOWED_HOSTS, DATABASE and STATIC_* settings and add the following at the end of the file:

  `from .settings_env import *`

4. Inside **settings_env.py**, fill both DEV_HOST and PROD_HOST

5. Your production settings now go exclusively inside **settings_prod.py**. Change what you need there. Everything that is global is still inside **settings.py**.
