To run the webapp:

1. Create a virtual environment as described in the tutorial.
1. Install packages with `pip install -r requirements.txt`.
1. Activate the virtual environment by running `source env/bin/activate` (Linux/MacOS) or `env\scripts\activate` (Windows).
1. Create and initialize the database by running `python manage.py migrate`.
1. Create a superuser as described at the end of the tutorial.
1. To Run this server locally use `python manage.py runserver`