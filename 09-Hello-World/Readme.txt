> powershell -Command "Copy-Item -Recurse 08-Django-Project 09-Hello-World"
> cd 09-Hello-World
> python manage.py startapp myapp

Edit mysite app settings.py file and add myapp to the INSTALLED_APPS list


9.3 Creating template files

create folder in myapp folder name templates
create folder in templates folder name myapp
create file in myapp "index.html"

#Project repo looks like 09-Hello-World > myapp > templates > myapp > index.html 

index.html > <h1>Hello world! This is myapp index view. </h1>

9.4 Creating Views
myapp > views.py > add index function

def index(request):
    return render(request, 'myapp/index.html')

9.5 Adding a homepage path
mysite > urls.py > from myapp import views as myapp_views

   path('',myapp_views.index, name='index').

> python manage.py runserver