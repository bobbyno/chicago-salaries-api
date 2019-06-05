# Chicago Salaries Data API

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true) article - check it out.

* sign up for a free Heroku account at https://signup.heroku.com/python
* Install the Heroku CLI: `brew install heroku/brew/heroku`


## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

```
* Fork this repo on github
* Clone your fork and cd into that directory
* Create a new virtualenv for this API
* Run `make requirements` to install the requirements for the API
* Run `heroku local`

```

Your app should now be running on [localhost:5000](http://localhost:5000/).

Visit `http://localhost:5000/employees` to see the list of employees in JSON.


## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
