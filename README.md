# Rekstone Bank

## Setup

Run the following commands to setup the application

```
# setup virtual environment
python -m venv venv

# if on windows 
venv\scripts\activate

# if on linux
source venv/bin/activate

# if on mac
# get a windows or linux pc

# install requirements
pip install -r requirements.txt

# collect static
python manage.py collectstatic --no-input
```

To start the server, run the following command

```
python manage.py runserver
```

## Admin Access

In order to access the admin dashboard you'd need to create a superuser by running the command below and following the prompt
```
python manage.py createsuperuser
```

Once done, start the server and visit the `/admin` endpoint