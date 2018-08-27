# iClinic Test

Clone project:
```sh
git clone https://github.com/rodrigosavian/iclinic-test.git
cd iclinic-test
```

Create virtualenv and activate:
```sh
python3 -m venv venv
. venv/bin/activate
```

Install requirements:
```sh
pip install -r requirements.txt
```

Run tests:
```sh
coverage run --source=app -m unittest discover -s tests/
```

Run app:
```sh
export FLASK_APP=app
export FLASK_ENV=development
flask run
```