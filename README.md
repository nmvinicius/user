# User django app

## Description
This is a django app for user control

## Installation
* Install django rest framework
```shell script
$ pip install djangorestframework markdown django-filter
```
* Clone the application at the project root
```shell script
$ git clone git@github.com:ViniciusNunesMartins/user.git
```
* Now, just add the following variables in <project_name>/settings.py
  * INSTALLED_APPS
  ```python
  INSTALLED_APPS = [
    #...
    'rest_framework',
    'user.apps.UserConfig',
  ]
  ```
  * TEMPLATES
  ```python
  TEMPLATES = [
    {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [
        os.path.join(BASE_DIR, 'template'),
        os.path.join(BASE_DIR, 'user/template')
      ],
      'APP_DIRS': True,
      'OPTIONS': {
        'context_processors': [
          'django.template.context_processors.debug',
          'django.template.context_processors.request',
          'django.contrib.auth.context_processors.auth',
          'django.contrib.messages.context_processors.messages',
        ],
      },
    },
  ]
  ```
  * AUTH_USER_MODEL, LOGIN_URL and SITE_ID
  ```python
  AUTH_USER_MODEL = 'user.User'

  LOGIN_URL = '/user/login/'
  
  SITE_ID = 1
  ```
  * REST_FRAMEWORK
  ```python
  REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
      'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
  }
  ```
* Add app routes to project routes at <project_name>/urls.py
```python
from django.urls import path, include

urlpatterns = [
  #...
  path('user/', include("user.urls")),
  path('api-auth/', include('rest_framework.urls'))
]

```
* And run makemigrations and migrate
```shell script
$ python manage.py makemigrations
$ python manage.py migrate
```
