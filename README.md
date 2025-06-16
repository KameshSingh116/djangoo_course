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

### We will use the render function to render or display a html page on the starting page or whereever we want.

Using the context keyword we can send a dynamic data from backend to the frontend page.

{{% %}}
is used to perform further functions like turning the backend dynamic list data into tables in frontend.

{{ text |truncatechars:5 }}
This is used for slicing the content from a particulr position.