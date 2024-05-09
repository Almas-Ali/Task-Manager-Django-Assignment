# Task Manager Django Application - Assignment for Mediusware

Total Coding Time: [![wakatime](https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/f0000eeb-a292-46e5-861a-446c30a08b97.svg)](https://wakatime.com/badge/user/168edf9f-71dc-49cc-bf77-592d9c9d4eed/project/f0000eeb-a292-46e5-861a-446c30a08b97)

## Installation Guide

```bash
# Clone the repository
git clone https://github.com/Almas-Ali/Task-Manager-Django-Assignment

# Change the directory
cd Task-Manager-Django-Assignment

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Linux)
source venv/bin/activate

# Recreate the .env file (Windows)
copy .env.example .env

# Recreate the .env file (Linux)
cp .env.example .env

# Set the secret key in the .env file
# Site settings and database configurations

# Install the requirements
pip install -r requirements.txt

# Load the initial data
python manage.py loaddata initial_data.json

# Run the server
python manage.py runserver
```

Data has been dumped with the following credentials:

```bash
python manage.py dumpdata --indent 2 > initial_data.json
```

Demo User Credentials:

- Username: `test`
- Username: `test2`
- Username: `test3`
- Password: `1234`

What to create your own superuser?

```bash
# Create a superuser
python manage.py createsuperuser
```
