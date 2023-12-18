# Week 5

## The Story So Far...

## Why Do We Need an API?

## Adding DRF

### Installation Steps
- `pip install djangorestframework`
- In `settings.py` add `rest_framework` to the `INSTALLED_APPS` list
- Create a new `api` app (or package)
- "hook up" urls

### Create the Serializer class

- Inherits from the `serializer.ModelSerializer` class
- Create your `Meta` class

### Create the API views

- import the Serializer and model
- import the viewsets
- Create a class viewset inheriting from `viewsets.ModelViewSet`
    - Add `serializer_class` attribute
    - Add `queryset` attribute

### Set up URLS

- import the `routers` module
- create instance of `DefaultRouter`
- register `router.register(regex, viewset, basename)`
- `urlpatterns = router.urls`
- Add to project level urls.py

### DRF UI and Testing w/ Postman

### Let's Look at the DRF Documentation
- [Main Page](https://www.django-rest-framework.org/)
- [Model Serializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)
- [Model Viewsets](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)
- [Router](https://www.django-rest-framework.org/api-guide/routers/)
