powershell -Command "Copy-Item -Recurse 10-first 11-template-inherit"


> django-admin startproject mysite .
> python manage.py startapp myapp1

Edit mysite app settings.py file and add myapp1 to the INSTALLED_APPS list

#Creating template files

create folder in myapp1 folder name templates
create folder in templates folder name myapp
create file in myapp "index.html"

index.html > <h1>Hello world! This is myapp1 index view. </h1>

# Creating Views
myapp > views.py > add index function

def index(request):
    return render(request, 'myapp/index.html')

# Adding a homepage path
mysite > urls.py > from myapp1 import views as myapp_views

   path('',myapp_views.index, name='index'),

# Register models in admin.py files
myapp1/admin.py

from myapp1.models import Post
admin.site.register(Post)

# change Configuration to human readable name for this app
myapp1/apps.py

verbose_name = "Excellent App"


# models files
myapp1/models.py

class Flower(models.Model):
    title = models.CharField(max_length=255, default='')

> python manage.py runserver
