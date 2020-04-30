# User django app

## Description
This is a django app for user control

```shell script
$ tree -I 'migrations|__pycache__' user
user
├── admin.py
├── apps.py
├── forms.py
├── __init__.py
├── managers.py
├── models.py
├── README.md
├── serializers.py
├── template
│   ├── baseNone.html
│   ├── baseNone.html.py
│   ├── changepassword.html
│   ├── changepassword.html.py
│   ├── login.html
│   ├── login.html.py
│   ├── _profile.html
│   ├── _profile.html.py
│   ├── register.html
│   ├── register.html.py
│   ├── user_change_avatar.html
│   └── user_change_email.html
├── tests.py
├── urls.py
├── viewsets.py
└── views.py
```

## Installation
* Install django rest framework and pillow
```shell script
$ pip install djangorestframework markdown django-filter pillow
```
* Clone the application at the project root
```shell script
$ git submodule add git@github.com:ViniciusNunesMartins/user.git
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
  * MEDIA_URL and MEDIA_ROOT
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
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
