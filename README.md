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

## Django Template Tags (credits to docs.djangoproject.com)
[Visit This Link](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/)


When we will go throgh the HTML code of all the three files, we will see that there are some portions completely same as that of others.|

## Here comes the concept of DRY(Don't Repeat Yourself) in OOP
TO follow this up we will make a base.html file and then keep the common stuff in it then using the django template tags , we will make them accesible by the files which need them.

## Now we are going to study about models and migrations.
### This is the heart and the most important stuff in the backend development.

 - we make a class (which becomes our model).
 - then we give models.Model as the argument to that class.

 class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()
    -- this is the example model structure.



     dependencies = [
        ('home', '0001_initial'),
    ]

    these are the changes in the dependencies list that we see when we add some arguments to the fields after the first makemigrations.


This was the lecture on models and migrations.
#### To see/read the sqlite/sqlite3 files we can use "DB Browser"

## "Django Shell"
Its a bridge to interact with the files through the terminal/shell which is in many cases comvenient

To enter the django shell we will you the command 
- python manage.py shell


Think of a file which imports or uses some components of some file of django's components or django related components, then the direct execution of that file is not allowed....

##### so here comes the role of django shell which helps to execute that file or function of that file or any component of that file without any error.

## CRUD operations in Django for records
### C - Create
### R - Read
### U - Update
### D - Delete

By visiting some sites we can know several operations under these all 4 catgories.

## Practice well and make projects to be confident.
# Radhe Radhe Hare Krishn