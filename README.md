# iClinic Test

## Install
cd iclinic-test

## Create virtualenv and activate
python3 -m venv venv
. venv/bin/activate

## Install requirements
pip install -r requirements.txt

## Run tests
coverage run --source=app -m unittest discover -s tests/

## Run app
export FLASK_APP=app
export FLASK_ENV=development
flask run