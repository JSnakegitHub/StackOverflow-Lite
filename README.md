# StackOverflow-Lite
## Andela Challenge 2
[![Build Status](https://travis-ci.org/JSnakegitHub/StackOverflow-Lite.svg?branch=post_an_answer_api)](https://travis-ci.org/JSnakegitHub/StackOverflow-Lite)
[![Coverage Status](https://coveralls.io/repos/github/JSnakegitHub/StackOverflow-Lite/badge.svg?branch=post_an_answer_api)](https://coveralls.io/github/JSnakegitHub/StackOverflow-Lite?branch=post_an_answer_api)

## Installation Instructions for the app:
1. Install Flask using `pip install flask`
2. Clone the app using `git clone https://github.com/JSnakegitHub/StackOverflow-Lite.git`

## Getting Started With Tests:
### For Python 2:
1. `pip install pytest`
### For Python 3:
1. `pip3 install pytest`
## Running the tests on a virtual environment
### For python 2:
1. `pip install -U virtualenv`
2. `python -m virtualenv venv`
3. `source venv/bin/activate` # in Windows -> venv\Scripts\activate.bat
4. `pip install pytest`
### For Python 3:
1. `pip3 install -U virtualenv`
2. `python3 -m virtualenv venv`
3. `source venv/bin/activate` # in Windows -> venv\Scripts\activate.bat
4. `pip install pytest`
### For Python 3.6+:
2. `python3 -m venv venv`
3. `source venv/bin/activate` # in Windows -> venv\Scripts\activate.bat
4. `pip install pytest`
### What The Tests Are Testing:
1. If the required endpoints are rendered.
2. If the requests are being sent in the right format (JSON-JavaScript Object Notation).
3. If Validations are being respected

## Testing the App Locally.
1. Use [Postman](https://www.getpostman.com/) to test the application locally
2. Move to the project directory locally
3. Once you are in the project's root directory, run the command `python run.py`.
4. At this point the server should be running.
5. The application is set to run on port 8080, so the URL for testing this api is `127.0.0.1:8080/api/v1/questions/question_id/answers`. 
6. Testing for this API requires use of Postman.
7. The above instruction should be able to return all the questions in the data structure when you paste the test URL.

## Deployment
1. The app can be deplyed on Heroku following the Heroku [Documentation](https://devcenter.heroku.com/categories/reference).

## Contributing
Contributions for this project is allowed.
## Versioning
GitHub was used to help track the different versions of the project. 

## Authors
1. Walter Nyeko, under supervision of Hadijah Kyampeire
## License
1. This project is licensed under the Andela License

