# test_project

A simple Django project that returns سلام.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ai-agent-1955/test.git
   cd test
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Django:
   ```bash
   pip install django
   ```

4. Create a new Django project:
   ```bash
   django-admin startproject myproject .
   ```

5. Create a new app:
   ```bash
   python manage.py startapp myapp
   ```

6. Add the app to `settings.py`:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'myapp',  # Add your app here
   ]
   ```

7. Create a view in `myapp/views.py`:
   ```python
   from django.http import HttpResponse

   def hello(request):
       return HttpResponse('سلام')
   ```

8. Add a URL pattern in `myapp/urls.py`:
   ```python
   from django.urls import path
   from .views import hello

   urlpatterns = [
       path('hello/', hello),
   ]
   ```

9. Include the app's URLs in `myproject/urls.py`:
   ```python
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),  # Include your app's URLs
   ]
   ```

10. Run the server:
    ```bash
    python manage.py runserver
    ```

Now you can access the app at `http://127.0.0.1:8000/hello/` to see the سلام message!