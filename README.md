[![Build Status](https://travis-ci.org/owezzy/StoreManager.svg?branch=develop)](https://travis-ci.org/owezzy/StoreManager)
[![Maintainability](https://api.codeclimate.com/v1/badges/d8e04cb04dc6460d7e89/maintainability)](https://codeclimate.com/github/owezzy/StoreManager/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/owezzy/StoreManager/badge.svg?branch=ch-test-api-endpoints-161203421)](https://coveralls.io/github/owezzy/StoreManager?branch=ch-test-api-endpoints-161203421)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e58262b320d743418f09de2743b35ac0)](https://app.codacy.com/app/owezzy/StoreManager?utm_source=github.com&utm_medium=referral&utm_content=owezzy/StoreManager&utm_campaign=Badge_Grade_Dashboard)
# StoreManager - API


Store Manager is a web application that helps store owners manage sales and product inventory
records. This application is meant for use in a single store.

## Running a local copy of the Application
- [Here](https://github.com/owezzy/StoreManager.git) - Clone the repository from link.

- Navigate to root of your application and run:
- Create a virtual environment
   `$ python3 -m venv venv` these creates a python virtual environment called `venv`

- activate the virtual environment
   `$ source venv/bin/activate`

- install dependencies needed for the project to run
   `$ pip install -r requirements.txt`

- export FLASK_APP enviroment variable
  `$ export FLASK_APP=run.py`

- run the application using `flask run`

- a server should be deployed at `http://127.0.0.1:5000/ `


 ## API ROUTES
- Using Postman the following endpoints can be accessed:

 
| Methods | Url                                            |      Description         |
| -------:|:----------------------------------------------:|-------------------------:|
| POST    | http://127.0.0.1:5000/api/v1/products          |   create a product       | 
| POST    | http://127.0.0.1:5000/api/v1/sales             |  create a sale record    | 
| GET     | http://127.0.0.1:5000/api/v1/products          |  Fetch all product       |       
| GET     | http://127.0.0.1:5000/api/v1/sales             |  Fetch all sales         |      
| GET     | http://127.0.0.1:5000/api/v1/product/<int: id> |  Fetches a single product|
| GET     | http://127.0.0.1:5000/api/v1/sale/<int: id>    |  Fetches a single sale   |

## RUN TEST
To run the tests, in your terminal from the root folder run



## Built With

- <a href="https://owezzy.github.io/StoreManager/" target="_blank">DEMO </a>

- [Flask](https://flask.readthedocs.io/en/rtd/) - Used to style HTML pages.

- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - Used extend the Flask application.

## Versioning

The project uses [Gitflow](https://datasift.github.io/gitflow/IntroducingGitFlow.html) for versioning.

## Authors

 **Owen Adira** - _Initial work_ - [owezzy](https://github.io/owezzy)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
