# Sentiment analysis using Django

A project to get and analysis sentimento from facebook page posts

## Features

- GET Facebook page posts comments
- View to display sentiment analysis

## How to Use

1. Create your working environment inside a dir with `$ python3 -m venv env`
2. Activate Virtual Env with `$ source env/bin/activate`
3. Install the requirements (`$ pip install -r dev-requirements.txt`)
4. `$ Make migrations`
5. `$ Make migrate`
6. `$ Make run`

## Deployment to Heroku

First install heroku toolbelt to use this..
After your finish the release follow this steps.

    $ heroku git:remote
    $ git add .
    $ git commit -m "Initial commit"
	$ git push heroku master

And done :)
