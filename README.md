# djangoo_course
We first setupp the django project using

django-admin startproject <project-name>

cd <project-name>

python manage.py startapp <app-name>

Then to run/boot the project , 
we use

python manage.py runserver

## To run on custom port
python manage.py runserver 0.0.0.0:<custom port number>

also update the installed apps list in the settings.py bu addin the names of the created apps.

# All the logical stuff includiing what we want to send from the backend to the frontend is written in the views
