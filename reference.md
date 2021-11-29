## Start project
`django-admin startproject vidly`

## Start server
`python manage.py runserver`

## Migrate
`python manage.py makemigrations`
`python manage.py migrate`

## Create app template
`python manage.py startapp movies`

## Show SQLMigrate
Command that gets called internally to make the updates to the database.
`python manage.py sqlmigrate movies 0001`

## User
`python manage.py createsuperuser`


## Deployment on Heroku
- Setup Heroku account
- Install heroku-cli `brew install heroku/brew/heroku`
- Web process `pipenv install gunicorn`
- `touch Procfile` for heroku: `web: gunicorn vidly.wsgi`
- set static folder in `settings.py` and `mkdir`
- collect static `python manage.py collectstatic`
- to serve static on heroku: `pipenv install whitenoise`
- add whitenoise middleware after `SecurityMiddleware`: `whitenoise.middleware.WhiteNoiseMiddleware`
- add to git from work_dir
- `heroku login`
- `heroku create`
- `git push heroku master` push to heroku remote git
- deploy: `heroku ps:scale web=1`
- add to allowed hosts in `settings.py`, add, commit, push
- `heroku open`
